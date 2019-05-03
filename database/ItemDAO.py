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

    def insert_item(self, itemObject):
        connect = Connect()
        print("Insert into Item values (" + itemObject.get_value_string())
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


#TESTING STUFF
# item_dao = ItemDAO()
#
# item = Item()
#
# item.set_ntd_num("N369")
# item.set_quantity(420.00)
# item.set_total_cost(6969.69)
# item.set_hold_num("17101")
#
# #item_dao.insert_item(item)
# print("just did the insert")
# stuff = item_dao.select_all()
# for things in stuff:
#     print(things.get_dictionary())
#
# item.set_quantity(400.00)
# item_dao.update(item)
# print("\n\njust did the update")
# stuff = item_dao.select_all()
# for things in stuff:
#     print(things.get_dictionary())
#
# print("\n\nTesting select")
# print(item_dao.select("N365", "18095").get_dictionary())
#
#
# item_dao.delete_item("N369", "17101")
# print("\n\nafter deletion")
# stuff = item_dao.select_all()
# for things in stuff:
#     print(things.get_dictionary())