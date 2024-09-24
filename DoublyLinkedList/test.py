import unittest
from main import DoublyLinkedList, IndexOutOfRange


class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.dll = DoublyLinkedList()

    def test_push_tail(self):
        self.dll.push_tail(1)
        self.assertEqual(self.dll.get_length(), 1)
        self.assertEqual(str(self.dll), "1")

        self.dll.push_tail(2)
        self.assertEqual(self.dll.get_length(), 2)
        self.assertEqual(str(self.dll), "1 < -- > 2")

    def test_push_head(self):
        self.dll.push_head(1)
        self.assertEqual(self.dll.get_length(), 1)
        self.assertEqual(str(self.dll), "1")

        self.dll.push_head(2)
        self.assertEqual(self.dll.get_length(), 2)
        self.assertEqual(str(self.dll), "2 < -- > 1")

    def test_contains(self):
        self.dll.push_tail(1)
        self.dll.push_tail(2)
        self.assertTrue(self.dll.contains(1))
        self.assertTrue(self.dll.contains(2))

        self.assertFalse(self.dll.contains(3))

    def test_get(self):
        self.dll.push_tail(1)
        self.dll.push_tail(2)
        self.dll.push_tail(3)
        self.assertEqual(self.dll.get(0), 1)
        self.assertEqual(self.dll.get(1), 2)
        self.assertEqual(self.dll.get(2), 3)

        with self.assertRaises(IndexOutOfRange):
            self.dll.get(3)
        with self.assertRaises(IndexOutOfRange):
            self.dll.get(-1)

    def test_remove(self):
        self.dll.push_tail(1)
        self.dll.push_tail(2)
        self.dll.push_tail(3)
        self.assertEqual(str(self.dll), "1 < -- > 2 < -- > 3")

        self.assertTrue(self.dll.remove(1))
        self.assertEqual(str(self.dll), "1 < -- > 3")
        self.assertEqual(self.dll.get_length(), 2)

        self.assertTrue(self.dll.remove(0))
        self.assertEqual(str(self.dll), "3")
        self.assertEqual(self.dll.get_length(), 1)

        self.assertTrue(self.dll.remove(0))
        self.assertEqual(self.dll.get_length(), 0)

        with self.assertRaises(IndexOutOfRange):
            self.dll.remove(0)

    def test_get_length(self):
        self.assertEqual(self.dll.get_length(), 0)

        self.dll.push_tail(1)
        self.assertEqual(self.dll.get_length(), 1)

        self.dll.push_head(2)
        self.assertEqual(self.dll.get_length(), 2)

    def test_shift(self):
        self.dll.push_tail(1)
        self.dll.push_tail(2)
        self.assertEqual(str(self.dll), "1 < -- > 2")

        self.dll.shift("right", 2)
        self.assertEqual(str(self.dll), "0 < -- > 0 < -- > 1 < -- > 2")
        self.dll.remove(0)
        self.dll.remove(0)
        self.dll.remove(0)
        self.dll.remove(0)

        self.dll.push_tail(1)
        self.dll.push_tail(2)
        self.assertEqual(str(self.dll), "1 < -- > 2")

        self.dll.shift("left", 2)
        self.assertEqual(str(self.dll), "1 < -- > 2 < -- > 0 < -- > 0")


if __name__ == '__main__':
    unittest.main()
