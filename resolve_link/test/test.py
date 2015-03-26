from unittest import TestCase
from resolve_link import resolve_link


class TestRunFunction(TestCase):
    def test_run_exists(self):
        self.assertTrue(bool(resolve_link.run))
