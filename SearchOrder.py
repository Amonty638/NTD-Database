from database.CustomerOrder import CustomerOrder
from database.CustomerOrderDAO import CustomerOrderDAO
from database.CustomerDAO import CustomerDAO
from database.ItemDAO import ItemDAO
from database.ProductDAO import ProductDAO
import math

customerOrderDAO = CustomerOrderDAO()
customerDAO = CustomerDAO()
itemDAO = ItemDAO()
productDAO = ProductDAO()



def main():

    print("|-------------------------------|")
    print("|  Welcome to the Search Order  |")
    print("|-------------------------------|")
    print("")

    customer_list = customerDAO.select_all()
    customer__order_list = customerOrderDAO.select_all()
    print("Hold Num:" + "            " + "Customer Name:"+ "               " + "Phone#:")
    for order in customer__order_list:
        for customer in customer_list:
            if customer.get_phone() == order.get_phone_num():
                print(order.get_hold_num() + "                " + customer.get_lname() + "," +
                      customer.get_fname()+ "                 " + customer.get_phone())

    while True:

        print("")
        print("Press 1 to view item details associated with a hold#")
        print("Press 2 to view item details associated with a customer phone#")
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

                    valid_hold_num = varifyHoldNum(hold_num,customer__order_list)

                    if valid_hold_num == False:
                        print("The hold# you tried to search by is invalid, please try again")
                        print("")

                    else:
                        order = customerOrderDAO.select_by_hold_number(hold_num)
                        print("Hold Num:" + "            " + "Customer Name:" + "            " +
                              "Date Made:" + "            " + "Delivery Address:" + "            " + "Phone#:")
                        print(order.get_hold_num() + "                "+
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
                                  str(calculatePieceCount(item.get_quantity(),item.get_ntd_num())))

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

                    valid_phone_num = varifyPhoneNum(phone_num, customer__order_list)

                    if valid_phone_num == False:
                        print("The phone# you tried to search by is invalid, please try again")
                        print("")

                    else:
                        orders = customerOrderDAO.select_by_customer_phone(phone_num)
                        print("Hold Num:" + "            " + "Customer Name:" + "            " +
                              "Date Made:" + "            " + "Delivery Address:" + "            " + "Phone#:")

                        for order in orders:
                            print(order.get_hold_num() + "                " +
                                  customerDAO.select_by_phone(order.get_phone_num()).get_lname() + "," +
                                  customerDAO.select_by_phone(order.get_phone_num()).get_fname() + "              " +
                                  order.get_date_made() + "             " +
                                  order.get_delivery_address() + "            "
                                  + order.get_phone_num())

                        print()

                        #items = itemDAO.select_by_hold_num(order.get_hold_num())

                        #print("NTD#:" + "            " + "Quantity:" + "            " + "Total Cost:" +
                              #"            " + "Carton Count:" + "            " + "Piece count:")
                        # for item in items:
                        #     print(item.get_ntd_num() + "             " +
                        #           str(item.get_quantity()) + "                 " + str(item.get_total_cost()) +
                        #           "                   " +
                        #           str(calculateCartonCount(item.get_quantity(), item.get_ntd_num()))
                        #           + "                         " +
                        #           str(calculatePieceCount(item.get_quantity(), item.get_ntd_num())))
                        print("")

                        while True:
                            print("Press 1 to view order")
                            print("Press 2 to quit")

                            choice3 = input()

                            if choice3 == "1":
                                print("Enter Hold#")

                                hold_num = input()

                                valid_hold_num = varifyHoldNum(hold_num, customer__order_list)

                                if valid_hold_num == False:
                                    print("The hold# you tried to search by is invalid, please try again")
                                    print("")

                                else:
                                    order = customerOrderDAO.select_by_hold_number(hold_num)
                                    print("Hold Num:" + "            " + "Customer Name:" + "            " +
                                          "Date Made:" + "            " + "Delivery Address:" + "            " + "Phone#:")
                                    print(order.get_hold_num() + "                " +
                                          customerDAO.select_by_phone(order.get_phone_num()).get_lname() + "," +
                                          customerDAO.select_by_phone(
                                              order.get_phone_num()).get_fname() + "              " +
                                          order.get_date_made() + "             " +
                                          order.get_delivery_address() + "          "
                                          + order.get_phone_num())

                                    print()

                                    items = itemDAO.select_by_hold_num(hold_num)

                                    print("NTD#:" + "                " + "Quantity:" + "                 " +
                                          "Total Cost:" +
                                          "           " + "Carton Count:" + "                " + "Piece count:")
                                    for item in items:
                                        print(item.get_ntd_num() + "                 " +
                                              str(item.get_quantity()) + "                      " + str(
                                            item.get_total_cost()) +
                                              "                   " +
                                              str(calculateCartonCount(item.get_quantity(), item.get_ntd_num()))
                                              + "                          " +
                                              str(calculatePieceCount(item.get_quantity(), item.get_ntd_num())))

                            elif choice3 == "2":
                                break

                            else:
                                print("Invalid entry, please try again")


                elif choice2 == "2":
                    break

                else:
                    print("Invalid entry, please try again")

        elif choice == "9":
            break

        else:
            print("Invalid entry please try again")


def varifyHoldNum(hold_num,customer_order_list):

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


def varifyPhoneNum(phone_num,customer_order_list):

    valid_phone_num = False

    for order in customer_order_list:
        if order.get_phone_num() == phone_num:
            valid_phone_num = True
            break

    return valid_phone_num
