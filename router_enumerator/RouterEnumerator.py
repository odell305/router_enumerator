from selenium import webdriver

driver = webdriver.Firefox()

class RouterEnumerator:

    def __init__(self):
        self.full_name = None

    def enumerate_from_source(self, source: str) -> str:
        # Todo
        pass

    def open_router_page(self, url: str):
        driver.get(url)