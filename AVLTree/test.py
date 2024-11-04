import unittest
from main import AVLTree, Student, EmptyTreeException


class TestAVLTree(unittest.TestCase):

    def setUp(self):
        self.tree = AVLTree()

    def test_insert_and_find(self):
        student1 = Student("Андрей", "4314", 1, 20, 3.5)
        student2 = Student("Дмитрий", "4314", 1, 21, 4.0)
        student3 = Student("Николай", "4314", 2, 22, 3.2)

        self.tree.insert(student1)
        self.tree.insert(student2)
        self.tree.insert(student3)

        found_student, found = self.tree.find(student1.key())  # OK
        self.assertTrue(found)
        self.assertEqual(found_student.full_name, student1.full_name)

        found_student, found = self.tree.find(student2.key())  # OK
        self.assertTrue(found)
        self.assertEqual(found_student.full_name, student2.full_name)

        found_student, found = self.tree.find(student3.key())  # OK
        self.assertTrue(found)
        self.assertEqual(found_student.full_name, student3.full_name)


    def test_empty_tree(self):
        with self.assertRaises(EmptyTreeException):
            self.tree.find(3.5)

    def test_size_after_insertion(self):
        self.assertEqual(self.tree.get_size(), 0)

        student1 = Student("Андрей", "4314", 1, 20, 3.5)
        self.tree.insert(student1)
        self.assertEqual(self.tree.get_size(), 1)

        student2 = Student("Дмитрий", "4314", 1, 21, 4.0)
        self.tree.insert(student2)
        self.assertEqual(self.tree.get_size(), 2)

    def test_insert_duplicates(self):
        student1 = Student("Андрей", "4314", 1, 20, 3.5)
        self.tree.insert(student1)
        self.tree.insert(student1)
        self.assertEqual(self.tree.get_size(), 1)


if __name__ == '__main__':
    unittest.main()
