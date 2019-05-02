#!/usr/bin/python

class Product:
    def __init__(self,dye_lot,color,location,mfg_num,buying_price,amt_in_stock,ntd_description,cost_per_sf,sf_per_carton,carton_count,size_of_product,piece_count,ntd_num):
        self.dye_lot = dye_lot
        self.color = color
        self.location = location
        self.mfg_num = mfg_num
        self.buying_price = buying_price
        self.amt_in_stock = amt_in_stock
        self.ntd_description = ntd_description
        self.cost_per_sf = cost_per_sf
        self.sf_per_carton = sf_per_carton
        self.carton_count = carton_count
        self.size_of_product = size_of_product
        self.piece_count = piece_count
        self.ntd_num = ntd_num

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
        return self.amt_in_stock()

    def get_ntd_description(self):
        return self.ntd_description()

    def get_cost_per_sf(self):
        return self.cost_per_sf()

    def get_sf_per_carton(self):
        return self.sf_per_carton

    def get_carton_count(self):
        return self.carton_count

    def get_size_of_product(self):
        return self.size_of_product

    def get_piece_count(self):
        return self.piece_count

    def get_ntd_num(self):
        return self.ntd_numd

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

    def carton_count(self,value):
        self.carton_count = value

    def set_size_of_product(self,value):
        self.size_of_product = value

    def set_piece_count(self,value):
        self.piece_count = value

    def ntd_num(self,value):
        self.ntd_num = str(value)
