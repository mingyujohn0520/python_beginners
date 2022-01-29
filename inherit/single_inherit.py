class Master():
    def __init__(self):
        self.skill = "[old methods]"
    
    def make_cake(self):
        print("use {} to make egg cake".format(self.skill))
        
class Prentice(Master):
    pass

moyu = Prentice()
print(moyu.skill)
moyu.make_cake()