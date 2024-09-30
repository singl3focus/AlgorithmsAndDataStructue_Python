import unittest
from main import HashedTable


class TestHashedTable(unittest.TestCase):
    def setUp(self):
        self.ht = HashedTable(size=20)

    def test_set(self):
        self.ht.set("1", 1)
        self.ht.set("2", 2)
        self.assertEqual(self.ht.get("1"), (1, True))
        self.assertEqual(self.ht.get("2"), (2, True))

    def test_delete(self):
        self.ht.set("2", 2)
        self.assertEqual(self.ht.get("2"), (2, True))

        self.assertEqual(self.ht.delete("2"), True)
        self.assertEqual(self.ht.get("2"), (None, False))

    def test_contains(self):
        self.ht.set("1", 1)
        self.ht.set("2", 2)
        self.assertEqual(self.ht.contains_with_index("1"), True)
        self.assertEqual(self.ht.contains_with_enumeration("2"), True)


if __name__ == '__main__':
    unittest.main()
