#!/usr/bin/python

class Item:
    def __init__(self,ntd_num,quantity,total_cost,hold_num):
        self.ntd_num = ntd_num
        self.quantity = quantity
        self.total_cost = total_cost
        self.hold_num = hold_num

    def get_ntd_num(self):
        return self.ntd_num

    def get_quantity(self):
        return self.quantity

    def get_total_cost(self):
        return self.total_cost

    def get_hold_num(self):
        return self.hold_num

    def get_dictionary(self):
        return {"NTD #":self.get_ntd_num(),
                "Quantity": self.get_quantity(),
                "Total cost": self.get_total_cost(),
                "Hold#": self.get_hold_num()
                }

    def set_ntd_num(self,value):
        self.ntd_num = str(value)

    def set_quantity(self,value):
        self.quantity = value

    def set_total_cost(self,value):
        self.total_cost = value

    def set_hold_num(self,value):
        self.hold_num = value
