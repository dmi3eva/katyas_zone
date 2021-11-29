import json
import collections
import sqlite3
import os

REQUEST_MASK = "SELECT \"{column}\" FROM \"{table}\""

from IPython.display import HTML, display

def progress(value, max=100):
    return HTML("""
        <progress
            value='{value}'
            max='{max}',
            style='width: 100%'
        >
            {value}
        </progress>
    """.format(value=value, max=max))

class SpiderDB:
    def __init__(self):
        self.db_path = None
        self.__dbs = None
        self.__tables = None
        self.__columns = None

    @property
    def dbs(self):
        if not self.__dbs:
            self.__dbs = self.get_dbs
        return self.__dbs

    @property
    def tables(self):
        if not self.__tables:
            self.__tables = self.get_tables
        return self.__tables

    @property
    def columns(self):
        if not self.__columns:
            self.__columns = self.get_columns
        return self.__columns

    def get_dbs(self):
        pass

    def get_tables(self):
        pass

    def get_columns(self):
        pass

    def execute_request(self, db_id, sql):
        db = os.path.join(self.db_path, db_id, db_id + ".sqlite")
        conn = sqlite3.connect(db)
        conn.text_factory = lambda b: b.decode(errors='ignore')
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            res = cursor.fetchall()
            return res
        except:
            raise ValueError

    def get_values(self, db, table, column):
        # Возвращает значения из столбца данной таблицы
        aim_request = REQUEST_MASK.format(table=table, column=column)
        try:
            response = self.execute_request(db, aim_request)
            values = [str(_v[0]) for _v in list(response)]
            return values
        except ValueError:
            print()
            print(f"Problem with {column} in {table} (db = {db}). Request: {aim_request}")
            return []

    def get_db_tables(self, db):
        return self.tables[db]

    def get_db_columns(self, db, table):
        return self.columns[db][table]

    def show_table(self, db, table):
        values_request = f"SELECT * FROM {table}"
        values = self.execute_request(db, values_request)
        column_names = tuple(self.get_db_columns(db, table))
        return column_names, values


class EnSpiderDB(SpiderDB):
    def __init__(self):
        super().__init__()
        self.db_path = "datasets/spider/database"
        self.schemes_path = "datasets/spider/tables.json"

    def get_dbs(self):
        pass

    def get_tables(self):
        pass

    def get_columns(self):
        pass


class RuSpiderDB(SpiderDB):
    def __init__(self):
        super().__init__()
        self.db_path = "datasets/russocampus/merged_database"

    def get_dbs(self):
        pass

    def get_tables(self):
        pass

    def get_columns(self):
        pass