from database.Employee import Employee
from database.Connect import Connect


class EmployeeDAO(Connect):
    def __init__(self):
        Connect.__init__(self)


    def select_all(self):
        connect = Connect()
        connect.sql_execute('select * from employee')
        employee_list = []
        for row in connect.cur:

            employee = Employee()
            employee.set_values_from_row(list(row))
            employee_list.append(employee)

        return employee_list

employeeDao = EmployeeDAO()

list = employeeDao.select_all()

for employee in list:
    print(employee.get_fname())

print("TEST")