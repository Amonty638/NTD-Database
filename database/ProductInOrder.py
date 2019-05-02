#!/usr/bin/python

class ProductInOrder:
    def __init__(self,cost,amount_of_product,ntd_num,date_made,total_cost,description,hold_num,delivery_address,salesperson_num,customer_phone):
        self.cost = cost
        self.amount_of_product = amount_of_product
        self.ntd_num = ntd_num
        self.date_made = date_made
        self.total_cost = total_cost
        self.description = description
        self.hold_num = hold_num
        self.delivery_address = delivery_address
        self.salesperson_num = salesperson_num
        self.customer_phone = customer_phone

    def get_cost(self):
        return self.cost

    def get_amount_of_product(self):
        return self.amount_of_product

    def get_ntd_num(self):
        return self.ntd_num

    def get_date_made(self):
        return self.date_made

    def get_total_cost(self):
        return self.total_cost

    def get_description(self):
        return self.description

    def get_hold_num(self):
        return self.hold_num

    def get_delivery_address(self):
        return self.delivery_address

    def get_salesperson_num(self):
        return self.salesperson_num

    def get_customer_phone(self):
        return self.customer_phone


    def get_dictionary(self):
        return {"Cost": self.get_cost(),
                "Amount of Product": self.get_amount_of_product(),
                "NTD#": self.get_ntd_num(),
                "Date Made": self.get_date_made(),
                "Total Cost": self.get_total_cost(),
                "Description": self.get_description(),
                "Hold#": self.get_hold_num(),
                "Delivery Address": self.get_delivery_address(),
                "Salesperson#": self.get_salesperson_num(),
                "Customer Phone": self.get_customer_phone()
                }

    def set_cost(self,value):
        self.cost = value

    def set_amount_of_product(self,value):
        self.amount_of_product = value

    def set_ntd_num(self,value):
        self.ntd_num = str(value)

    def set_date_made(self,value):
        self.date_made = str(value)

    def set_total_cost(self, value):
        self.total_cost = value

    def set_description(self,value):
        self.description = str(value)

    def set_hold_num(self,value):
        self.hold_num = value

    def set_delivery_address(self,value):
        self.delivery_address = str(value)

    def set_salesperson_num(self,value):
        self.salesperson_num = value

    def set_customer_phone(self, value):
        self.customer_phone = str(value)