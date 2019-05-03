#!/usr/bin/python

class Product:
    def __init__(self):
        self.dye_lot = ""
        self.color = ""
        self.location = ""
        self.mfg_num = ""
        self.buying_price = 0
        self.amt_in_stock = 0
        self.ntd_description = ""
        self.cost_per_sf = 0
        self.sf_per_carton = 0
        self.carton_count = 0
        self.size_of_product = 0
        self.piece_count = 0
        self.ntd_num = ""

    def get_dye_lot(self):
        return self.dye_lot

    def get_color(self):
        return self.color

    def get_location(self):
        return self.location

    def get_mfg_num(self):
        return self.mfg_num

    def get_buying_price(self):
        return self.buying_price

    def get_amt_in_stock(self):
        return self.amt_in_stock

    def get_ntd_description(self):
        return self.ntd_description

    def get_cost_per_sf(self):
        return self.cost_per_sf

    def get_sf_per_carton(self):
        return self.sf_per_carton

    def get_carton_count(self):
        return self.carton_count

    def get_size_of_product(self):
        return self.size_of_product

    def get_piece_count(self):
        return self.piece_count

    def get_ntd_num(self):
        return self.ntd_num

    def get_dictionary(self):
        return {"Dye Lot": self.get_dye_lot(),
                "Color": self.get_color(),
                "Location": self.get_location(),
                "MFG#": self.get_mfg_num(),
                "Buying Price": self.get_buying_price(),
                "Amount in Stock ": self.get_amt_in_stock(),
                "NTD Description": self.get_ntd_description(),
                "Cost per square foot": self.get_cost_per_sf(),
                "Square foot per carton": self.get_sf_per_carton(),
                "Carton count": self.get_carton_count(),
                "Size of product": self.get_size_of_product(),
                "Piece count": self.get_piece_count(),
                "NTD#": self.get_ntd_num()
                }

    def get_values_string(self):
        row = "'"+ self.dye_lot + "' , '" + self.color + "' , '" + self.location + "' , '"+  self.mfg_num+ "', '" + \
              str(self.buying_price) + "' ,'" + str(self.amt_in_stock) + "' ,'" + self.ntd_description + "' , '" + str(self.cost_per_sf) \
              +"', '" + str(self.sf_per_carton) + "' ,'" + str(self.carton_count) + "' , '"+ str(self.size_of_product) + "' ,'" + \
              str(self.piece_count) + "' ,'" + self.ntd_num + "') "

        return row

    def set_dye_lot(self,value):
        self.dye_lot = str(value)

    def set_color(self,value):
        self.color = str(value)

    def set_location(self,value):
        self.location = str(value)

    def set_mfg_num(self,value):
        self.mfg_num = str(value)

    def set_buying_price(self,value):
        self.buying_price = value

    def set_amt_in_stock(self,value):
        self.amt_in_stock = value

    def set_ntd_description(self,value):
        self.ntd_description = str(value)

    def set_cost_per_sf(self,value):
        self.cost_per_sf = value

    def set_sf_per_carton(self,value):
        self.sf_per_carton = value

    def set_carton_count(self,value):
        self.carton_count = value

    def set_size_of_product(self,value):
        self.size_of_product = value

    def set_piece_count(self,value):
        self.piece_count = value

    def set_ntd_num(self,value):
        self.ntd_num = str(value)

    def set_values_from_row(self,row):

        try:
            if len(row) < 13:
                raise ValueError("Row does not have enough indices")

            self.set_dye_lot(str(row[0]))
            self.set_color(str(row[1]))
            self.set_location(str(row[2]))
            self.set_mfg_num(str(row[3]))
            self.set_buying_price(row[4])
            self.set_amt_in_stock(row[5])
            self.set_ntd_description(str(row[6]))
            self.set_cost_per_sf(row[7])
            self.set_sf_per_carton(row[8])
            self.set_carton_count(row[9])
            self.set_size_of_product(row[10])
            self.set_piece_count(row[11])
            self.set_ntd_num(str(row[12]))

            return True
        except ValueError:
            return False
