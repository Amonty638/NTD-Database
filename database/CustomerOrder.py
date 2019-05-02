#!/usr/bin/python

class CustomerOrder:
    def __init__(self,date_made,total_cost,description,hold_num,delivery_address):
        self.date_made = date_made
        self.total_cost = total_cost
        self.description = description
        self.hold_num = hold_num
        self.delivery_address = delivery_address

    def get_date_made(self):
        return self.date_made

    def get_total_cost(self):
        return self.total_cost

    def get_description(self):
        return self.description()

    def get_hold_num(self):
        return self.hold_num()

    def get_delivery_address(self):
        return self.delivery_address()

    def get_dictionary(self):
        return {"Date made": self.get_date_made(),
                "Total cost": self.get_total_cost(),
                "Description": self.get_description(),
                "Hold#": self.get_hold_num(),
                "Delivery Address": self.get_delivery_address()
                }

    def set_date_made(self,value):
        self.date_made = str(value)

    def set_total_cost(self,value):
        self.total_cost = value

    def set_description(self,value):
        self.description = str(value)

    def set_hold_num(self,value):
        self.hold_num = value

    def set_delivery_address(self, value):
        self.delivery_address = str(value)
