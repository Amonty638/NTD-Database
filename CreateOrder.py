from database.CustomerOrderDAO import CustomerOrderDAO
from database.CustomerOrder import CustomerOrder
from database.CustomerDAO import CustomerDAO
from database.Customer import Customer
from database.ProductDAO import ProductDAO
from database.Item import Item
from database.ItemDAO import ItemDAO
from database.EmployeeDAO import EmployeeDAO

import random


def create_new_customer():
    customer = Customer()
    print("Pleas enter the following information: ")
    print("Customer first name")
    customer.set_fname(input())

    print("Customer last name")
    customer.set_lname(input())

    print("Customer street address")
    customer.set_saddress(input())

    print("Customer city")
    customer.set_city(input())

    print("Customer zip code")
    customer.set_zip(input())

    print("Customer state")
    customer.set_state(input())

    print("Customer phone number")
    customer.set_phone(input())

    print("Customer email")
    customer.set_email(input())

    customer_dao = CustomerDAO()
    customer_dao.insert_customer(customer)
    print("|------------------------|")
    print("|      Create Order      |")
    print("|------------------------|")
    print("")
    create_order()



def generate_hold_num():
    value = ""
    for x in range(5):
        value = value + str(random.randint(0,9))
    return value


def create_order():
    print("Connecting to database...")
    customer_dao = CustomerDAO()
    customer_order_dao = CustomerOrderDAO()
    customer_order = CustomerOrder()
    product_dao = ProductDAO()
    item_dao = ItemDAO()
    employee_dao = EmployeeDAO()

    found = False
    list_of_employees = employee_dao.select_all()
    salesperson_num = 0
    while not found:
        print("Enter in salesperson number")
        salesperson_num = input()
        for emp in list_of_employees:
            if emp.get_salesperson_num() == salesperson_num:
                found = True
        if not found:
            print("No employee with that salesperson number")


    print("Please enter customer phone number ")
    phone_num = input()
    customer = customer_dao.select_by_phone(str(phone_num))
    customer_order.set_phone_num(customer.get_phone())
    customer_order.set_salesperson_num(salesperson_num)

    print("Please enter today's date ")
    date = input()
    customer_order.set_date_made(date)

    list_customer_orders = customer_order_dao.select_all()

    found = False
    hold_num = 0
    while not found:
        hold_num = generate_hold_num()
        for order in list_customer_orders:
            if hold_num == order.get_hold_num():
                found = True
        if found:
            found = False
        else:
            break
    customer_order.set_hold_num(hold_num)

    print("Please enter description of where tile will be located ")
    customer_order.set_description(input())

    print("Please enter delivery address")
    customer_order.set_delivery_address(input())
    customer_order.set_total_cost(0.00)#Initialize to 0 we will manipulate this after

    customer_order_dao.insert_customer_order(customer_order)



    list_of_products = product_dao.select_all()
    done = True
    total_cost = 0
    while done:
        found = False
        item = Item()
        while not found:
            print("Enter product NTD number")
            ntd_num = input()
            for x in list_of_products:
                if x.get_ntd_num() == ntd_num:
                    item.set_ntd_num(ntd_num)
                    found = True
            if not found:
                print("Wrong NTD number")
        print("Enter desired quantity of product, if grout enter number of bags, if tile enter square footage")
        item.set_quantity(input())
        cost = float(item.get_quantity()) * float(product_dao.select_by_ntd_num(item.get_ntd_num()).get_cost_per_sf())
        total_cost = float(total_cost) + float(cost)
        item.set_total_cost(str(cost))
        item.set_hold_num(hold_num)
        item_dao.insert_item(item)

        product = product_dao.select_by_ntd_num(item.get_ntd_num())
        newSquareFootage = float(product.get_amt_in_stock()) - float(item.get_quantity())
        newCartonCount = int(float(newSquareFootage) / float(product.get_sf_per_carton()))
        newPieceCount = int((float(newSquareFootage) % float(product.get_sf_per_carton())) / float(product.get_size_of_product()))
        product.set_amt_in_stock(str(newSquareFootage))
        product.set_carton_count(str(newCartonCount))
        product.set_piece_count(str(newPieceCount))
        product_dao.update(product)

        print("Enter another product?\n"
              "Press 1 for yes\n"
              "Press 2 to complete the order")
        choice = input()
        if choice == "2":
            customerOrder = customer_order_dao.select_by_hold_number(customer_order.get_hold_num())
            customerOrder.set_total_cost(total_cost)
            customer_order_dao.update(customerOrder)
            done = False


def main():

    while True:
        print("|------------------------|")
        print("|      Create Order      |")
        print("|------------------------|")
        print("")

        print("Is the order for an existing customer or a new customer?\n"
            "Press 1 if existing customer\n"
            "Press 2 if new customer\n"
            "Press 9 to return to index page")

        choice = input()
        if choice != 1 or choice != 2 or choice != 3:
            True

        if (choice == "1"):
            create_order()

        if (choice == "2"):
            create_new_customer()

        if (choice == "9"):
            break

