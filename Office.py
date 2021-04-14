from db_connect import db


class Office:

    def get_all_employees(self):
        employees = db().get_all_emp()
        print(employees)

    def get_employee(self, id):
        employee = db().get_emp_by_id(id)
        print(employee)

    def hire(self):
        print("hired")

    def fire(self):
        print("fired")