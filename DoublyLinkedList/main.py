from typing import TypeVar, Generic, Optional

T = TypeVar("T")  # Вводим тип T, обобщающий все типы


class IndexOutOfRange(Exception):
    pass


class IncorrectShiftParam(Exception):
    pass


'''
TypeVar - позволяет определить параметр типа,
    который может быть подставлен позже при использовании Generic

Generic - Этот класс используется для создания обобщенных классов,
    которые могут работать с различными типами данных.
    Он требует параметр класса TypeVar

Optional - Опциональный тип указывает, что значение может быть None

Callable - Функциональный тип используется для определения функции или метода,
    который может принимать любые параметры и возвращать любое значение
'''

# ____________________________________________ #


class DoublyNode(Generic[T]):
    def __init__(self,
                 data: T,
                 next: Optional['DoublyNode[T]'] = None,
                 prev: Optional['DoublyNode[T]'] = None) -> None:
        self.data = data
        self.next: Optional['DoublyNode[T]'] = next
        self.prev: Optional['DoublyNode[T]'] = prev


class DoublyLinkedList(Generic[T]):
    def __init__(self) -> None:
        self._len: int = 0
        self._head: Optional['DoublyNode[T]'] = None
        self._tail: Optional['DoublyNode[T]'] = None

    def get_length(self) -> int:
        return self._len

    def _check_range(self, index: int) -> bool:
        if index < 0 or index >= self._len:
            return False
        return True

    def push_tail(self, elem: T) -> None:
        node = DoublyNode[T](elem, None)
        if self._len == 0:
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

        self._len += 1

    def push_head(self, elem: T) -> None:
        node = DoublyNode[T](elem, None)
        if self._len == 0:
            self._head = node
            self._tail = node
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node

        self._len += 1

    def __contains__(self, elem: T) -> bool:
        curr = self._head
        while curr:
            if curr.data == elem:
                return True
            curr = curr.next
        return False

    def contains(self, elem: T) -> bool:
        return self.__contains__(elem)

    def __str__(self) -> str:
        elements = []
        curr = self._head
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        return " < -- > ".join(elements)

    def get(self, index: int) -> T:
        if not self._check_range(index):
            raise IndexOutOfRange()

        if index == 0:
            return self._head.data
        elif index == self._len - 1:
            return self._tail.data

        node = self._head
        for i in range(0, index):
            node = node.next
        return node.data

    def remove(self, index: int) -> bool:
        if not self._check_range(index):
            raise IndexOutOfRange()

        if index == 0:
            self._head = self._head.next  # Can be 'None'
            if self._len == 1:  # 'self._head' is none
                pass
            else:
                self._head.prev = None

        elif index == self._len - 1:
            self._tail = self._tail.prev
            self._tail.next = None

        else:
            node = self._head
            for _ in range(0, index):
                node = node.next

            node.next.prev = node.prev
            node.prev.next = node.next

        self._len -= 1
        return True

    def shift(self, direct: str, n: int) -> None:
        if n < 0:
            raise IncorrectShiftParam("Offset param must be more 0")
        elif n == 0:
            raise IncorrectShiftParam("Offset is empty")

        empty_element = 0
        match direct:
            case "right":
                for _ in range(0, n):
                    self.push_head(empty_element)
            case "left":
                for _ in range(0, n):
                    self.push_tail(empty_element)
            case _:
                raise IncorrectShiftParam("Avaliable direct: right/left")

