#!/usr/bin/python

class Customer:
    def __init__(self,fname,lname,city,zip,state,email,phone,saddress):
       self.fname = fname
       self.lname = lname
       self.city = city
       self.zip = zip
       self.state = state
       self.email = email
       self.phone = phone
       self.saddress = saddress


    def get_fname(self):
        return self.fname

    def get_lname(self):
        return self.lname

    def get_city(self):
        return self.city

    def get_zip(self):
        return self.zip

    def get_state(self):
        return self.state

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

    def get_saddress(self):
        return self.saddress

    def get_dictionary(self):
        return {"First Name": self.get_fname(),
                "Last Name": self.get_lname(),
                "City": self.get_city(),
                "Zip": self.get_zip(),
                "State": self.get_state(),
                "Email": self.get_email(),
                "Phone": self.get_phone(),
                "Street Address": self.get_saddress()
                }

    def set_fname(self,value):
        self.fname = str(value)

    def set_lname(self,value):
        self.lname = str(value)

    def set_city(self,value):
        self.city = str(value)

    def set_zip(self,value):
        self.zip = str(value)

    def set_state(self,value):
        self.state = str(value)

    def set_email(self,value):
        self.email = str(value)

    def set_phone(self,value):
        self.phone = str(value)

    def set_saddress(self,value):
        self.saddress = str(value)

    def set_values_from_row(self,row):

        try:
            if len(row) < 8:
                raise ValueError("Row does not have enough indicies")

            self.set_fname(str(row[0]))
            self.set_lname(str(row[1]))
            self.set_city(str(row[2]))
            self.set_zip(str(row[3]))
            self.set_state(str(row[4]))
            self.set_email(str(row[5]))
            self.set_phone(str(row[6]))
            self.set_saddress(str(row[7]))

            return True
        except ValueError:
            return False

