from re import X
import prettytable
import colorama
from sqlalchemy import create_engine, text, inspect
from urllib.parse import quote_plus
import pwinput
import time
import os
import requests

logo = f"""{colorama.Fore.RED}{colorama.Style.BRIGHT}
====================================================================================================================

███╗   ██╗ █████╗ ██╗   ██╗██╗ ██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
████╗  ██║██╔══██╗██║   ██║██║██╔════╝ ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗  
██╔██╗ ██║███████║██║   ██║██║██║  ███╗███████║   ██║   ██║   ██║██████╔╝ 
██║╚██╗██║██╔══██║╚██╗ ██╔╝██║██║   ██║██╔══██║   ██║   ██║   ██║██╔══██╗
██║ ╚████║██║  ██║ ╚████╔╝ ██║╚██████╔╝██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═╝  ╚═══╝╚═╝  ╚═╝  ╚═══╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝  {colorama.Fore.GREEN}MADE BY {colorama.Fore.BLUE}MIGRDEV {colorama.Fore.GREEN}DISCORD: {colorama.Fore.BLUE}migrdev_buy {colorama.Fore.RED}
===================================================================================================================={colorama.Fore.RESET}
"""
print(logo)

DB_CONNECT = False
TYPE_DB = ""

DB_EXISTS = {
    "1": "PostgreSQL",
    "2": "MySQL",
    "3": "MariaDB",
    "4": "Oracle",
    "5": "SQL Server (MSSQL)",
}
DB_EXISTS_LIST = [
    "postgresql+psycopg2",
    "mysql+mysqlconnector",
    "mariadb+mariadbconnector",
    "mssql+pyodbc",
]
BANCOS_DEFAULT = {
    "1": "postgres",  # PostgreSQL
    "2": "",  # MySQL (pode ser vazio)
    "3": "",  # MariaDB
    "4": "xe",  # Oracle (comum em instâncias locais)
    "5": "master",  # SQL Server
}
DEFAULT_PORT = True


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


IP = ""
USER = ""
PASSWORD = ""
PORT = ""
TYPE = ""

def engine_create_engine(banco):
    global IP, USER, PASSWORD, PORT, TYPE
    PASSWORD = quote_plus(PASSWORD)
    url = f"{TYPE}://{USER}:{PASSWORD}@{IP}:{PORT}/{banco}"
    engine = create_engine(url=url)
    try:
        with engine.connect() as conexao:
            print("🚀 Conectando... ")

            resultado = conexao.execute(text("SELECT 1"))
            if resultado:
                print(f"✅ CONECTADO! O banco respondeu com sucesso.")
                print("Aguardando 2 segundos...")
                time.sleep(2)
                clear()
                dashboard(engine)

    except Exception as e:
        print(f"❌ ERRO DE CONEXÃO: \n{e}")


