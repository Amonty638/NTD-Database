from database.Employee import Employee
from database.EmployeeDAO import EmployeeDAO
from database.CustomerOrderDAO import CustomerOrderDAO

def view_employee_orders():
    print("|----------------------------|")
    print("|       Employee Orders      |")
    print("|----------------------------|")
    print("")
    employee_dao = EmployeeDAO()
    employee_list = employee_dao.select_all()
    for employee in employee_list:
        print(employee.get_fname() + " " + employee.get_lname() + " " + employee.get_salesperson_num())

    found = False
    salesperson_num = 100000
    while not found:
        print("\nEnter in an Employee's salesperson number to view their placed orders")
        salesperson_num = input()
        for employee in employee_list:
            if employee.get_salesperson_num() == salesperson_num:
                found = True

    employee = employee_dao.select_by_salesperson_num(salesperson_num)
    customer_order_dao = CustomerOrderDAO()
    customer_order_list = customer_order_dao.select_all()
    print(employee.get_fname() + " " + employee.get_lname() + " " + employee.get_salesperson_num())
    print(employee.get_fname() + "'s Orders")
    for customer_order in customer_order_list:
        if customer_order.get_salesperson_num() == employee.get_salesperson_num():
            print(customer_order.get_dictionary())
            print("----------------------------------------------------------------------------------------------------"
                  "-----------------------------------------\n")


def edit_employee():
    print("|----------------------------|")
    print("|        Edit Employee       |")
    print("|----------------------------|")
    print("")

    employee_dao = EmployeeDAO()
    employee_list = employee_dao.select_all()
    for employee in employee_list:
        print(employee.get_fname() + " " + employee.get_lname() + " " + employee.get_salesperson_num())

    found = False
    salesperson_num = 100000
    while not found:
        print("\nEnter in an Employee's salesperson number to edit")
        salesperson_num = input()
        for employee in employee_list:
            if employee.get_salesperson_num() == salesperson_num:
                found = True

    employee = employee_dao.select_by_salesperson_num(salesperson_num)

    print("Press 1 to edit first name\n"
          "Press 2 to edit last name\n"
          "Press 3 to delete employee\n"
          "Press 9 to return to Employee Index")

    choice = input()

    if choice == "1":
        print("Enter in first name")
        employee.set_fname(input())
        employee_dao.update(employee)

    if choice == "2":
        print("Enter in last name")
        employee.set_lname(input())
        employee_dao.update(employee)

    if choice == "3":
        print("Deleting employee " + employee.get_fname() + " " + employee.get_lname())
        employee_dao.delete_employee(employee.get_salesperson_num())

    else:
        return 0



def main():
    while True:
        print("|----------------------------|")
        print("|          Employee          |")
        print("|----------------------------|")
        print("")

        print("Press 1 to view an Employee's customer orders\n"
              "Press 2 to edit an Employee\n"
              "Press 3 to add an Employee\n"
              "Press 9 to go to return to index page")
        choice = input()

        if choice == "1":
            view_employee_orders()

        if choice == "2":
            edit_employee()

        if choice == "9":
            break
