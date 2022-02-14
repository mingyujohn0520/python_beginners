class Student():
    def __init__(self, name, gender, mobile):
        self.name = name
        self.gender = gender
        self.mobile = mobile

    def __str__(self):
        return "{}, {}, {}".format(self.name, self.gender, self.mobile)

aa = Student("aa", "female", 33)
print(aa)