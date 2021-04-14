from Person import Person
from db_connect import db
import random
import re

class Employee(Person):

    ID = None
    Email = None
    Work_mood = None
    Salary = None
    Is_manager = None
    Health_rate = None

    def __init__(self,Full_name , email, salary, is_manager, health_rate):
        self.full_name = Full_name
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex, email):
            self.Email = email
        else:
            raise Exception("Sorry, email isn't valid")

        if salary >= 1000:
            self.Salary = salary
        else:
            raise Exception("Sorry, salary must be 1000 or more")

        if 0 < health_rate < 100:
            self.Health_rate = health_rate
        else:
            self.healthRate = random.randrange(1, 100, 1)

        if is_manager == 0 or is_manager == 1:
            self.Is_manager = is_manager
        else:
            raise Exception("Sorry, is_manager must be 0 or 1")

        db().insert_emp((Full_name,email, salary, is_manager))
        

    def sleep(self, hours):
        if hours < 7:
            print("tired")
        elif hours > 7:
            print("lazy")
        else:
            print("happy")

    def eat(self, meals):
        if meals == 3:
            print("health rate = 100")
        elif meals == 2:
            print("health rate = 75")
        elif meals == 1:
            print("health rate = 50")
        else:
            print("not human")

    def buy(self, items):
        for x in range(items):
            if self.Salary < 10:
                raise Exception("Sorry, is_manager must be 0 or 1")
            self.Salary -= 10

    def sendEmail(self, to, bodyreciever_name):
        f = open('email.txt', 'w')
        email = f'to : {to} \n' \
                f'subject : welcome email \n' \
                f'reciever : {bodyreciever_name} \n' \
                f'welcome to lab 2'
        f.write(email)
        f.close()