class Dog():
    __tooth = 10

    @classmethod
    def get_tooth(cls):
        return cls.__tooth
    
ad = Dog()
print(ad.get_tooth())
        