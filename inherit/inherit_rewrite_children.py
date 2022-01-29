class Master():
    def __init__(self):
        self.skill = "[old methods]"
    
    def make_cake(self):
        print("use {} to make egg cake".format(self.skill))
        
class School():
    def __init__(self):
        self.skill = "[new methods]"
        
    def make_cake(self):
        print("use {} to make egg cake".format(self.skill))

# inherit the first one here, School is the first one, so inherit School   
class Prentice(School, Master):
    def __init__(self):
        self.skill = "[unique method]"
        
    def make_cake(self):
        print("use {} to make egg cake".format(self.skill))

moyu = Prentice()
print(moyu.skill)
moyu.make_cake()