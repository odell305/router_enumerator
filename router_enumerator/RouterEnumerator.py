from selenium import webdriver
from pathlib import Path

driver = webdriver.Firefox()


class RouterEnumerator:

    def __init__(self, routers_db: Path):
        self.routers_db = routers_db
        assert self.routers_db.is_file()

        self.full_name = None

    def enumerate_from_source(self, source: str) -> str:
        # Todo
        pass

    def open_router_page(self, url: str):
        driver.get(url)
