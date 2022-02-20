from random import randint

dic1 = {x: randint(50, 100) for x in range (1, 21)}
print(dic1)

dic2 = dict()
for (key, value) in dic1.items():
    if value >= 80:
        dic2[key] = value
print(dic2)