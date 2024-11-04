import time
import random
from main import BinarySearchTree, Student


class BinarySearchTreeBenchmarks:
    def __init__(self, num_students: int = 1000):
        self.num_students = num_students
        self.bst = BinarySearchTree()
        self.students = self._generate_students()

    def _generate_students(self):
        students = []
        for i in range(self.num_students):
            full_name = f"Student {i+1}"
            group_number = f"Group {random.randint(1, 10)}"
            course = random.randint(1, 5)
            age = random.randint(18, 25)
            average_grade = random.uniform(2.0, 5.0)
            students.append(Student(full_name, group_number, course, age, average_grade))
        return students

    def benchmark_insertion(self):
        start_time = time.time()
        for student in self.students:
            self.bst.insert(student)
        end_time = time.time()
        return end_time - start_time

    def benchmark_find(self, average_grade: float):
        start_time = time.time()
        self.bst.find(average_grade)
        end_time = time.time()
        return end_time - start_time

    def run_benchmarks(self):
        insertion_time = self.benchmark_insertion()
        print(f"Insertion time for {self.num_students} students: {insertion_time:.5f} seconds")

        random_student = self.students[random.randint(0, self.num_students - 1)]
        find_time = self.benchmark_find(random_student.average_grade)
        print(f"Find time for average_grade {random_student.average_grade:.2f}: {find_time:.5f} seconds")


if __name__ == "__main__":
    benchmark = BinarySearchTreeBenchmarks(num_students=1000)
    benchmark.run_benchmarks()
