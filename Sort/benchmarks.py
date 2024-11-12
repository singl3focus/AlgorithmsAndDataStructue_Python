import time
from DoubleLinkedList import DoublyLinkedList


class DoublyLinkedListBenchmarks:
    def __init__(self):
        self.dll = DoublyLinkedList()

    def benchmark_push_tail(self):
        start_time = time.perf_counter()
        for i in range(1000):
            self.dll.push_tail(i)
        end_time = time.perf_counter()
        print(f"Time taken to push 1000 elements to tail: {end_time - start_time:.6f} seconds")

    def benchmark_push_head(self):
        start_time = time.perf_counter()
        for i in range(1000):
            self.dll.push_head(i)
        end_time = time.perf_counter()
        print(f"Time taken to push 1000 elements to head: {end_time - start_time:.6f} seconds")

    def benchmark_get(self):
        for i in range(1000):
            self.dll.push_tail(i)
        start_time = time.perf_counter()
        for i in range(1000):
            self.dll.get(i)
        end_time = time.perf_counter()
        print(f"Time taken to get 1000 elements: {end_time - start_time:.6f} seconds")

    def benchmark_remove(self):
        for i in range(1000):
            self.dll.push_tail(i)
        start_time = time.perf_counter()
        for i in range(1000):
            self.dll.remove(0)  # Всегда удаляем первый элемент
        end_time = time.perf_counter()
        print(f"Time taken to remove 1000 elements: {end_time - start_time:.6f} seconds")


if __name__ == '__main__':
    dll = DoublyLinkedListBenchmarks()
    dll.benchmark_remove()
    dll.benchmark_get()
    dll.benchmark_push_tail()
    dll.benchmark_push_head()
