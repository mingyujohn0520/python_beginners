import re

log = open(r"C:\Users\mingy\Desktop\example\zxc.log").read()
print(log)

new_log = re.sub("(\d{4})-(\d{2})-(\d{2})", r"\2/\3/\1", log)
print(new_log)

new_log2 = re.sub("(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", r"\g<day>/\g<month>/\g<year>", log)
print(new_log2)
