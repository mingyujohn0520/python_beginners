class Master():
    def __init__(self):
        self.skill = "[old methods]"
    
    def make_cake(self):
        print("use {} to make egg cake".format(self.skill))
        
class School(Master):
    def __init__(self):
        self.skill = "[new methods]"
        
    def make_cake(self):
        print("use {} to make egg cake".format(self.skill))

        # must have a indentation here
        # super(School, self).__init__()
        # super(School, self).make_cake()
        
        super().__init__()
        super().make_cake()

# inherit the first one here, School is the first one, so inherit School   
class Prentice(School):
    def __init__(self):
        self.skill = "[unique method]"
        
    def make_cake(self):
        print("use {} to make egg cake".format(self.skill))
        
    def make_master_cake(self):
        # if there is no init, it will be use unique method
        Master.__init__(self)
        # if there is no self, moyu cannot find make_cake
        Master.make_cake(self)
        
    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

    def make_old_cake(self):
        # Master.__init__(self)
        # Master.make_cake(self)
        # School.__init__(self)
        # School.make_cake(self)

        # super(Prentice, self).__init__()
        # super(Prentice, self).make_cake()
        
        super().__init__()
        super().make_cake()
        
moyu = Prentice()
moyu.make_old_cake()
