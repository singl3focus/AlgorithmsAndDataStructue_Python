import pickle
from typing import Optional


class Student:
    def __init__(self,
                 full_name: str,
                 group_number: str,
                 course: int,
                 age: int,
                 average_grade: float):
        self.full_name = full_name
        self.group_number = group_number
        self.course = course
        self.age = age
        self.average_grade = average_grade

    def __repr__(self) -> str:
        return f"Student({self.full_name}, {self.group_number}, {self.course}, {self.age}, {self.average_grade})"


class BSTNode:
    def __init__(self, student: Student):
        self.student = student
        self.left: Optional[BSTNode] = None
        self.right: Optional[BSTNode] = None


class BinarySearchTree:
    def __init__(self):
        self.root: Optional[BSTNode] = None

    def __repr__(self) -> str:
        return self._repr_helper(self.root, 0)

    def _repr_helper(self, node: Optional[BSTNode], level: int) -> str:
        if node is None:
            return ""
        result = "  " * level + repr(node.student) + "\n"
        result += self._repr_helper(node.left, level + 1)
        result += self._repr_helper(node.right, level + 1)
        return result

    def insert(self, student: Student) -> None:
        if self.root is None:
            self.root = BSTNode(student)
        else:
            self._insert_recursive(self.root, student)

    def _insert_recursive(self, node: BSTNode, student: Student) -> None:
        if student.average_grade < node.student.average_grade:
            if node.left is None:
                node.left = BSTNode(student)
            else:
                self._insert_recursive(node.left, student)
        else:
            if node.right is None:
                node.right = BSTNode(student)
            else:
                self._insert_recursive(node.right, student)

    def find(self, average_grade: float) -> Optional[Student]:
        return self._find_recursive(self.root, average_grade)

    def _find_recursive(self, node: Optional[BSTNode], average_grade: float) -> Optional[Student]:
        if node is None:
            return None
        if node.student.average_grade == average_grade:
            return node.student
        if average_grade < node.student.average_grade:
            return self._find_recursive(node.left, average_grade)
        else:
            return self._find_recursive(node.right, average_grade)

    def contains(self, average_grade: float) -> bool:
        return self.find(average_grade) is not None

    def contains_iterative(self, average_grade: float) -> bool:
        current = self.root
        while current is not None:
            if current.student.average_grade == average_grade:
                return True
            elif average_grade < current.student.average_grade:
                current = current.left
            else:
                current = current.right
        return False

    def save_to_file(self, filename: str) -> None:
        with open(filename, 'wb') as f:
            pickle.dump(self.root, f)

    def load_from_file(self, filename: str) -> None:
        with open(filename, 'rb') as f:
            self.root = pickle.load(f)