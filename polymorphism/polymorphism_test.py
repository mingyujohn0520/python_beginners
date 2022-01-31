class Dog():
    def work(self):
        pass

class ArmyDog(Dog):
    def work(self):
        print("protect people")

class DrugDog(Dog):
    def work(self):
        print("check if there is drug")

class Person():
    def work_with_dog(self, dog):
        dog.work()

ad = ArmyDog()
dd = DrugDog()

moyu = Person()
moyu.work_with_dog(ad)
moyu.work_with_dog(dd)