def dashboard(engine):
    db_escolhido = ""
    db_db = engine
    while True:
        with db_db.connect() as conexao:
            escolha = input(
                f"{colorama.Fore.CYAN}===================================\nO que você deseja fazer?\n1- Listar Bancos de Dados\n2- Entrar no Banco de Dados\n3- Listar tabelas\n4- Ler tabela\n5- Executar Comando SQL\n==================================={colorama.Fore.RED}\n\n>>> {colorama.Fore.RESET}"
            )
            if escolha.lower() in ["1", "2", "3", "4","5"]:
                match escolha:
                    case "1":
                        query_bancos = text(
                            "SELECT datname FROM pg_database WHERE datistemplate = false;"
                        )
                        procura_bancos = conexao.execute(query_bancos)
                        lista_bancos = [linha[0] for linha in procura_bancos]
                        print()
                        print(f"📂 Bancos de dados encontrados no servidor:")
                        qnt = 1
                        print()
                        for banco in lista_bancos:
                            print(f"{qnt} - {banco}")
                            qnt += 1
                        print()
                    case "2":
                        qnt = 1
                        print()
                        for banco in lista_bancos:
                            print(f"{qnt} - {banco}")
                            qnt += 1
                        print()
                        db = input("Digite o número do banco de dados: ")
                        engine_create_engine(banco=lista_bancos[int(db)-1])
                        print()
                    case "3":
                        inspector = inspect(engine)
                        print()
                        print(f"📋 Tabelas Encontradas:")
                        tabelas = inspector.get_table_names()
                        qnt = 1
                        print()
                        for tabela in tabelas:
                            print(f"{qnt} - {tabela}")
                            qnt += 1
                        print()
                    case "4":
                        print()
                        print(f"📋 Listar tabela:")
                        print()
                        qnt = 1
                        for tabela in tabelas:
                            print(f"{qnt} - {tabela}")
                            qnt += 1
                        print()
                        tabela_escolhida = input("Digite o número da tabela: ")
                        execute = conexao.execute(text(f"SELECT * FROM {tabelas[int(tabela_escolhida)-1]}"))
                        colunas = list(execute.keys())
                        # lista_tabela = [linha for linha in execute]
                        tabela = prettytable.PrettyTable()
                        tabela.field_names = colunas
                        tabela.align = "l"
                        tabela.max_width = 38
                        for tuple_tabela in execute:
                            tabela.add_row(tuple_tabela)
                            
                        print(tabela)
                    case "5":
                        print("""
                                🛠️  MANIPULAÇÃO DE ESTRUTURA (ALTER):
                                • ALTER TABLE tabela ADD COLUMN nova_coluna TEXT;  (Adiciona coluna)
                                • ALTER TABLE tabela RENAME COLUMN antigo TO novo; (Muda nome da coluna)
                                • ALTER TABLE tabela DROP COLUMN coluna;           (Apaga uma coluna)
                                
                                🚀 COMANDOS BÁSICOS:
                                • INSERT INTO tabela (coluna) VALUES ('valor');
                                • DELETE FROM tabela WHERE id = 1;
                                • DROP TABLE tabela; (Apaga a tabela toda!)
                        """)
                        command = input("👉 Digite o comando EX: INSERT INTO : ")
                        conexao.execute(text(command))
                        print("🚀 Comando Executado")
                        conexao.commit()


def connect(ip, user, password, port, type_db, banco):
    global DB_EXISTS_LIST, IP, USER, PASSWORD, PORT, TYPE
    type = DB_EXISTS_LIST[int(type_db) - 1]
    IP = ip
    USER = user
    PASSWORD = password
    PORT = port
    TYPE = type

    password = quote_plus(password)

    url = f"{type}://{user}:{password}@{ip}:{port}/{banco}"

    engine = create_engine(url=url)
    try:
        with engine.connect() as conexao:
            print("🚀 Conectando... ")

            resultado = conexao.execute(text("SELECT 1"))
            if resultado:
                print(f"✅ CONECTADO! O banco respondeu com sucesso.")
                print("Aguardando 2 segundos...")
                time.sleep(2)
                clear()
                dashboard(engine)

    except Exception as e:
        print(f"❌ ERRO DE CONEXÃO: \n{e}")


def home():
    global DB_CONNECT, TYPE_DB, DB_EXISTS, DEFAULT_PORT, BANCOS_DEFAULT
    
    print("Welcome! Seja muito bem-vindo!")
    if DB_CONNECT == False:
        print("Vamos conectar ao Banco de Dados Primeiro!\n")
        time.sleep(2)
        for key, value in DB_EXISTS.items():
            print(f"{key} - {value}")
        print()
        type_db = input("Qual é o banco de dados?: ")
        db_padrao = BANCOS_DEFAULT.get(type_db, "")
        db_name = input(f"Digite o nome do banco (Padrão: {db_padrao}): ") or db_padrao
        ip = input("Digite o IP/URL do banco de dados: ")
        user = input("Digite o usuário do banco de dados: ")
        password = pwinput.pwinput(
            prompt="Digite a senha do banco de dados: ", mask="*"
        )
        port = input(
            "Deseja selecionar uma porta específica? (Para Padrão Digite ENTER): "
        )

        if type_db not in ["1", "2", "3", "4", "5"]:
            print("Por favor selecione um banco de dados existente!")
            time.sleep(2)
            home()

        if ip == "":
            print("Por favor selecione um IP válido!")
            time.sleep(2)
            home()

        if port != "":
            DEFAULT_PORT = False
        elif type_db == "1":
            port = 5432
        elif type_db == "2" or type_db == "3":
            port = 3306
        elif type_db == "4":
            port = 1521
        elif type_db == "5":
            port = 1433

        connect(ip, user, password, port, type_db, db_name)


home()
