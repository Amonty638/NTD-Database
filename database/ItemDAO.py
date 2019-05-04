from database.Item import Item
from database.Connect import Connect

class ItemDAO(Connect):
    def __init__(self):
        Connect.__init__(self)

    def select_all(self):
        connect = Connect()
        connect.sql_execute('select * from item')
        item_list = []
        for row in connect.cur:
            item = Item()
            item.set_values_from_row(row)
            item_list.append(item)
        return item_list

    def select_by_ntd_num_and_hold_num(self, key, hold_num):
        connect = Connect()
        connect.sql_execute('select * from item where ntd# = ' + "'" + str(key) + "' and hold# = " + "'" + hold_num + "'")
        row = connect.cur.fetchone()
        item = Item()
        item.set_values_from_row(row)
        return item

    def select_by_hold_num(self,key):
        connect = Connect()
        connect.sql_execute('select * from item where hold# = ' + "'" + str(key) + "'")
        item_list = []

        for row in connect.cur:
            item = Item()
            item.set_values_from_row(row)
            item_list.append(item)
        return item_list

    def insert_item(self, itemObject):
        connect = Connect()
        connect.sql_execute('Insert into Item values ( ' + itemObject.get_value_string())
        connect.commit()



    def update(self, itemObject):
        connect = Connect()
        connect.sql_execute("update item set " +
                            "ntd# = '" + itemObject.get_ntd_num() + "'," +
                            "quantity = " + str(itemObject.get_quantity()) + "," +
                            "total_cost = " + str(itemObject.get_total_cost()) + "," +
                            "hold# = '" + itemObject.get_hold_num() + "' " +
                            "where ntd# = '" + itemObject.get_ntd_num() + "' and hold# = '" + itemObject.get_hold_num() + "'")
        connect.commit()

    def delete_item(self, ntd_num, hold_num):
        connect = Connect()
        connect.sql_execute("delete from item where ntd# = " + "'" + ntd_num + "' and hold# = " + "'" + hold_num + "'")
        connect.commit()

    def delete_item_using_hold_num(self, key):
        connect = Connect()
        connect.sql_execute("delete from item where hold# = " + "'" + key + "'")
        connect.commit()

