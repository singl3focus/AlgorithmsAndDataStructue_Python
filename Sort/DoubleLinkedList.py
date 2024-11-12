from typing import Optional
from Car import Car


class IndexOutOfRange(Exception):
    pass


class DoublyNode:
    def __init__(self,
                 data: Car,
                 nxt: Optional['DoublyNode'] = None,
                 prev: Optional['DoublyNode'] = None) -> None:
        self.data = data
        self.next: Optional[DoublyNode] = nxt
        self.prev: Optional[DoublyNode] = prev


class DoublyLinkedList:
    def __init__(self) -> None:
        self._len: int = 0
        self._head: Optional[DoublyNode] = None
        self._tail: Optional[DoublyNode] = None

    def get_length(self) -> int:
        return self._len

    def _check_range(self, index: int) -> bool:
        if index < 0 or index >= self._len:
            return False
        return True

    def push_tail(self, elem: Car) -> None:
        node = DoublyNode(elem)
        if self._len == 0:
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

        self._len += 1

    def __contains__(self, elem: Car) -> bool:
        curr = self._head
        while curr:
            if curr.data == elem:
                return True
            curr = curr.next
        return False

    def contains(self, elem: Car) -> bool:
        return self.__contains__(elem)

    def __str__(self) -> str:
        elements = []
        curr = self._head
        while curr:
            elements.append(f'[{curr.data.speed},{curr.data.VIN}]')
            curr = curr.next
        return " < -- > ".join(elements)

    def get(self, index: int) -> Car:
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

    # bubble_desc_sort: Сортировка пузырьком (по убыванию) по полю «средняя скорость».
    def bubble_desc_sort(self):
        length = self.get_length()
        if length <= 1:
            return

        for i in range(length):
            curr = self._head
            for j in range(0, length - i - 1):
                first = curr
                second = first.next

                if second.data.speed > first.data.speed:
                    # Сохраняем состояние крайних элементов узлов пары
                    first_prev = first.prev
                    second_next = second.next

                    # Обновляем prev и next для first
                    if first_prev:
                        first_prev.next = second
                    first.prev = second
                    first.next = second_next

                    # Обновляем prev и next для second
                    if second_next:
                        second_next.prev = first
                    second.prev = first_prev
                    second.next = first

                    # Если first был головой списка, обновляем _head
                    if first == self._head:
                        self._head = second
                    # Если second был хвостом, обновляем _tail
                    if second == self._tail:
                        self._tail = first

                    curr = first
                else:
                    curr = second

    def __sorted_insert(self, new_node):
        if not self._head or self._head.data.VIN > new_node.data.VIN:
            new_node.next = self._head
            if self._head:
                self._head.prev = new_node
            self._head = new_node
            return

        current = self._head
        while current.next and current.next.data.VIN <= new_node.data.VIN:
            current = current.next

        new_node.next = current.next
        new_node.prev = current
        current.next = new_node
        if new_node.next:
            new_node.next.prev = new_node

    # inserting_sort: быстрой сортировки вставками (по возрастанию) по полю «VIN».
    def insertion_sort(self):
        if self.get_length() <= 1:
            return

        current = self._head
        while current:
            temp = current.next

            if current.prev:
                current.prev.next = current.next
            if current.next:
                current.next.prev = current.prev # head??
                if current == self._head:
                    self._head = current.next

            current.prev = None
            current.next = None

            self.__sorted_insert(current)

            current = temp


if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.push_tail(Car(vin=4, speed=50))
    dll.push_tail(Car(vin=2, speed=20))
    dll.push_tail(Car(vin=3, speed=30))
    dll.push_tail(Car(vin=1, speed=40))
    dll.push_tail(Car(vin=5, speed=60))

    dll.insertion_sort()
    print(dll)
    dll.bubble_desc_sort()
    print(dll)