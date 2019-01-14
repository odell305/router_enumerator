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

        self.full_name = None

    def enumerate_from_source(self, source: str) -> str:
        # Todo
        pass

    def open_router_page(self, url: str):
        pass
        driver.get(url)

    def get_manufacturers(self) -> Iterable[set]:
        query = 'SELECT manufacturer FROM routers'
        manufacturers = {m[0] for m in self.db_cursor.execute(query)}
        return manufacturers
