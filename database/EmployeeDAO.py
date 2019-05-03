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
            employee.set_values_from_row(row)
            employee_list.append(employee)

        return employee_list

    def select_by_salesperson_num(self,key):
        connect = Connect()
        connect.sql_execute('select * from employee where salesperson# =  ' + str(key) + '')
        row = connect.cur.fetchone()

        employee = Employee()
        employee.set_values_from_row(row)

        return employee

    def insert_employee(self,employee):
        connect = Connect()
        connect.cur.execute('insert into employee values( ' + employee.get_values_string())
        connect.commit()


    def update(self, employee):
        connect = Connect()
        connect.sql_execute("update employee set " +
                            "fname = '" + employee.get_fname() + "'," +
                            "lname = '" + employee.get_lname() + "'," +
                            "salesperson# = '" + employee.get_salesperson_num() + "' " +
                            "where salesperson# = '" + employee.get_salesperson_num() + "'")
        connect.commit()

    def delete_employee(self,key):
        connect = Connect()
        connect.cur.execute('delete from employee where salesperson# = ' + "'" + str(key) + "'")
        connect.commit()



#employeeDao = EmployeeDAO()
#
# employeeDao.delete_employee(99)
#
# newEmployee = Employee()
# newEmployee.set_fname("test")
# newEmployee.set_lname("Montano")
# newEmployee.set_salesperson_num(6969)
# print(newEmployee.get_values_string())
# employeeDao.insert_employee(newEmployee)
#
#
# list = employeeDao.select_all()
#
# for item in list:
#     print(item.get_fname())

# employee = employeeDao.select_by_salesperson_num(25)
#
# print(employee.get_fname())
#
# employee.set_fname("Zander")
#
# employeeDao.update(employee)
#
# print(employeeDao.select_by_salesperson_num(25).get_fname())