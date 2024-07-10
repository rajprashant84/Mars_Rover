import unittest
from table_dimensions import TableDimensions


class TestTableDimensions(unittest.TestCase):
    def setUp(self):
        self.table = TableDimensions()

    def test_is_on_table_valid(self):
        self.assertTrue(self.table.is_on_table(0, 0))
        self.assertTrue(self.table.is_on_table(4, 4))

    def test_is_on_table_invalid(self):
        self.assertFalse(self.table.is_on_table(-1, 0))
        self.assertFalse(self.table.is_on_table(0, -1))
        self.assertFalse(self.table.is_on_table(5, 0))
        self.assertFalse(self.table.is_on_table(0, 5))

if __name__ == "__main__":
    unittest.main()
