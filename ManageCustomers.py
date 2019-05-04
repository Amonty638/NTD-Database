from database.Customer import Customer
from database.CustomerDAO import CustomerDAO
from database.CustomerOrderDAO import CustomerOrderDAO


def main():
    print("|----------------------------|")
    print("|        Edit Customer       |")
    print("|----------------------------|")
    print("")

    while True:

        print("Press 1 to view all customers")
        print("Press 2 to add a customer")
        print("Press 3 to delete a customer")
        print("Press 4 to change a customer's first name")
        print("Press 5 to change a customer's last name")
        print("Press 6 to change a customer's city")
        print("Press 7 to change a customer's state")
        print("Press 8 to change a customer's zip")
        print("Press 9 to change a customer's street address")
        print("Press 10 to change a customer's email")
        print("Press 11 to return to index page")
        print("")

        choice = input()

        if choice =="1":
            viewCustomers()

        elif choice=="2":
            addCustomer()

        elif choice =="3":
            deleteCustomer()

        elif choice == "4":
            changeCustomerFname()

        elif choice == "5":
            changeCustomerLname()

        elif choice == "6":
            changeCustomerCity()

        elif choice == "7":
            changeCustomerState()

        elif choice == "8":
            changeCustomerZip()

        elif choice == "9":
            changeCustomerStreetAddress()

        elif choice == "10":
            changeCustomerEmail()

        elif choice == "11":
            break

        else:
            print("Invalid entry, please try again")
            print("")


def viewCustomers():

    customerDao = CustomerDAO()

    customer_list = customerDao.select_all()

    for customer in customer_list:
        print("First name: " + customer.get_fname())
        print("Last name: " + customer.get_lname())
        print("City: " + customer.get_city())
        print("State: " + customer.get_state())
        print("Zip: " + customer.get_zip())
        print("Street Address: " + customer.get_saddress())
        print("Email: " + customer.get_email())
        print("Phone: " + customer.get_phone())
        print("")
        print("")


def addCustomer():

    customerDao = CustomerDAO()

    while True:
        print("Enter the Phone# of a customer you would like to add")

        phone_num = input()

        customer_exists = verifyPhoneNum(phone_num)

        if customer_exists == True:
            print("A customer with that phone# already exists, please try again")
            print("")

        else:
            customer = Customer()
            print("Enter customer's first name")
            fname = input()
            print("Enter customer's last name")
            lname = input()
            print("Enter customer's city")
            city = input()
            print("Enter customer's state")
            state = input()
            print("Enter customer's zip code")
            zip = input()
            print("Enter customer's street address")
            saddress = input()
            print("Enter customer's email")
            email = input()

            customer.set_fname(fname)
            customer.set_lname(lname)
            customer.set_city(city)
            customer.set_state(state)
            customer.set_zip(zip)
            customer.set_saddress(saddress)
            customer.set_email(email)
            customer.set_phone(phone_num)

            customerDao.insert_customer(customer)
            break


def verifyPhoneNum(phone_num):

    customer_exists = False

    customerDao = CustomerDAO()

    customer_list = customerDao.select_all()

    for customer in customer_list:
        if customer.get_phone() == phone_num:
            customer_exists = True
            break

    return customer_exists


def deleteCustomer():

    while True:
        print("Enter the Phone# of a customer you would like to delete or press 1 to quit")

        phone_num = input()

        if phone_num == "1":
            break

        customer_exists = verifyPhoneNum(phone_num)

        if customer_exists == False:
            print("A customer with that phone# does not exist, please try again")
            print("")

        else:

            order_exists = checkForCustomerOrder(phone_num)

            if order_exists == True:
                print("That customer already has orders placed. Delete the orders before deleting the customer")
                print("")

            else:
                customerDao = CustomerDAO()

                customerDao.delete_customer_by_phone_number(phone_num)
                print("Customer deleted")
                print("")
                break


