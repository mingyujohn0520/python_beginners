import re
from collections import Counter

txt = open("new.txt").read()
co = Counter(re.split("\W+", txt))
print(co.most_common(10))