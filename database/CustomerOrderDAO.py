from database.CustomerOrder import CustomerOrder
from database.Connect import Connect

class CustomerOrderDAO(Connect):
    def __init__(self):
        Connect.__init__(self)

    def select_all(self):
        connect = Connect()
        connect.sql_execute('select * from customer_order')
        customer_order_list = []
        for row in connect.cur:
            customer_order = CustomerOrder()
            customer_order.set_values_from_row(row)
            customer_order_list.append(customer_order)
        return customer_order_list

    def select_by_hold_number(self, key):
        connect = Connect()
        connect.sql_execute('select * from customer_order where hold# = ' + "'" + str(key) + "'")
        row = connect.cur.fetchone()
        customer_order = CustomerOrder()
        customer_order.set_values_from_row(row)
        return customer_order

    def select_by_customer_phone(self,key):
        connect = Connect()
        connect.sql_execute('select * from customer_order where phone# = ' + "'" + str(key) + "'")
        customer_order_list = []
        for row in connect.cur:
            customer_order = CustomerOrder()
            customer_order.set_values_from_row(row)
            customer_order_list.append(customer_order)
        return customer_order_list

    def insert_customer_order(self, customerOrderObject):
        connect = Connect()
        print("Insert into  customer_order values (" + customerOrderObject.get_value_string())
        connect.sql_execute('Insert into customer_order values ( ' + customerOrderObject.get_value_string())
        connect.commit()



    def update(self, customerOrderObject):
        connect = Connect()
        connect.sql_execute("update customer_order set " +
                            "date_made = '" + customerOrderObject.get_date_made() + "'," +
                            "total_cost = " + str(customerOrderObject.get_total_cost()) + "," +
                            "hold# = '" + customerOrderObject.get_hold_num() + "', " +
                            "delivery_address = '" + customerOrderObject.get_delivery_address() + "', " +
                            "phone# = '" + customerOrderObject.get_phone_num() + "' " +
                            "where hold# = '" + customerOrderObject.get_hold_num() + "'")
        connect.commit()

    def delete_customer_order_by_hold_num(self, hold_num):
        connect = Connect()
        connect.sql_execute("delete from customer_order where hold# = " + "'" + hold_num + "'")
        connect.commit()


#TESTING STUFF
# custorder = CustomerOrder()
#custorder_dao = CustomerOrderDAO()
# custorder.set_phone_num("123-123-1234")
# custorder.set_delivery_address("330 Main street north reading ma")
# custorder.set_description("Kitchen")
# custorder.set_hold_num("98765")
# custorder.set_total_cost(0.00)
# custorder.set_date_made("5/3/19")
#
# custorder_dao.insert_customer_order(custorder)
# stuff = custorder_dao.select_all()
# print("Just inserted: ")
# for things in stuff:
#     print(things.get_dictionary())
#
# custorder.set_total_cost(10.00)
# custorder_dao.update(custorder)
#
# print("\n\n After updateing total cost")
# stuff = custorder_dao.select_all()
# print("Just inserted: ")
# for things in stuff:
#     print(things.get_dictionary())
#
# print("\n\n Doing a select ")
# print(custorder_dao.select("98765").get_dictionary())
#
# print("\n\n Doing a delete ")
# custorder_dao.delete_customer_order("98765")
# stuff = custorder_dao.select_all()
# for things in stuff:
#     print(things.get_dictionary())


# orders = custorder_dao.select_by_customer_phone("123-123-1234")
#
# for item in orders:
#     print(item.get_dictionary())

