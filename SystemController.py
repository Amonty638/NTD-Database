import ManageEmployee
import ManageInventory
import ManageCustomerOrder
import CreateOrder
import ManageCustomers
from colorama import Fore, Back, Style


def main():

    print("|--------------------------------------------------------------|")
    print("|  Welcome to the National Tile Distributors Inventory System  |")
    print("|--------------------------------------------------------------|")
    print("")
    while True:

        print("Please enter the password to login (cap sensitive)")

        password = input()

        if password == "tony":
            index()
            break

        else:
            print("Password incorrect")


def index():


    while True:
        print("|------------------------|")
        print("|  Welcome to the Index  |")
        print("|------------------------|")
        print("")
        print("Press 1 to create an order")
        print("Press 2 to manage an order")
        print("Press 3 to manage inventory")
        print("Press 4 to manage Employees")
        print("Press 5 to manage customers")
        print("Press 6 to log out")

        choice = input()

        if choice == "1":
            CreateOrder.main()

        elif choice == "2":
            ManageCustomerOrder.main()

        elif choice == "3":
            ManageInventory.main()

        elif choice == "4":
            ManageEmployee.main()

        elif choice == "5":
            ManageCustomers.main()

        elif choice == "6":
            print("GoodBye!")
            break

        else:
            print("Invalid choice please try again")
            print("")


main()
