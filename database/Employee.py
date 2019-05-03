#!/usr/bin/python

class Employee:
    def __init__ (self):
        self.fname = ""
        self.lname = ""
        self.salesperson_num = ""

    def get_fname(self):
        return self.fname

    def get_lname(self):
        return self.lname


    def get_salesperson_num(self):
        return self.salesperson_num

    def get_dictionary(self):
        return {"First Name": self.get_fname(),
                "Last Name": self.get_lname(),
                "Salesperson #": self.get_salesperson_num()
                }

    def get_values_string(self):
        row = "'"+ self.fname + "' , '" + self.lname + "' , '" + self.salesperson_num + "') "

        return row

    def set_fname(self,value):
        self.fname = str(value)

    def set_lname(self,value):
        self.lname = str(value)

    def set_salesperson_num(self,value):
        self.salesperson_num = str(value)

    def set_values_from_row(self,row):

        try:
            if len(row) < 3:
                raise ValueError("Row does not have enough indices")

            self.set_fname(str(row[0]))
            self.set_lname(str(row[1]))
            self.set_salesperson_num(str(row[2]))

            return True
        except ValueError:
            return False

