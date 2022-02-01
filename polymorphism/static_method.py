class Dog():
    @staticmethod   
    def info_print():
        print("this is a static method")
        
ad = Dog()
ad.info_print()

Dog.info_print() 