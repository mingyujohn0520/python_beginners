from functools import reduce
from random import randint, sample

# random pick 3 to 6 samples
sample("abcdefg", randint(3, 6))

# make it as a dictionary
s1 = {x: randint(1, 4) for x in sample("abcdefg", randint(3, 6))}

s2 = {x: randint(1, 4) for x in sample("abcdefg", randint(3, 6))}

s3 = {x: randint(1, 4) for x in sample("abcdefg", randint(3, 6))}

# find the public key method 1
list1 = []
for k in s1:
    if k in s1:
        if k in s2 and k in s3:
            list1.append(k)
print(list1)

# find the public key method 2
print(s1.keys() & s2.keys() & s3.keys())

# find the public key method 3, use map reduce
print(reduce(lambda a, b: a & b, map(dict.keys, [s1, s2, s3])))