from random import randint

list1 = [randint(-10, 10) for x in range(20)]
print(list1)

filter1 = [x for x in set(list1) if x % 3 == 0]
print(filter1)