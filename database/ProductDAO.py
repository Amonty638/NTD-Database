from database.Product import Product
from database.Connect import Connect

class ProductDAO(Connect):
    def __init__(self):
        Connect.__init__(self)


    def select_all(self):
        connect = Connect()
        connect.sql_execute('select * from product')
        product_list = []

        for row in connect.cur:
            product = Product()
            product.set_values_from_row(row)
            product_list.append(product)

        return product_list

    def select_by_ntd_num(self,key):
        connect = Connect()
        connect.sql_execute('select * from product where ntd# =  ' + "'" +str(key) + "'")
        row = connect.cur.fetchone()

        product = Product()
        product.set_values_from_row(row)

        return product

    def insert_product(self,product):
        connect = Connect()
        connect.cur.execute('insert into product values( ' + product.get_values_string())
        connect.commit()


    def update(self, product):
        connect = Connect()
        connect.sql_execute("update product set " +
                            "dye_lot = '" + product.get_dye_lot() + "'," +
                            "color = '" + product.get_color() + "'," +
                            "location = '" + product.get_location() + "'," +
                            "mfg# = '" + product.get_mfg_num() + "'," +
                            "buying_price = " + str(product.get_buying_price()) + "," +
                            "amt_in_stock = " + str(product.get_amt_in_stock()) + "," +
                            "ntd_description = '" + product.get_ntd_description() + "' ," +
                            "cost_per_sf = " + str(product.get_cost_per_sf()) + "," +
                            "sf_per_carton = " + str(product.get_sf_per_carton()) + "," +
                            "carton_count = " + str(product.get_carton_count()) + ", " +
                            "size_of_product = " + str(product.get_size_of_product()) + "," +
                            "piece_count = " + str(product.get_piece_count()) + " , " +
                            "ntd# = '" + product.get_ntd_num() + "' " +
                            "where ntd# = '" + product.get_ntd_num() + "'")
        connect.commit()

    def delete_product(self,key):
        connect = Connect()
        connect.cur.execute('delete from product where ntd# = ' + "'" + str(key) + "'")
        connect.commit()



#productDao = ProductDAO()


#
# for item in list:
#     print(item.get_values_string())
#
#
# print(productDao.select_by_ntd_num("N369").get_color())
#
# product = Product()
#
# product.set_dye_lot("test")
# product.set_color("test")
# product.set_location("test")
# product.set_mfg_num("test")
# product.set_buying_price(0)
# product.set_amt_in_stock(0)
# product.set_ntd_description("test")
# product.set_cost_per_sf(0)
# product.set_sf_per_carton(0)
# product.set_carton_count(0)
# product.set_size_of_product(0)
# product.set_piece_count(0)
# product.set_ntd_num("test")
# #
# # print(product.get_values_string())
#productDao.insert_product(product)
#

# temp = productDao.select_by_ntd_num("test")
# temp.set_color("Hello Rick Harrison")
# print(temp.get_color())
# productDao.update(temp)
# list = productDao.select_all()

# productDao.delete_product("test")
# list = productDao.select_all()
# for item in list:
#     print(item.get_values_string())