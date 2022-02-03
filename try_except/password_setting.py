class ShortInputError(Exception):
    def __init__(self, length, min_length):
        self.length = length
        self.min_length = min_length

    def __str__(self):
        return "the length of password you key in is {}, the password length should equal or greater than {}".format(self.length, self.min_length)

def main():
    try:
        passwd = input("please key in your password: ")
        if len(passwd) < 3:
            raise ShortInputError(len(passwd), 3)
    except Exception as result:
        print(result)

    else:
        print("password set up successfully!")
        
main()