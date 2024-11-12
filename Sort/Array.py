from typing import List
from Book import Book


class OutOfRange(Exception):
    pass


class Array:
    def __init__(self, capacity: int = 10) -> None:
        self._len: int = 0
        self._capacity: int = 10
        self.elems: List[Book] = []

    def get_length(self) -> int:
        return self._len

    def get_capacity(self) -> int:
        return self._capacity

    def append(self, elem: Book) -> None:
        if self._len < self._capacity:
            self.elems.append(elem)
            self._len += 1
        else:
            raise OutOfRange("Массив переполнен")

    def __str__(self) -> str:
        elements = []
        for _, book in enumerate(self.elems):
            elements.append(f'[{book.price},{book.ISBN}]')
        return " ".join(elements)

    # quick_desc_sort: Быстрая сортировка (по убыванию) по полю «стоимость»
    def quick_desc_sort(self):
        self.elems = self.__quick_desc_sort(self.elems)

    def __quick_desc_sort(self, arr: List[Book]) -> List[Book]:
        if len(arr) <= 1:
            return arr
        pivot: Book = arr[len(arr) // 2]
        left: List[Book] = [x for x in arr if x.price < pivot.price]
        middle: List[Book] = [x for x in arr if x.price == pivot.price]
        right: List[Book] = [x for x in arr if x.price > pivot.price]

        return self.__quick_desc_sort(right) + middle + self.__quick_desc_sort(left)


if __name__ == '__main__':
    array = Array()
    for i in range(1, 11):
        array.append(Book(price=i*10, ISBN="a"))

    print(array)

    array.quick_desc_sort()

    print(array)

