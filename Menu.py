from Office import Office
from Employee import Employee

class Menu  :
    def create_menu(self) :
        print('welcome')
        flag = 1
        while flag:
            print("oprations\n1)get all employee\n2)get employee by ID\n3)add new employee\n4)exit")
            opration = input(">")
            if opration == '1' :
                Office().get_all_employees()
            elif opration == '2' :
                id = input('enter id : ')
                if int(id):
                    Office().get_employee(int(id))
                else:
                    print('id not valid')
            elif opration == '3' :
                    name = input('name : ')
                    email = input('email : ')
                    salary = input('salary : ')
                    is_admin = input('admin ?(1 admin , 0 not admin) :')
                    helth = input('helth rate (from 1 to 100) : ')
                    Employee(name,email,int(salary),int(is_admin),int(helth))
            elif opration == '4' :
                flag = 0
            else :
                print('opration not valid')



