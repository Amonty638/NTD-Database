from database.CustomerOrder import CustomerOrder
from database.CustomerOrderDAO import CustomerOrderDAO
from database.CustomerDAO import CustomerDAO
from database.ItemDAO import ItemDAO
from database.ProductDAO import ProductDAO
from database.Item import Item
from database.Product import Product
import math

customerOrderDAO = CustomerOrderDAO()
customerDAO = CustomerDAO()
itemDAO = ItemDAO()
productDAO = ProductDAO()

def deleteCustomerOrderPickUp():


    while True:

        print("Press 1 to enter hold#")
        print("Press 2 to quit")

        choice = input()

        if choice == "1":

            print("Enter hold#")

            hold_num = input()

            valid_hold_num = varifyHoldNum(hold_num)

            if valid_hold_num == False:
                print("The hold# you tried to search by is invalid, please try again")
                print("")
            else:
                customerOrderDAO.delete_customer_order_by_hold_num(hold_num)
                itemDAO.delete_item_using_hold_num(hold_num)
                print("Delete Completed")
                print("")


        elif choice =="2":
            break

        else:
            print("Invalid entry, please try again")

def deleteCustomerOrderCancelled():


    while True:

        print("Press 1 to enter hold#")
        print("Press 2 to quit")

        choice = input()

        if choice == "1":

            print("Enter hold#")

            hold_num = input()

            valid_hold_num = varifyHoldNum(hold_num)

            if valid_hold_num == False:
                print("The hold# you tried to search by is invalid, please try again")
                print("")
            else:
                items = itemDAO.select_all()

                for item in items:
                    if item.get_hold_num() == hold_num:

                        product = productDAO.select_by_ntd_num(item.get_ntd_num())
                        originalQty = product.get_amt_in_stock()
                        newQty = originalQty + item.get_quantity()

                        newCartonCount = int(float(newQty) / float(product.get_sf_per_carton()))
                        newPieceCount = int((float(newQty) % float(product.get_sf_per_carton())) / float(
                        product.get_size_of_product()))
                        product.set_amt_in_stock(str(newQty))
                        product.set_carton_count(str(newCartonCount))
                        product.set_piece_count(str(newPieceCount))
                        productDAO.update(product)

                        itemDAO.delete_item(item.get_ntd_num(), hold_num)
                        customerOrderDAO.delete_customer_order_by_hold_num(hold_num)
                        print("Delete Completed")
                        print("")


        elif choice == "2":
            break

        else:
            print("Invalid entry, please try again")

def editCustomerOrder():


    while True:

        print("Press 1 to enter hold# for the order you would like to edit")
        print("Press 2 to quit")

        choice = input()

        if choice == "1":

            print("Enter hold#")

            hold_num = input()

            valid_hold_num = varifyHoldNum(hold_num)

            if valid_hold_num == False:
                print("The hold# you tried to search by is invalid, please try again")
                print("")

            else:
                while True:
                    print("Press 1 to delete an item")
                    print("Press 2 to add an item")
                    print("Press 3 to quit")

                    choice2 = input()

                    if choice2 == "1":
                        deleteItem(hold_num)
                        break

                    elif choice2 == "2":
                        addItem(hold_num)
                        break

                    elif choice2 == "3":
                        break

                    else:
                        print("Invalid entry, please try again")

        elif choice == "2":
            break

        else:
            print("Invalid entry, please try again")


