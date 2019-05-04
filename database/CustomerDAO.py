from database.Customer import Customer
from database.Connect import Connect

class CustomerDAO(Connect):
    def __init__(self):
        Connect.__init__(self)

    def select_all(self):
        connect = Connect()
        connect.sql_execute('select * from customer')
        customer_list = []
        for row in connect.cur:
            customer = Customer()
            customer.set_values_from_row(row)
            customer_list.append(customer)

        return customer_list

    def select_by_phone(self, key):
        connect = Connect()
        connect.sql_execute('select * from customer where phone = \'' + str(key) + '\'')
        row = connect.cur.fetchone()
        customer = Customer()
        customer.set_values_from_row(row)
        return customer

    def insert_customer(self, customerObject):
        connect = Connect()
        connect.sql_execute('Insert into Customer values ( ' + customerObject.get_value_string())
        connect.commit()

    def update(self, customerObject):
        connect = Connect()
        connect.sql_execute("update customer set " +
                            "fname = '" + customerObject.get_fname() + "'," +
                            "lname = '" + customerObject.get_lname() + "'," +
                            "city = '" + customerObject.get_city() + "'," +
                            "zip = '" + customerObject.get_zip() + "'," +
                            "state = '" + customerObject.get_state() + "'," +
                            "email = '" + customerObject.get_email() + "'," +
                            "phone = '" + customerObject.get_phone() + "'," +
                            "street_address = '" + customerObject.get_saddress() + "' "+
                            "where phone = '" + customerObject.get_phone() + "'")
        connect.commit()

    def delete_customer_by_phone_number(self, phone):
        connect = Connect()
        connect.sql_execute('delete from customer where phone = ' + "'" + str(phone) + "'")
        connect.commit()


