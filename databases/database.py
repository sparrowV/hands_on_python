import sqlite3 as db
import json
connection = db.connect("my_database.db")
cursor = connection.cursor()


def insert_employee(employee, cursor):
    insert_post_string = " insert into Employees(fullname,email,salary,country) values(:fullname,:email,:salary,:country)"
    cursor.execute(insert_post_string, {'fullname': employee['fullname'], 'email':employee['email'],
                                        'salary': employee['salary'],'country':employee['country']})

def get_employees_by_salary(salary):
    employees_obj = cursor.execute("select * from Employees where salary>:salary",{'salary':salary})
    return employees_obj.fetchall()

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
filtered_employees = get_employees_by_salary(2000)
print(filtered_employees)
print(len(filtered_employees))
cursor.close()
connection.close()