def deleteItem(hold_num):
    order = customerOrderDAO.select_by_hold_number(hold_num)
    print("Hold Num:" + "            " + "Customer Name:" + "            " +
          "Date Made:" + "            " + "Delivery Address:" + "            " + "Phone#:")
    print(order.get_hold_num() + "                " +
          customerDAO.select_by_phone(order.get_phone_num()).get_lname() + "," +
          customerDAO.select_by_phone(order.get_phone_num()).get_fname() + "              " +
          order.get_date_made() + "             " +
          order.get_delivery_address() + "          "
          + order.get_phone_num())

    print()

    items = itemDAO.select_by_hold_num(hold_num)

    print("NTD#:" + "                " + "Quantity:" + "                 " + "Total Cost:" +
          "           " + "Carton Count:" + "                " + "Piece count:")
    for item in items:
        print(item.get_ntd_num() + "                 " +
              str(item.get_quantity()) + "                      " + str(item.get_total_cost()) +
              "                 " +
              str(calculateCartonCount(item.get_quantity(), item.get_ntd_num()))
              + "                            " +
              str(calculatePieceCount(item.get_quantity(), item.get_ntd_num())))


    while True:
        print("Enter the NTD# for the item you would like to delete or press 1 to quit")


        ntd_num = input()

        if ntd_num == "1":
            break

        valid_ntd_num = verifyNTDNumDel(ntd_num, hold_num)

        if valid_ntd_num == False:
            print("The hold# you tried to search by is invalid, please try again")
            print("")

        else:

            customerOrder = customerOrderDAO.select_by_hold_number(hold_num)

            total_cost_of_order = customerOrder.get_total_cost()

            for item in items:
                if item.get_ntd_num() == ntd_num:
                    product = productDAO.select_by_ntd_num(item.get_ntd_num())
                    originalQty = product.get_amt_in_stock()
                    newQty = originalQty + item.get_quantity()

                    newCartonCount = int(float(newQty) / float(product.get_sf_per_carton()))
                    newPieceCount = int((float(newQty) % float(product.get_sf_per_carton())) / float(
                        product.get_size_of_product()))
                    product.set_amt_in_stock(str(newQty))
                    product.set_carton_count(str(newCartonCount))
                    product.set_piece_count(str(newPieceCount))
                    productDAO.update(product)

                    cost_per_item = item.get_total_cost()
                    total_cost_of_order = total_cost_of_order - cost_per_item

                    itemDAO.delete_item(item.get_ntd_num(), hold_num)
                    customerOrder.set_total_cost(total_cost_of_order)
                    customerOrderDAO.update(customerOrder)
            break


def verifyNTDNumDel(ntd_num,hold_num):

    items = itemDAO.select_by_hold_num(hold_num)
    valid_ntd_num = False

    for item in items:
        if item.get_ntd_num() == ntd_num:
            valid_ntd_num = True
            break

    return valid_ntd_num

def verifyNTDNumAdd(ntd_num):
    valid_ntd_num = False

    products = productDAO.select_all()

    for product in products:
        if product.get_ntd_num() == ntd_num:
            valid_ntd_num = True
            break

    return valid_ntd_num


def addItem(hold_num):
    order = customerOrderDAO.select_by_hold_number(hold_num)
    print("Hold Num:" + "            " + "Customer Name:" + "            " +
          "Date Made:" + "            " + "Delivery Address:" + "            " + "Phone#:")
    print(order.get_hold_num() + "                " +
          customerDAO.select_by_phone(order.get_phone_num()).get_lname() + "," +
          customerDAO.select_by_phone(order.get_phone_num()).get_fname() + "              " +
          order.get_date_made() + "             " +
          order.get_delivery_address() + "          "
          + order.get_phone_num())

    print()

    items = itemDAO.select_by_hold_num(hold_num)

    print("NTD#:" + "                " + "Quantity:" + "                 " + "Total Cost:" +
          "           " + "Carton Count:" + "                " + "Piece count:")
    for item in items:
        print(item.get_ntd_num() + "                 " +
              str(item.get_quantity()) + "                      " + str(item.get_total_cost()) +
              "                 " +
              str(calculateCartonCount(item.get_quantity(), item.get_ntd_num()))
              + "                            " +
              str(calculatePieceCount(item.get_quantity(), item.get_ntd_num())))

    while True:
        print("Enter the NTD# for the item you would like to add or press 1 to quit")

        ntd_num = input()

        if ntd_num == "1":
            break

        valid_ntd_num = verifyNTDNumAdd(ntd_num)

        if valid_ntd_num == False:
            print("The NTD# you tried to search by is invalid, please try again")
            print("")

        else:

            item = Item()
            item.set_hold_num(hold_num)
            item.set_ntd_num(ntd_num)

            print("Enter desired quantity of product, if grout enter number of bags, if tile enter square footage")
            item.set_quantity(input())
            cost = float(item.get_quantity()) * float(
                productDAO.select_by_ntd_num(item.get_ntd_num()).get_cost_per_sf())


            product = productDAO.select_by_ntd_num(ntd_num)
            newSquareFootage = float(product.get_amt_in_stock()) - float(item.get_quantity())
            newCartonCount = int(float(newSquareFootage) / float(product.get_sf_per_carton()))
            newPieceCount = int(
                (float(newSquareFootage) % float(product.get_sf_per_carton())) / float(product.get_size_of_product()))
            product.set_amt_in_stock(str(newSquareFootage))
            product.set_carton_count(str(newCartonCount))
            product.set_piece_count(str(newPieceCount))
            productDAO.update(product)

            total_cost_of_item = float(cost)
            item.set_total_cost(str(cost))
            item.set_hold_num(hold_num)
            itemDAO.insert_item(item)

            customerOrder = customerOrderDAO.select_by_hold_number(hold_num)
            customerOrder.set_total_cost(float(total_cost_of_item) + float(customerOrder.get_total_cost()))
            customerOrderDAO.update(customerOrder)
            break

