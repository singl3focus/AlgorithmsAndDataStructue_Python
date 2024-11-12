import unittest

from DoubleLinkedList import DoublyLinkedList
from Array import Array
from Car import Car
from Book import Book


class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.dll = DoublyLinkedList()
        self.array = Array(capacity=5)

    def test_bubble_desc_sort(self):
        for i in range(1, 6):
            self.dll.push_tail(Car(vin=100, speed=i*1))

        self.assertEqual(str(self.dll), "[1,100] < -- > [2,100] < -- > [3,100] < -- > [4,100] < -- > [5,100]")
        self.assertEqual(self.dll.get_length(), 5)

        self.dll.bubble_desc_sort()
        self.assertEqual(str(self.dll), "[5,100] < -- > [4,100] < -- > [3,100] < -- > [2,100] < -- > [1,100]")
        self.assertEqual(self.dll.get_length(), 5)

    def test_insertion_sort(self):
        for i in range(5, 0, -1):
            self.dll.push_tail(Car(vin=i * 1, speed=250))

        self.assertEqual(str(self.dll), "[250,5] < -- > [250,4] < -- > [250,3] < -- > [250,2] < -- > [250,1]")
        self.assertEqual(self.dll.get_length(), 5)

        self.dll.insertion_sort()
        self.assertEqual(str(self.dll), "[250,1] < -- > [250,2] < -- > [250,3] < -- > [250,4] < -- > [250,5]")
        self.assertEqual(self.dll.get_length(), 5)

    def test_quick_desc_sort(self):
        for i in range(1, 6):
            self.array.append(Book(price=i*5, ISBN="a"))

        self.assertEqual(str(self.array), "[5,a] [10,a] [15,a] [20,a] [25,a]")
        self.assertEqual(self.array.get_length(), 5)

        self.array.quick_desc_sort()
        self.assertEqual(str(self.array), "[25,a] [20,a] [15,a] [10,a] [5,a]")
        self.assertEqual(self.array.get_length(), 5)


if __name__ == '__main__':
    unittest.main()
