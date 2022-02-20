from random import randint
from collections import Counter

list1 = [randint(0, 20) for x in range(30)]
print(list1)

dict1 = Counter(list1)
print(dict1.most_common(3))