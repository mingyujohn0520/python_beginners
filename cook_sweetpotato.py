class Sweetpotato():
    def __init__(self):
        self.cook_time = 0
        self.status = "raw"
        self.condiments = []

    def cook(self, time):
        self.cook_time += time
        if self.cook_time >= 0 and self.cook_time < 3:
            self.status = "raw"
        elif self.cook_time >= 3 and self.cook_time < 5:
            self.status = "medium"
        elif self.cook_time >= 5 and self.cook_time < 8:
            self.status = "well done"
        elif self.cook_time > 8:
            self.status = "too much"
            
    def add_condiment(self, condiment):
        self.condiments.append(condiment)

    def __str__(self):
        return "the cook time is {}, the status is {}, the condiments have {}".format(self.cook_time, self.status, self.condiments)

sweet1 = Sweetpotato()
sweet1.cook(2)
sweet1.cook(2)
sweet1.add_condiment("pepper")
print(sweet1)