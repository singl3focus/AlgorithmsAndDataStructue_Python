import pickle
from typing import Optional


class EmptyNodeException(Exception):
    pass


class EmptyTreeException(Exception):
    pass


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

    def key(self) -> float:
        return self.average_grade

    def __repr__(self) -> str:
        return f"Student({self.full_name}, {self.group_number}, {self.course}, {self.age}, {self.average_grade})"


class AVLNode:
    def __init__(self, student: Student):
        self.student: Student = student
        self.height: int = 1
        self.left: Optional[AVLNode] = None
        self.right: Optional[AVLNode] = None

    def key(self) -> float:
        return self.student.key()


class AVLTree:
    def __init__(self):
        self._length: int = 0
        self._root: Optional[AVLNode] = None

    def is_empty(self) -> bool:
        return self._length == 0

    def get_size(self) -> int:
        return self._length

    def __height(self, p: Optional[AVLNode]) -> int:
        if p is None:
            return 0
        return p.height

    def __bfactor(self, p: Optional[AVLNode]) -> int:
        return self.__height(p.right) - self.__height(p.left)

    def __update_height(self,  p: Optional[AVLNode]) -> None:
        if p is None:
            raise EmptyNodeException("Empty node")

        hl = self.__height(p.left)
        hr = self.__height(p.right)

        if hl > hr:
            p.height = hl + 1
        else:
            p.height = hr + 1

    def __rotate_right(self, p: AVLNode) -> AVLNode:
        if p is None:
            return p

        q = p.left
        p.left = q.right
        q.right = p
        self.__update_height(p)
        self.__update_height(q)
        return q

    def __rotate_left(self, p: AVLNode) -> AVLNode:
        if p is None:
            return p

        q = p.right
        p.right = q.left
        q.left = p
        self.__update_height(p)
        self.__update_height(q)
        return q

    def __balance(self, p: AVLNode) -> AVLNode:
        self.__update_height(p)
        if self.__bfactor(p) >= 2:
            if self.__bfactor(p.right) < 0:
                p.right = self.__rotate_right(p.right)
            return self.__rotate_left(p)
        if self.__bfactor(p) <= -2:
            if self.__bfactor(p.left) < 0:
                p.right = self.__rotate_left(p.left)
            return self.__rotate_right(p)
        return p

    def insert(self, value: Student) -> None:
        self._root = self.__insert(self._root, value)
        self._length += 1

    def __insert(self, p: Optional[AVLNode], value: Student) -> AVLNode:
        if p is None:
            return AVLNode(student=value)
        if value.key() < p.key():
            p.left = self.__insert(p.left, value)
        else:
            p.right = self.__insert(p.right, value)
        return self.__balance(p)

    def find(self, key: float) -> tuple[Optional[Student], bool]:
        if self.get_size() == 0:
            raise EmptyTreeException("Empty tree")

        curr = self._root
        while curr.key() != key:
            if curr is None:
                return None, False
            if key < curr.key():
                curr = curr.left
            else:
                curr = curr.right
        return curr.student, True

    def save_to_file(self, filename: str) -> None:
        with open(filename, 'wb') as f:
            pickle.dump(self._root, f)

    def load_from_file(self, filename: str) -> None:
        with open(filename, 'rb') as f:
            self._root = pickle.load(f)
