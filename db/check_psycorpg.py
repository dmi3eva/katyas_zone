import psycopg2

# # Settings for Alpha
# HOST = "tklid-monit0001.vm.mos.cloud.sbrf.ru"
# PORT = "5433"
# DB_NAME = "aiadviserdb"
# USER_1 = "aiadviser_admin"
# PASSWORD_1 = "aiadviser0TEST$Admin123"
# USER_2 = "aiadviser"
# PASSWORD_2 = "aiadviser0TEST$User123"
# USER = USER_1
# PASSWORD = PASSWORD_1

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

cursor = conn.cursor()
try:
    query_1 = """
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema = 'public'
    ORDER BY table_name;
    """
    cursor.execute(query_1)
    print('Done')
    records = cursor.fetchall()
    print(records)

    query_2 = """
        SELECT *
        FROM cat_tmgroup
    """
    cursor.execute(query_2)
    print('Done')
    records = cursor.fetchall()
    print(records)

    query_3 = """
    SELECT 
       table_name, 
       column_name, 
       data_type 
    FROM 
       information_schema.columns
    WHERE 
       table_name = 'cat_tmgroup';
    """
    cursor.execute(query_3)
    print('Done')
    records = cursor.fetchall()
    print(records)

    last_update = f"to_timestamp('16-05-2011 15:36:38', 'dd-mm-yyyy hh24:mi:ss')"
    query_4 = f"""
    SELECT cat_tmgroup.id, cat_tmgroup.updated_at, cat_sourceunit.text AS source, cat_translationunit.text AS translation 
    FROM cat_tmunit 
    INNER JOIN cat_translationunit  
        ON cat_translationunit.id=cat_tmunit.translation_unit_id 
    INNER JOIN cat_sourceunit  
        ON cat_sourceunit.id=cat_tmunit.source_unit_id 
    INNER JOIN cat_tmgroup  
        ON cat_tmgroup.id=cat_tmunit.tm_group_id 
    WHERE cat_tmunit.language_id IN (20, 72) AND cat_tmgroup.updated_at > {last_update};
    """
    # query_4 = f"""
    # SELECT  cat_tmunit.tm_group_id , cat_sourceunit.text AS source, cat_translationunit.text AS translation
    # FROM cat_tmunit
    # INNER JOIN cat_translationunit
    #     ON cat_translationunit.id=cat_tmunit.translation_unit_id
    # INNER JOIN cat_sourceunit
    #     ON cat_sourceunit.id=cat_tmunit.source_unit_id
    # """
    cursor.execute(query_4)
    print('Done main')
    records = cursor.fetchall()
    print(records[:3])

    # query_5 = f"""
    # SELECT *
    # FROM cat_tmgroup
    # """
    # cursor.execute(query_5)
    # print('Done 5')
    # records = cursor.fetchall()
    # print(records)
except:
    print('Some problems')
finally:
    cursor.close()
    conn.close()


