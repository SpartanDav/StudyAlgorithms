# Задание 1:

random_array_one = [53, 78, 3, 2, 103, 91, 97, 35, 80, 44]
sort_array_one = []

for i in range(len(random_array_one)):
    maxItem = random_array_one[0]
    maxItemNumber = 0
    for j in range(len(random_array_one)):
        k = random_array_one[j]
        if k < maxItem or k == maxItem:
            maxItem = k
            maxItemNumber = j
    del random_array_one[maxItemNumber]
    sort_array_one.append(maxItem)

print("Задание_1:")
print(sort_array_one)
print()


# Задание 2:

random_array_two = [73, 8, 0, 66, 39, 12, 100, 92, 37, 50]
sort_array_two = []

for i in range(len(random_array_two)):
    maxItem = random_array_two[0]
    maxItemNumber = 0
    for j in range(len(random_array_two)):
        k = random_array_two[j]
        if k > maxItem or k == maxItem:
            maxItem = k
            maxItemNumber = j
    del random_array_two[maxItemNumber]
    sort_array_two.append(maxItem)

print("Задание_2:")
print(sort_array_two)
print()


# Задание 3:

random_array_three = [
    "23-45-67",
    "43-29-10",
    "01-40-99",
    "20-20-19",
    "00-78-34",
    "85-39-08",
    "20-20-76",
    "73-82-10",
    "40-28-19",
    "10-02-04",
]
sort_array_three = []

for i in range(len(random_array_three)):
    maxItem = random_array_three[0]
    maxItemNumber = 0
    for j in range(len(random_array_three)):
        k = int(random_array_three[j].replace("-", ""))
        if k < int(maxItem.replace("-", "")) or k == int(maxItem.replace("-", "")):
            maxItem = random_array_three[j]
            maxItemNumber = j
    del random_array_three[maxItemNumber]
    sort_array_three.append(maxItem)

print("Задание_3:")
print(sort_array_three)
print()
