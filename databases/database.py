import sqlite3 as db
import json

connection = db.connect("my_database.db")
cursor = connection.cursor()

def insert_employee(employee,cursor):
    insert_employee_string = "insert into Employees(fullname,email,salary,country) values (:fullname,:email,:salary,:country)"
    cursor.execute(insert_employee_string,{'fullname':employee['fullname'],'email':employee['email'],'salary':employee['salary'],
                                           'country':employee['country']})


def get_emplooyes_by_salary(salary,cursor):
    employees_obj = cursor.execute("select * from Employees where salary >:salary",{'salary':salary})
    return employees_obj.fetchall()


def get_employees_by_country_and_salary(country,salary):
    pass


employee_table = '''
    CREATE TABLE Employees(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname text,
        email text,
        salary INTEGER,
        country text
    
    );
'''

cursor.execute(employee_table)
with open("employees.json") as f:
    employees = json.load(f)
    for employee in employees:
        insert_employee(employee,cursor)

connection.commit()
filtered_employees = get_emplooyes_by_salary(2000,cursor)
print(len(filtered_employees))
print(filtered_employees)


cursor.close()
connection.close()