def main():

    print("|---------------------------|")
    print("|  Welcome to Manage Order  |")
    print("|---------------------------|")
    print("")

    customer_list = customerDAO.select_all()
    customer__order_list = customerOrderDAO.select_all()
    listHeader = ("Hold Num:", "Customer Name:", "Phone #:")
    print('{0:>5} {1:>26} {2:>20}'.format(*listHeader))
    for order in customer__order_list:
        for customer in customer_list:
            if customer.get_phone() == order.get_phone_num():
                list = (order.get_hold_num(), str(customer.get_lname()) + ", " + str(customer.get_fname()), customer.get_phone())
                print('{0:>5} {1:>30} {2:>20}'.format(*list))

    while True:

        print("")
        print("Press 1 to view item details associated with a hold#")
        print("Press 2 to view item details associated with a customer phone#")
        print("Press 3 to delete a customer order that was picked up")
        print("Press 4 to delete a customer order that was cancelled")
        print("Press 5 to edit a customer order")
        print("Press 9 to return to Index")
        print("")

        choice = input()

        if choice == "1":

            while True:

                print("Press 1 to enter hold#")
                print("Press 2 to quit")
                print("")

                choice2 = input()

                if choice2 == "1":

                    print("Enter the hold#")

                    hold_num = input()

                    valid_hold_num = varifyHoldNum(hold_num)

                    if valid_hold_num == False:
                        print("The hold# you tried to search by is invalid, please try again")
                        print("")

                    else:
                        order = customerOrderDAO.select_by_hold_number(hold_num)
                        listHeader = ("Hold Num:", "Customer Name:", "Date Made:", "Delivery Address:", "Phone#:")
                        print('{0:>5} {1:>23} {2:>12} {3:>25} {4:>20}'.format(*listHeader))
                        list = (order.get_hold_num(), str(customerDAO.select_by_phone(order.get_phone_num()).get_lname()) + ", " + str(customerDAO.select_by_phone(order.get_phone_num()).get_fname()), order.get_date_made(), order.get_delivery_address(), order.get_phone_num())
                        print('{0:>5} {1:>26} {2:>12} {3:>25} {4:>20}'.format(*list))
                        print("")
                        items = itemDAO.select_by_hold_num(hold_num)
                        listHeader = ("NTD#:", "Quantity:", "Total Cost:", "Carton Count:", "Piece count:")
                        print('{0:>15} {1:>17} {2:>18} {3:>18} {4:>15}'.format(*listHeader))
                        for item in items:
                            list = (item.get_ntd_num(), item.get_quantity(), item.get_total_cost(), calculateCartonCount(item.get_quantity(),item.get_ntd_num()), calculatePieceCount(item.get_quantity(),item.get_ntd_num()))
                            print('{0:>15} {1:>17} {2:>18} {3:>18} {4:>15}'.format(*list))
                        print("")
                elif choice2 == "2":
                    break

                else:
                    print("Invalid entry, please try again")

        elif choice == "2":
            while True:

                print("Press 1 to enter phone#")
                print("Press 2 to quit")
                print("")

                choice2 = input()

                if choice2 == "1":

                    print("Enter the phone#")

                    phone_num = input()

                    valid_phone_num = varifyPhoneNum(phone_num)

                    if valid_phone_num == False:
                        print("The phone# you tried to search by is invalid, please try again")
                        print("")

                    else:
                        orders = customerOrderDAO.select_by_customer_phone(phone_num)
                        listHeader = ("Hold Num:", "Customer Name:", "Date Made:", "Delivery Address:", "Phone#:")
                        print('{0:>5} {1:>23} {2:>12} {3:>25} {4:>20}'.format(*listHeader))
                        for order in orders:
                            list = (order.get_hold_num(), str(customerDAO.select_by_phone(order.get_phone_num()).get_lname()) + ", " + str(customerDAO.select_by_phone(order.get_phone_num()).get_fname()), order.get_date_made(), order.get_delivery_address(), order.get_phone_num())
                            print('{0:>5} {1:>26} {2:>12} {3:>25} {4:>20}'.format(*list))

                        print()
                        print("")

                        while True:
                            print("Press 1 to view order")
                            print("Press 2 to quit")

                            choice3 = input()

                            if choice3 == "1":
                                print("Enter Hold#")

                                hold_num = input()

                                valid_hold_num = varifyHoldNum(hold_num)

                                if valid_hold_num == False:
                                    print("The hold# you tried to search by is invalid, please try again")
                                    print("")

                                else:
                                    order = customerOrderDAO.select_by_hold_number(hold_num)
                                    listHeader = (
                                    "Hold Num:", "Customer Name:", "Date Made:", "Delivery Address:", "Phone#:")
                                    print('{0:>5} {1:>23} {2:>12} {3:>25} {4:>20}'.format(*listHeader))
                                    list = (order.get_hold_num(), str(customerDAO.select_by_phone(order.get_phone_num()).get_lname()) + ", " + str(customerDAO.select_by_phone(order.get_phone_num()).get_fname()), order.get_date_made(), order.get_delivery_address(), order.get_phone_num())
                                    print(print('{0:>5} {1:>26} {2:>12} {3:>25} {4:>20}'.format(*list)))
                                    items = itemDAO.select_by_hold_num(hold_num)
                                    print("")
                                    listHeader = ("NTD#:", "Quantity:", "Total Cost:", "Carton Count:", "Piece count:")
                                    print('{0:>15} {1:>17} {2:>18} {3:>18} {4:>15}'.format(*listHeader))
                                    for item in items:
                                        list = (item.get_ntd_num(), item.get_quantity(), item.get_total_cost(), calculateCartonCount(item.get_quantity(), item.get_ntd_num()), calculatePieceCount(item.get_quantity(), item.get_ntd_num()))
                                        print('{0:>15} {1:>17} {2:>18} {3:>18} {4:>15}'.format(*list))
                                    print("")
                            elif choice3 == "2":
                                break

                            else:
                                print("Invalid entry, please try again")


                elif choice2 == "2":
                    break

                else:
                    print("Invalid entry, please try again")

        elif choice == "3":
            deleteCustomerOrderPickUp()

        elif choice == "4":
            deleteCustomerOrderCancelled()

        elif choice == "5":
            editCustomerOrder()

        elif choice == "9":
            break

        else:
            print("Invalid entry please try again")


def varifyHoldNum(hold_num):


    customer_order_list = customerOrderDAO.select_all()
    valid_hold_num = False

    for order in customer_order_list:
        if order.get_hold_num() == hold_num:
            valid_hold_num = True
            break

    return valid_hold_num

def calculateCartonCount(quantity, ntd_num):

    list_of_products = productDAO.select_all()

    for product in list_of_products:
        if product.get_ntd_num() == ntd_num:
            carton_count = int(quantity / product.get_sf_per_carton())

    return str(carton_count)


def calculatePieceCount(quantity, ntd_num):
    list_of_products = productDAO.select_all()

    for product in list_of_products:
        if product.get_ntd_num() == ntd_num:
            calculation = quantity % product.get_sf_per_carton()
            piece_count = math.ceil(calculation / product.get_size_of_product())

    return str(piece_count)


def varifyPhoneNum(phone_num):

    customer_order_list = customerOrderDAO.select_all()

    valid_phone_num = False

    for order in customer_order_list:
        if order.get_phone_num() == phone_num:
            valid_phone_num = True
            break

    return valid_phone_num
