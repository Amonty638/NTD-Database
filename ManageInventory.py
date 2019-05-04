from database.Product import Product
from database.ProductDAO import ProductDAO

def add_inventory():
    print("|----------------------------|")
    print("|        Add Inventory       |")
    print("|----------------------------|")
    print("")
    product = Product()
    product_dao = ProductDAO()
    list_of_products = product_dao.select_all()


    found = True
    while found:
        print("Enter NTD#")
        ntd_num = input()
        for thing in list_of_products:
            if ntd_num == thing.get_ntd_num():
                found = False
        if not found:
            found = True
            print("NTD# already in database")
        else:
            product.set_ntd_num(ntd_num)
            break

    print("Enter dye lot")
    product.set_dye_lot(input())

    print("Enter color")
    product.set_color(input())

    print("Enter location in warehouse (example A-1-2)")
    product.set_location(input())

    print("Enter manufacturing number")
    product.set_mfg_num(input())

    print("Enter buying price")
    product.set_buying_price(input())

    print("Enter description of product")
    product.set_ntd_description(input())

    print("Enter cost per square foot")
    product.set_cost_per_sf(input())

    print("Enter square feet per carton")
    product.set_sf_per_carton(input())

    print("Enter cartons in stock")
    product.set_carton_count(input())

    print("Enter square footage per piece of product")
    product.set_size_of_product(input())

    print("Enter number of pieces in stock")
    product.set_piece_count(input())

    amt_in_stock = float(product.get_sf_per_carton()) * float(product.get_carton_count())
    amt_in_stock = amt_in_stock + (float(product.get_size_of_product()) * float(product.get_piece_count()))
    product.set_amt_in_stock(amt_in_stock)

    product_dao.insert_product(product)




def edit_inventory():
    print("|----------------------------|")
    print("|        Edit Inventory      |")
    print("|----------------------------|")
    print("")

    product_dao = ProductDAO()
    list_of_products = product_dao.select_all()
    found = True
    ntd_num = 0
    while found:
        print("Enter NTD# to find the product you wish to edit")
        ntd_num = input()
        for prod in list_of_products:
            if ntd_num == prod.get_ntd_num():
                found = False

        if found == False:
            break

    product = product_dao.select_by_ntd_num(ntd_num)
    while True:
        print("Press 1 to change description\n"
              "Press 2 to change dye lot\n"
              "Press 3 to change color\n"
              "Press 4 to change location in warehouse\n"
              "Press 5 to change manufacturing number\n"
              "Press 6 to change buying price\n"
              "Press 7 to change square footage in stock\n"
              "Press 8 to change cost per square foot\n"
              "Press 9 to change square footage in a carton\n"
              "Press 10 to change number of cartons in stock\n"
              "Press 11 to change size of product in square feet\n"
              "Press 12 to change number of pieces in stock\n"
              "Press 13 to return back to inventory manager")

        choice = input()
        print(product.get_dictionary())
        if choice == "1":
            print("Enter description of product")
            product.set_ntd_description(input())
            product_dao.update(product)

        if choice == "2":
            print("Enter dye lot")
            product.set_dye_lot(input())
            product_dao.update(product)

        if choice == "3":
            print("Enter color")
            product.set_color(input())
            product_dao.update(product)

        if choice == "4":
            print("Enter location in warehouse (example A-1-2)")
            product.set_location(input())
            product_dao.update(product)

        if choice == "5":
            print("Enter manufacturing number")
            product.set_mfg_num(input())
            product_dao.update(product)

        if choice == "6":
            print("Enter buying price")
            product.set_buying_price(input())
            product_dao.update(product)

        if choice == "7":
            print("Enter square footage in stock")
            newSquareFootage = input()
            newCartonCount = int(float(newSquareFootage) / float(product.get_sf_per_carton()))
            newPieceCount = int((float(newSquareFootage) % float(product.get_sf_per_carton())) / float(product.get_size_of_product()))
            product.set_amt_in_stock(str(newSquareFootage))
            product.set_carton_count(str(newCartonCount))
            product.set_piece_count(str(newPieceCount))
            product_dao.update(product)

        if choice == "8":
            print("Enter cost per square foot")
            product.set_cost_per_sf(input())
            product_dao.update(product)

        if choice == "9":
            print("Enter square feet per carton")
            newSquareFeetPerCarton = input()
            newAmountInWarehouse = float(newSquareFeetPerCarton) * float(product.get_carton_count())
            newAmountInWarehouse = float(newAmountInWarehouse) + (float(product.get_piece_count()) * float(product.get_size_of_product()))
            product.set_amt_in_stock(str(newAmountInWarehouse))
            product.set_sf_per_carton(str(newSquareFeetPerCarton))
            product_dao.update(product)

        if choice == "10":
            print("Enter cartons in stock")
            newCartonCount = input()
            newAmountInWarehouse = float(newCartonCount) * float(product.get_sf_per_carton())
            newAmountInWarehouse = float(newAmountInWarehouse) + (float(product.get_piece_count()) + float(product.get_size_of_product()))
            product.set_amt_in_stock(str(newAmountInWarehouse))
            product.set_carton_count(str(newCartonCount))
            product_dao.update(product)

        if choice == "11":
            print("Enter square footage per piece of product")
            newSizeOfProduct = input()
            newAmountInWarehouse = float(product.get_sf_per_carton()) * float(product.get_carton_count())
            newAmountInWarehouse = float(newAmountInWarehouse) + (float(product.get_piece_count()) * float(newSizeOfProduct))
            product.set_amt_in_stock(str(newAmountInWarehouse))
            product.set_size_of_product(str(newSizeOfProduct))
            product_dao.update(product)

        if choice == "12":
            print("Enter number of pieces in stock")
            newNumberPieces = input()
            newAmountInWarehouse = float(product.get_sf_per_carton()) * float(product.get_sf_per_carton())
            newAmountInWarehouse = float(newAmountInWarehouse) + (float(product.get_size_of_product()) * float(newNumberPieces))
            product.set_amt_in_stock(str(newAmountInWarehouse))
            product.set_piece_count(str(newNumberPieces))
            product_dao.update(product)

        if choice == "13":
            break









def delete_inventory():
    print("|----------------------------|")
    print("|      Delete Inventory      |")
    print("|----------------------------|")
    print("")
    product_dao = ProductDAO()
    product_list = product_dao.select_all()
    found = False
    while not found:
        print("Enter hold# to delete product\n"
              "Enter 0 to go back to inventory screen ")
        choice = input()
        if(choice == "0"):
            break
        for product in product_list:
            if product.get_ntd_num() == choice:
                found = True

        if found == True:
            product_dao.delete_product(choice)
            break



def view_inventory():
    product_dao = ProductDAO()
    product_list = product_dao.select_all()
    for product in product_list:
        print(product.get_ntd_num())
        print(product.get_dictionary())
        print("-------------------------------------------------------------------------------------------------------"
              "-------------------------------------------------------------------------------------------------------"
              "--------------------------------------------------------------------------------------------------------"
              "-----------------------------------------------------------------------------------------------------\n")

def main():
    while True:
        print("|----------------------------|")
        print("|          Inventory         |")
        print("|----------------------------|")
        print("")

        print("Press 1 to add inventory")
        print("Press 2 to edit inventory")
        print("Press 3 to delete inventory")
        print("Press 4 to view inventory")
        print("Press 9 to return to index")
        choice = input()
        if(choice == "1"):
            add_inventory()

        if(choice == "2"):
            edit_inventory()

        if(choice == "3"):
            delete_inventory()

        if(choice == "4"):
            view_inventory()

        if(choice == "9"):
            break