def checkForCustomerOrder(phone_num):

    customerOrderDao = CustomerOrderDAO()

    order_exists = False

    customer_orders_list = customerOrderDao.select_all()

    for order in customer_orders_list:
        if order.get_phone_num() == phone_num:
            order_exists = True
            break

    return order_exists


def changeCustomerFname():
    customerDao = CustomerDAO()

    while True:
        print("Enter the Phone# of a customer who's first name you would like to change")

        phone_num = input()

        customer_exists = verifyPhoneNum(phone_num)

        if customer_exists == True:

            customer = customerDao.select_by_phone(phone_num)

            print("Enter the new first name")

            fname = input()

            customer.set_fname(fname)
            customerDao.update(customer)
            print("First name changed")
            print("")
            break

        else:
            print("Phone# does not match an existing customer, please try again")
            print("")

def changeCustomerLname():
    customerDao = CustomerDAO()

    while True:
        print("Enter the Phone# of a customer who's last name you would like to change")

        phone_num = input()

        customer_exists = verifyPhoneNum(phone_num)

        if customer_exists == True:

            customer = customerDao.select_by_phone(phone_num)

            print("Enter the new last name")

            lname = input()

            customer.set_lname(lname)
            customerDao.update(customer)
            print("Last name changed")
            print("")
            break

        else:
            print("Phone# does not match an existing customer, please try again")
            print("")

def changeCustomerCity():
    customerDao = CustomerDAO()

    while True:
        print("Enter the Phone# of a customer who's city you would like to change")

        phone_num = input()

        customer_exists = verifyPhoneNum(phone_num)

        if customer_exists == True:

            customer = customerDao.select_by_phone(phone_num)

            print("Enter the new city")

            city = input()

            customer.set_city(city)
            customerDao.update(customer)
            print("City changed")
            print("")
            break

        else:
            print("Phone# does not match an existing customer, please try again")
            print("")

def changeCustomerState():
    customerDao = CustomerDAO()

    while True:
        print("Enter the Phone# of a customer who's state you would like to change")

        phone_num = input()

        customer_exists = verifyPhoneNum(phone_num)

        if customer_exists == True:

            customer = customerDao.select_by_phone(phone_num)

            print("Enter the new state")

            state = input()

            customer.set_state(state)
            customerDao.update(customer)
            print("State changed")
            print("")
            break

        else:
            print("Phone# does not match an existing customer, please try again")
            print("")

def changeCustomerZip():
    customerDao = CustomerDAO()

    while True:
        print("Enter the Phone# of a customer who's zip code you would like to change")

        phone_num = input()

        customer_exists = verifyPhoneNum(phone_num)

        if customer_exists == True:

            customer = customerDao.select_by_phone(phone_num)

            print("Enter the new zip code")

            zip = input()

            customer.set_zip(zip)
            customerDao.update(customer)
            print("Zip code changed")
            print("")
            break

        else:
            print("Phone# does not match an existing customer, please try again")
            print("")

def changeCustomerEmail():
    customerDao = CustomerDAO()

    while True:
        print("Enter the Phone# of a customer who's email you would like to change")

        phone_num = input()

        customer_exists = verifyPhoneNum(phone_num)

        if customer_exists == True:

            customer = customerDao.select_by_phone(phone_num)

            print("Enter the new email")

            email = input()

            customer.set_email(email)
            customerDao.update(customer)
            print("Email changed")
            print("")
            break

        else:
            print("Phone# does not match an existing customer, please try again")
            print("")

def changeCustomerStreetAddress():
    customerDao = CustomerDAO()

    while True:
        print("Enter the Phone# of a customer who's street address you would like to change")

        phone_num = input()

        customer_exists = verifyPhoneNum(phone_num)

        if customer_exists == True:

            customer = customerDao.select_by_phone(phone_num)

            print("Enter the new street address")

            saddress = input()

            customer.set_saddress(saddress)
            customerDao.update(customer)
            print("Street address changed")
            print("")
            break

        else:
            print("Phone# does not match an existing customer, please try again")
            print("")

















