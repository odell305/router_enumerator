import unittest
from router_enumerator.RouterEnumerator import RouterEnumerator
from pathlib import Path, PurePath
from selenium import webdriver

driver = webdriver.Firefox()

TEST_RESOURCES_DIR = Path('./test_resources/')
assert TEST_RESOURCES_DIR.is_dir()

ROUTERS_DB_PATH = Path('../resources/routers.db')
assert ROUTERS_DB_PATH.is_file()

TPLINK_ARCHER_C8_PAGE_FILE = PurePath.joinpath(TEST_RESOURCES_DIR, 'tplink_archer_c8_page')
assert TPLINK_ARCHER_C8_PAGE_FILE.is_file()
TPLINK_ARCHER_C8_HTML = TPLINK_ARCHER_C8_PAGE_FILE.read_text(encoding='UTF-8')


class TestRouterEnumerator(unittest.TestCase):

    def setUp(self):
        self.router_enumerator = RouterEnumerator(ROUTERS_DB_PATH)

    # This is a test for routers on this specific ip address
    # We assume that the title for the page is "Home"
    def test_192_168_1_254(self):
        router_enumerator = RouterEnumerator(ROUTERS_DB_PATH)
        expected_url = "http://192.168.1.254/"
        driver.get("http://192.168.1.254/")
        self.assertEquals(expected_url, "http://192.168.1.254/")

    # Not going to work without this router
    def test_tplink_archer_c8_html_returns_correct_name_when_enumerating_from_source(self):
        page_html = TPLINK_ARCHER_C8_HTML

        self.router_enumerator.enumerate_from_source(page_html)

        expected = 'TP-LINK Archer C8'
        actual = self.router_enumerator.full_name

        self.assertEqual(expected, actual)

