import unittest
from router_enumerator.RouterEnumerator import RouterEnumerator
from pathlib import Path, PurePath
from selenium import webdriver

driver = webdriver.Firefox()

TEST_RESOURCES_DIR = Path('./test_resources/')
assert TEST_RESOURCES_DIR.is_dir()

ROUTERS_DB_PATH = Path('../resources/routers.db')
assert ROUTERS_DB_PATH.is_file()

ARRIS_NVG5689 = PurePath.joinpath(TEST_RESOURCES_DIR, 'Arris_NVG589.html')
assert ARRIS_NVG5689.is_file()
ARRIS_NVG589_HTML = ARRIS_NVG5689.read_text(encoding='UTF-8')


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

    def test_arris_nvg589_html_returns_correct_name_when_enumerating_from_source(self):
        page_html = ARRIS_NVG589_HTML

        self.router_enumerator.enumerate_from_source(page_html)

        expected = 'arris nvg589'
        actual = self.router_enumerator.full_name

        self.assertEqual(expected, actual)

