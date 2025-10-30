import random

# Задание 1 --------------------------------------------------------------


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Опорный элемент (середина)
    left = [x for x in arr if x < pivot]  # Элементы меньше опорного
    middle = [x for x in arr if x == pivot]  # Элементы равные опорному
    right = [x for x in arr if x > pivot]  # Элементы больше опорного

    return quick_sort(left) + middle + quick_sort(right)


data = [random.randint(1, 10000) for _ in range(1000)]

sorted_data = quick_sort(data)

print(sorted_data)
print()


# Задание 2 --------------------------------------------------------------

data = [random.randint(50, 100) for _ in range(50)]
sorted_data = quick_sort(data)
print(sorted_data)
print()


# Задание 3 --------------------------------------------------------------


def sort_first_column(matrix):
    first_column = [row[0] for row in matrix]  # Извлечение первого столбца
    sorted_column = quick_sort(first_column)
    for i in range(len(matrix)):
        matrix[i][0] = sorted_column[i]  # Замена первого столбца отсортированным


rows = 10
cols = 5
matrix = [[random.randint(5, 61) for _ in range(cols)] for _ in range(rows)]

sort_first_column(matrix)

for row in matrix:
    print(row)

print()


# Задание 4 --------------------------------------------------------------

students = [
    "Шермати Азизджон Акрамджон",
    "Филиппова Вероника Игоревна",
    "Гончаренко Глеб Вячеславович",
    "Григорьев Егор Викторович",
    "Дешко Александр Николаевич",
    "Сенякина Варвара Владимировна",
    "Евтеев Матвей Витальевич",
    "Иванов Алексей Владимирович",
    "Игнатьева Лидия Григорьевна",
    "Киселева София Алексеевна",
    "Котов Владимир Петрович",
    "Летникова Мария Алексеевна",
    "Митяев Павел Сергеевич",
    "Максимов Дмитрий Александрович",
    "Мелентьев Давид Леонидович",
    "Акользин Павел Юрьевич",
    "Нюнин Савва Александрович",
    "Журавлев Серафим Владимирович",
    "Славин Давид Львович",
    "Чистяков Тимофей Сергеевич",
    "Поддубко Тимофей Сергеевич",
]

sorted_students = sorted(students)

print("Отсортированный список студентов:")
for student in sorted_students:
    print(student)
