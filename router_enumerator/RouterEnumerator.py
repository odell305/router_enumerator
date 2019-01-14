from selenium import webdriver
from pathlib import Path
import sqlite3
from typing import Iterable

driver = webdriver.Firefox()


class RouterEnumerator:
    def __init__(self, routers_db: Path):
        self.routers_db = routers_db
        assert self.routers_db.is_file()

        self.db_conn = sqlite3.connect(self.routers_db.as_posix())
        self.db_cursor = self.db_conn.cursor()

        self.manufacturer = None
        self.model = None
        self.full_name = None

    def enumerate_from_string(self, source: str):
        self.enumerate_manufacturer(source)
        self.enumerate_model(source)
        self.full_name = f'{self.manufacturer} {self.model}'

    def enumerate_manufacturer(self, source):
        manufacturers = self.get_manufacturers()
        for mfr in manufacturers:
            mfr = str(mfr).lower()

            if mfr in source.lower():
                self.manufacturer = mfr
                break

    def enumerate_model(self, source):
        models = self.get_models(self.manufacturer)
        for m in models:
            m = str(m).lower()

            if m in source.lower():
                self.model = m
                break

    def open_router_page(self, url: str):
        pass
        driver.get(url)

    def get_manufacturers(self) -> Iterable[set]:
        query = 'SELECT manufacturer FROM routers'
        manufacturers = {m[0] for m in self.db_cursor.execute(query)}
        return manufacturers

    def get_models(self, manufacturer) -> Iterable[set]:
        query = f'SELECT model FROM routers WHERE manufacturer == "{manufacturer}"'
        models = {m[0] for m in self.db_cursor.execute(query)}
        return models
