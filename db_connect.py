import mysql.connector

class db:

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="*tswa$1024",
            database="mydb"
        )
        self.cur = self.mydb.cursor()
        self.cur.execute('''CREATE SCHEMA IF NOT EXISTS mydb ''')
        self.cur.execute("CREATE TABLE IF NOT EXISTS employee ( id int PRIMARY KEY AUTO_INCREMENT, full_name VARCHAR(50), email VARCHAR(50),salary INT, is_manager INT )")
        self.mydb.commit()


    def get_all_emp(self):
        self.cur.execute("select * from mydb.employee")
        records = self.cur.fetchall()
        return records

    def get_emp_by_id(self, id):
        sql_select_query = """select * from employee where id = %s"""
        self.cur.execute(sql_select_query, (id,))
        records = self.cur.fetchall()
        return records
    def insert_emp(self, emp):
        sql = "INSERT INTO mydb.employee (full_name, email, salary, is_manager) VALUES (%s, %s, %s, %s)"
        val = (emp[0], emp[1], emp[2], emp[3])
        self.cur.execute(sql, val)
        self.mydb.commit()
        print("inserted")