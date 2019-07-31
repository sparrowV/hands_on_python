import copy
import json

def get_employee_by_salary(employees,salary_from):
    result = []
    for employee in employees:
        if(employee['salary'] > salary_from):
            result.append(copy.deepcopy(employee))
    return result

def get_employees_by_countries(employees):
    result = {}
    for employee in employees:
        country = employee['country']
        if(country in result):
            result[country]+=1
        else:
            result[country] = 1
    return sorted(result.items(), key = lambda key_value :key_value[1],reverse= True )

def save_employee_summary(employees,filename,keys):
    with open(filename,'w') as f:
        result = []
        for employee in employees:
            employee_summary = {}
            for key in keys:
                employee_summary[key] = employee[key]
            result.append(employee_summary)
        json.dump(result,f,indent=4)

with open('employees.json') as f:
    employees = json.load(f)
    print(len(employees))
    # print(employees)
    employees_by_salary = get_employee_by_salary(employees,4000)
    print(employees_by_salary)
    print(len(employees_by_salary))
    employees_by_countries = get_employees_by_countries(employees)
    print(employees_by_countries)
    save_employee_summary(employees,"output.json",['fullname','email','salary'])