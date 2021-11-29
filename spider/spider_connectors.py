import json
import collections
import sqlite3
import os
from typing import *

REQUEST_MASK = "SELECT \"{column}\" FROM \"{table}\""
TABLES_REQUEST = f"SELECT name FROM sqlite_master WHERE type='table'"

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
        self.__dbs: Union[List[str], None] = None
        self.__tables: Union[List[str], None] = None
        self.__columns: Union[List[str], None] = None

    def get_dbs(self) -> List[str]:
        pass

    def get_tables(self) -> List[str]:
        pass

    def get_columns(self) -> List[str]:
        pass

    @property
    def dbs(self) -> List[str]:
        if not self.__dbs:
            self.__dbs = self.get_dbs()
        return self.__dbs

    @property
    def tables(self) -> List[str]:
        if not self.__tables:
            self.__tables = self.get_tables()
        return self.__tables

    @property
    def columns(self) -> List[str]:
        if not self.__columns:
            self.__columns = self.get_columns()
        return self.__columns

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
        return os.listdir(self.db_path)

    def get_tables(self):
        with open(self.schemes_path) as table_file:
            schemes = json.load(table_file)
        extracted_tables = {_s['db_id']: _s['table_names_original'] for _s in schemes}
        return extracted_tables

    def get_columns(self):
        with open(self.schemes_path) as table_file:
            schemes = json.load(table_file)
        columns = {
            _s['db_id']: {
                _table: [] for _table in _s['table_names_original']
            } for _s in schemes
        }
        for _scheme in schemes:
            db_id = _scheme['db_id']
            table_names = _scheme['table_names_original']
            for _column in _scheme["column_names_original"]:
                column_name = _column[1]
                table_name = table_names[_column[0]]
                if column_name == '*':
                    continue
                columns[db_id][table_name].append(column_name)
        return columns


class RuSpiderDB(SpiderDB):
    def __init__(self):
        super().__init__()
        self.db_path = "datasets/russocampus/merged_database"

    def get_dbs(self):
        return os.listdir(self.db_path)

    def get_tables(self):
        tables = {}
        for _db in self.dbs:
            extracted_tables = self.execute_request(_db, TABLES_REQUEST)
            tables[_db] = [_t[0] for _t in extracted_tables]

    def get_columns(self):
        columns = {}
        COLUMNS_REQUEST = "PRAGMA table_info({:s});"
        for _db in self.dbs:
            columns[_db] = {}
            for _table in self.tables[_db]:
                extracted_columns = self.execute_request(_db, COLUMNS_REQUEST.format(_table))
                columns[_db][_table] = [_c[1] for _c in extracted_columns]