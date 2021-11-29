import psycopg2
import datetime
# Settings for test
HOST = "127.0.0.1"
PORT = "5433"
DB_NAME = "translation_memory"
USER = "postgres"
PASSWORD = "100542"

conn = psycopg2.connect(
    user=USER,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    database=DB_NAME
)

cursor = conn.cursor()
try:
    # # Создаем БД
    # sql_create_database = f"create database {DB_NAME}"
    # cursor.execute(sql_create_database)
    # conn.commit()
    # print("DB was created")

    # Вставляем таблицу
    # create_table_query = '''
    # CREATE TABLE cat_tmgroup (
    # id INT PRIMARY KEY NOT NULL,
    # updated_at TIMESTAMP WITH TIME ZONE NOT NULL
    # );
    # '''
    # cursor.execute(create_table_query)
    # conn.commit()
    # print("Table was created")

    # create_table_query = '''
    # CREATE TABLE cat_sourceunit (
    # id INT PRIMARY KEY NOT NULL,
    # text TEXT NOT NULL
    # );
    # '''
    # cursor.execute(create_table_query)
    # conn.commit()
    # print("Source unit was created")
    #
    # create_table_query = '''
    # CREATE TABLE cat_translationunit (
    # id INT PRIMARY KEY NOT NULL,
    # text TEXT NOT NULL
    # );
    # '''
    # cursor.execute(create_table_query)
    # conn.commit()
    # print("Translation unit was created")
    #
    # create_table_query = '''
    # CREATE TABLE cat_tmunit (
    # tm_group_id INT PRIMARY KEY NOT NULL,
    # translation_unit_id INT NOT NULL,
    # source_unit_id INT NOT NULL,
    # language_id INT NOT NULL
    # );
    # '''
    # cursor.execute(create_table_query)
    # conn.commit()
    # print("TM unit was created")


    # Вставляем значения 1
    # insert_query_1 = """INSERT INTO cat_translationunit (id, text) VALUES (100, 'Russian Federation')"""
    # insert_query_2 = """INSERT INTO cat_translationunit (id, text) VALUES (200, 'Hi! I am Boris.')"""
    # insert_query_3 = """INSERT INTO cat_translationunit (id, text) VALUES (300, 'The current procedure is briefly called PSG.')"""
    #
    # cursor.execute(insert_query_1)
    # print("1")
    # cursor.execute(insert_query_2)
    # print("2")
    # cursor.execute(insert_query_3)
    # print("3")
    # conn.commit()

    # # Вставляем значения 2
    # insert_query_1 = """INSERT INTO cat_sourceunit (id, text) VALUES (10, 'Россия')"""
    # insert_query_2 = """INSERT INTO cat_sourceunit (id, text) VALUES (20, 'Здравствуйте! Меня зовут Борис Викторович.')"""
    # insert_query_3 = """INSERT INTO cat_sourceunit (id, text) VALUES (30, 'Данная процедура именуется в реестре как Согласование Отделом Надежности')"""
    #
    # cursor.execute(insert_query_1)
    # print("4")
    # cursor.execute(insert_query_2)
    # print("5")
    # cursor.execute(insert_query_3)
    # print("6")
    # conn.commit()

    # Вставляем значения 3
    now = datetime.datetime.now()
    now_utc = "{:%d-%m-%Y %H:%M:%S}".format(now)
    print(now_utc)
    insert_query_1 = """INSERT INTO cat_tmgroup (id, updated_at) VALUES (110, to_timestamp('16-05-2011 15:36:38', 'dd-mm-yyyy hh24:mi:ss'))"""
    insert_query_2 = f"""INSERT INTO cat_tmgroup (id, updated_at) VALUES (220, to_timestamp(\'{now_utc}\', 'dd-mm-yyyy hh24:mi:ss'))"""
    insert_query_3 = f"""INSERT INTO cat_tmgroup (id, updated_at) VALUES (330, to_timestamp(\'{now_utc}\', 'dd-mm-yyyy hh24:mi:ss'))"""

    cursor.execute(insert_query_1)
    print("7")
    print(insert_query_2)
    cursor.execute(insert_query_2)
    print("8")
    cursor.execute(insert_query_3)
    print("9")
    conn.commit()


    # # Вставляем значения 4
    # insert_query_1 = """INSERT INTO cat_tmunit (translation_unit_id, source_unit_id, tm_group_id, language_id) VALUES (100, 10, 110, 72)"""
    # insert_query_2 = """INSERT INTO cat_tmunit (translation_unit_id, source_unit_id, tm_group_id, language_id) VALUES (200, 20, 220, 72)"""
    # insert_query_3 = """INSERT INTO cat_tmunit (translation_unit_id, source_unit_id, tm_group_id, language_id) VALUES (300, 30, 330, 72)"""
    #
    # cursor.execute(insert_query_1)
    # print("10")
    # cursor.execute(insert_query_2)
    # print("11")
    # cursor.execute(insert_query_3)
    # print("12")
    # conn.commit()
except Exception as er:
    print(f'Some problems: {er}')
finally:
    cursor.close()
    conn.close()