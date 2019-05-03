#!/usr/bin/python

class Item:
    def __init__(self):
        self.ntd_num = " "
        self.quantity = " "
        self.total_cost = " "
        self.hold_num = " "

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

    def get_value_string(self):
        value = "'" + self.ntd_num + "', " + str(self.quantity) + ", " + str(self.total_cost) + ", '" + self.hold_num + "')"
        return value

    def set_ntd_num(self,value):
        self.ntd_num = str(value)

    def set_quantity(self,value):
        self.quantity = value

    def set_total_cost(self,value):
        self.total_cost = value

    def set_hold_num(self,value):
        self.hold_num = value

    def set_values_from_row(self, row):
        try:
            if len(row) < 4:
                raise ValueError("Row does not have enough indicies")

            self.set_ntd_num(str(row[0]))
            self.set_quantity(row[1])
            self.set_total_cost(row[2])
            self.set_hold_num(str(row[3]))

            return True
        except ValueError:
            return False
