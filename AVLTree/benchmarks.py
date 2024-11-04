import timeit
import random
from main import AVLTree, Student


def create_students(num_students: int = 1000):
    students = []
    for i in range(num_students):
        student = Student(
            full_name=f"Student {i}",
            group_number=f"Group {random.randint(1, 10)}",
            course=random.randint(1, 5),
            age=random.randint(18, 25),
            average_grade=round(random.uniform(2.0, 5.0), 2)
        )
        students.append(student)
    return students


def benchmark_insert(num_students: int = 1000):
    tree = AVLTree()
    students = create_students(num_students)

    # Бенчмарк на вставку
    insert_time = timeit.timeit(
        stmt=lambda: [tree.insert(s) for s in students],
        number=1
    )
    return insert_time


def benchmark_find(num_students: int = 1000):
    tree = AVLTree()
    students = create_students(num_students)

    for student in students:
        tree.insert(student)

    find_time = timeit.timeit(
        stmt=lambda: [tree.find(s.average_grade) for s in students],
        number=1
    )
    return find_time


if __name__ == "__main__":
    num_students = 100
    insert_benchmark = benchmark_insert(num_students)
    find_benchmark = benchmark_find(num_students)

    print(f"Время вставки {num_students} студентов: {insert_benchmark:.6f} секунд")
    print(f"Время поиска {num_students} студентов: {find_benchmark:.6f} секунд")
