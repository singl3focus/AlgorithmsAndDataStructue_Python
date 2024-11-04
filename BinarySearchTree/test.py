import unittest
from main import BinarySearchTree, Student


class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

        self.students = [
            Student("Павел", "4314", 1, 20, 4.5),
            Student("Герман", "4314", 1, 21, 3.2),
            Student("Никита", "4314", 2, 22, 3.8),
            Student("Диана", "4314", 2, 23, 4.0),
            Student("Александр", "4314", 3, 24, 2.5)
        ]
        for student in self.students:
            self.bst.insert(student)

    def test_find(self):
        found_student = self.bst.find(4.0)
        self.assertIsNotNone(found_student)
        self.assertEqual(found_student.full_name, "Диана")

    def test_find_non_existent(self):
        found_student = self.bst.find(5.0)
        self.assertIsNone(found_student)

    def test_contains(self):
        self.assertTrue(self.bst.contains(3.2))
        self.assertTrue(self.bst.contains(4.5))
        self.assertFalse(self.bst.contains(5.0))

    def test_contains_iterative(self):
        self.assertTrue(self.bst.contains_iterative(3.8))
        self.assertTrue(self.bst.contains_iterative(2.5))
        self.assertFalse(self.bst.contains_iterative(4.2))


if __name__ == "__main__":
    unittest.main()
