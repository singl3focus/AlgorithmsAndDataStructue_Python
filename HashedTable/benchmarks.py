import time
from main import HashedTable


class HashedTableBenchmarks:
    def __init__(self):
        self.ht = HashedTable(size=1000)

    def benchmark_set(self):
        elems: int = 1000
        start_time = time.perf_counter()
        for i in range(elems):
            self.ht.set(i, i+1)
        end_time = time.perf_counter()
        print(f"Time taken to set {elems} elements: {end_time - start_time:.6f} seconds")

    def benchmark_delete(self):
        elems: int = 1000

        for i in range(elems): #seeding
            self.ht.set(i, i+1)

        start_time = time.perf_counter()
        for i in range(elems):
            self.ht.delete(i)
        end_time = time.perf_counter()
        print(f"Time taken to delete {elems} elements: {end_time - start_time:.6f} seconds")

    def benchmark_contains(self):
        elems: int = 1000

        for i in range(elems):  # seeding
            self.ht.set(i, i + 1)

        start_time = time.perf_counter()
        for i in range(1000):
            self.ht.contains_with_index(i)
        end_time = time.perf_counter()
        print(f"Time taken to contains_with_index {elems} elements: {end_time - start_time:.6f} seconds")


if __name__ == '__main__':
    ht = HashedTableBenchmarks()
    ht.benchmark_set()
    ht.benchmark_delete()
    ht.benchmark_contains()
