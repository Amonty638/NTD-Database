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
        #print(customerObject.get_value_string())
        connect = Connect()
        #print("Insert into Customer values (" + customerObject.get_value_string())
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



#TESTING SHIT
# CustomerDao = CustomerDAO()
#
# newCustomer = Customer()
# newCustomer.set_fname("Donkey")
# newCustomer.set_lname("Test")
# newCustomer.set_city("Neverland")
# newCustomer.set_email("donkey@yahoo.com")
# newCustomer.set_phone("9788862538")
# newCustomer.set_saddress("12 tilton boo")
# newCustomer.set_state("Massachusetts")
# newCustomer.set_zip("01810")
#
# #print(newCustomer.get_value_string())
# CustomerDao.insert_customer(newCustomer)
#
# newCustomer.set_zip("11111")
# CustomerDao.update(newCustomer)
# CustomerDao.delete_customer("9788862538")
# list = CustomerDao.select_all()
# for item in list:
#     print(item.get_zip())
# print(CustomerDao.select_by_phone("555-555-5555").get_fname())


