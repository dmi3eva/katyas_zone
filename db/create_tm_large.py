import psycopg2
import datetime
import pandas as pd
# Settings for test
HOST = "127.0.0.1"
PORT = "5433"
DB_NAME = "translation_memory_large"
USER = "postgres"
PASSWORD = "100542"

conn = psycopg2.connect(
    user=USER,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    database=DB_NAME
)

data = pd.read_csv("data/synt_un_ltc_50000.csv", sep=";")
size = len(data)

cursor = conn.cursor()
try:
    # # Создаем БД
    # sql_create_database = f"create database {DB_NAME}"
    # cursor.execute(sql_create_database)
    # conn.commit()
    # print("DB was created")

    # # Вставляем таблицу
    # create_table_query = '''
    # CREATE TABLE cat_tmgroup (
    # id INT PRIMARY KEY NOT NULL,
    # updated_at TIMESTAMP WITH TIME ZONE NOT NULL
    # );
    # '''
    # cursor.execute(create_table_query)
    # conn.commit()
    # print("Table was created")
    #
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
    # print("tmunit was created")

    # # Вставляем значения 1
    # for ind, _row in data.iterrows():
    #     ind += 1
    #     if ind % 100 == 0:
    #         print(f"{ind} / {size}")
    #     text = _row['ref_en'].replace("\"", "").replace("\'", "")
    #     insert_query = f"""INSERT INTO cat_translationunit (id, text) VALUES ({ind}, \'{text}\')"""
    #     # print(insert_query)
    #     cursor.execute(insert_query)
    # print("Done")
    # conn.commit()

    # # Вставляем значения 2
    # for ind, _row in data.iterrows():
    #     ind += 1
    #     if ind % 100 == 0:
    #         print(f"{ind} / {size}")
    #     text = _row['ref_ru'].replace("\"", "").replace("\'", "")
    #     insert_query = f"""INSERT INTO cat_sourceunit (id, text) VALUES ({ind}, \'{text}\')"""
    #     # print(insert_query)
    #     cursor.execute(insert_query)
    # print("Done")
    # conn.commit()

    # # Вставляем значения 3
    # now = datetime.datetime.now()
    # now_utc = "{:%d-%m-%Y %H:%M:%S}".format(now)
    #
    # for ind, _row in data.iterrows():
    #     ind += 1
    #     if ind % 100 == 0:
    #         print(f"{ind} / {size}")
    #     if ind % 2 == 0:
    #         insert_query = f"""INSERT INTO cat_tmgroup (id, updated_at) VALUES ({ind}, to_timestamp('16-05-2021 15:36:38', 'dd-mm-yyyy hh24:mi:ss'))"""
    #     else:
    #         insert_query = f"""INSERT INTO cat_tmgroup (id, updated_at) VALUES ({ind}, to_timestamp(\'{now_utc}\', 'dd-mm-yyyy hh24:mi:ss'))"""
    #     cursor.execute(insert_query)
    # print("Done")
    # conn.commit()


    # # Вставляем значения 4
    for ind, _row in data.iterrows():
        ind += 1
        if ind % 100 == 0:
            print(f"{ind} / {size}")
        insert_query = f"""INSERT INTO cat_tmunit (translation_unit_id, source_unit_id, tm_group_id, language_id) VALUES ({ind}, {ind}, {ind}, 72)"""
        cursor.execute(insert_query)
    print("Done")
    conn.commit()
except Exception as er:
    print(f'Some problems: {er}')
finally:
    cursor.close()
    conn.close()