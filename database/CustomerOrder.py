#!/usr/bin/python

class CustomerOrder:
    def __init__(self):
        self.date_made = " "
        self.total_cost = " "
        self.description = " "
        self.hold_num = " "
        self.delivery_address = " "
        self.phone_num = " "

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

    def get_phone_num(self):
        return self.phone_num

    def get_value_string(self):
        return "'" + self.date_made + "', " + str(self.total_cost) + ",'" + self.description + "', '" + self.hold_num + "','" + self.delivery_address + "','" + self.phone_num + "')"

    def get_dictionary(self):
        return {"Date made": self.get_date_made(),
                "Total cost": self.get_total_cost(),
                "Description": self.get_description(),
                "Hold#": self.get_hold_num(),
                "Delivery Address": self.get_delivery_address(),
                "Phone#": self.get_phone_num()
                }

    def set_date_made(self,value):
        self.date_made = str(value)

    def set_total_cost(self,value):
        self.total_cost = value

    def set_description(self,value):
        self.description = str(value)

    def set_hold_num(self,value):
        self.hold_num = str(value)

    def set_delivery_address(self, value):
        self.delivery_address = str(value)

    def set_phone_num(self, value):
        self.phone_num = str(value)

    def set_values_from_row(self, row):
        try:
            if len(row) < 6:
                raise ValueError("Row does not have enough indicies")

            self.set_date_made(str(row[0]))
            self.set_total_cost(row[1])
            self.set_description(str(row[2]))
            self.set_hold_num(str(row[3]))
            self.set_delivery_address(str(row[4]))
            self.set_phone_num(str(row[5]))

            return True
        except ValueError:
            return False
