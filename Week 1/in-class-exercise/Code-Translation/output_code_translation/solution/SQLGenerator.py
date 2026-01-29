from typing import List, Dict


class SQLGenerator:
    def __init__(self, table_name: str):
        self.table_name = table_name

    def select(self, fields: List[str] = None, condition: str = "") -> str:
        if fields is None:
            fields = []
        fields_str = "*"
        if fields:
            fields_str = ", ".join(fields)
        sql = f"SELECT {fields_str} FROM {self.table_name}"
        if condition:
            sql += f" WHERE {condition}"
        return sql + ";"

    def insert(self, data: Dict[str, str]) -> str:
        fields = ", ".join(data.keys())
        values = ", ".join(f"'{v}'" for v in data.values())
        sql = f"INSERT INTO {self.table_name} ({fields}) VALUES ({values})"
        return sql + ";"

    def update(self, data: Dict[str, str], condition: str) -> str:
        set_clause = ", ".join(f"{k} = '{v}'" for k, v in data.items())
        sql = f"UPDATE {self.table_name} SET {set_clause}"
        if condition:
            sql += f" WHERE {condition}"
        return sql + ";"

    def delete_query(self, condition: str) -> str:
        sql = f"DELETE FROM {self.table_name}"
        if condition:
            sql += f" WHERE {condition}"
        return sql + ";"

    def select_female_under_age(self, age: int) -> str:
        condition = f"age < {age} AND gender = 'female'"
        return self.select([], condition)

    def select_by_age_range(self, min_age: int, max_age: int) -> str:
        condition = f"age BETWEEN {min_age} AND {max_age}"
        return self.select([], condition)
