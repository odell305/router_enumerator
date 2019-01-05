import unittest
from router_enumerator.RouterEnumerator import RouterEnumerator
from pathlib import Path, PurePath

TEST_RESOURCES_DIR = Path('./test_resources/')
assert TEST_RESOURCES_DIR.is_dir()

TPLINK_ARCHER_C8_PAGE_FILE = PurePath.joinpath(TEST_RESOURCES_DIR, 'tplink_archer_c8_page')
assert TPLINK_ARCHER_C8_PAGE_FILE.is_file()
TPLINK_ARCHER_C8_HTML = TPLINK_ARCHER_C8_PAGE_FILE.read_text(encoding='UTF-8')


class TestRouterEnumerator(unittest.TestCase):

    def test_instantiate_RouterEnumerator(self):
        router_enumerator = RouterEnumerator()

    def test_tplink_archer_c8_html_returns_correct_name_when_enumerating_from_source(self):
        page_html = TPLINK_ARCHER_C8_HTML

        router_enumerator = RouterEnumerator()
        router_enumerator.enumerate_from_source(page_html)

        expected = 'TP-LINK Archer C8'
        actual = router_enumerator.full_name

        self.assertEqual(expected, actual)

