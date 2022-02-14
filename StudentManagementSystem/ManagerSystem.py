from student import *

class StudentManagement():
    def __init__(self):
        self.student_list = []
        
    def run(self):
        
        self.load_student()
        
        while True:
            self.show_menu()
           
            menu_num = int(input("please key in function number: ")) 
           
            if menu_num == 1:
                self.add_student()
            elif menu_num == 2:
                self.delete_student()
            elif menu_num == 3:
                self.modify_student()
            elif menu_num == 4:
                self.search_student()
            elif menu_num == 5:
                self.list_student()
            elif menu_num == 6:
                self.save_student()
            elif menu_num == 7:
                break
           
    @staticmethod
    def show_menu():
        print("Please choose the following functions: ")
        print("1. Add on a student")
        print("2. Delete a student")
        print("3. Modify a student information")
        print("4. Search a student")
        print("5. List all students")
        print("6. Save student information")
        print("7. Log out the system")
    
    def add_student(self):
        name = input("please key in the student name: ")
        gender = input("please key in the student gender: ")
        mobile = input("please key in the student mobile: ")
        
        new_student = Student(name, gender, mobile)
        self.student_list.append(new_student)
        
        print(self.student_list)
        print(new_student)

    def delete_student(self):
        del_name = input("please key in the student name you want to delete: ")
        
        for i in self.student_list:
            if i.name == del_name:
                self.student_list.remove(i)
                break
        else:
            print("this student is not on the list")
        
        print(self.student_list)
        
    def modify_student(self):
        
        modify_name = input("please key in the student name you want to modify: ")
        
        for i in self.student_list:
            if i.name == modify_name:
                i.name = input("please key in student name: ")
                i.gender = input("please key in student gender: ")
                i.mobile = input("please key in the student mobile: ")
                print("modified succefully! Name: {}, Gender: {}, Mobile: {}".format(i.name, i.gender, i.mobile))
                break
            
            else:
                print("this student doesn't exists")

    def search_student(self):
        
        search_name = input("please key in the student name you want to search: ")
        
        for i in self.student_list:
            if i.name == search_name:
                print("Name: {}, Gender: {}, Mobile: {}".format(i.name, i.gender, i.mobile))
                break
        
        else:
            print("this student doesn't exists")
            
        
    def list_student(self):
        print("name\tgender\tmobile")
        
        for i in self.student_list:
            print("{}\t{}\t{}".format(i.name, i.gender, i.mobile))

    def save_student(self):
        f = open("student.data", "w")
        new_list = [i.__dict__ for i in self.student_list]
        f.write(str(new_list))
        f.close()
                
    def load_student(self):
        try:
            f = open("student.data", "r")
        except:
            f = open("student.data", "w")
        else:
            data = f.read()
            new_list = eval(data)
            self.student_list = [Student(i["name"], i["gender"], i["mobile"]) for i in new_list]
        finally:
            f.close()
