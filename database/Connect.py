#!/usr/bin/python

import cx_Oracle


class Connect:

    def __init__(self):
        #print("Attempting to connect")
        self.ip = 'stonehillcsc325.cjjvanphib99.us-west-2.rds.amazonaws.com'
        self.port = 1521
        self.SID = 'ORCL'
        self.dsn_tns = cx_Oracle.makedsn(self.ip, self.port, self.SID)
        self.db = cx_Oracle.connect('wdutton', 'csrocks55', self.dsn_tns)
        self.cur = self.db.cursor()

        # self.cur.execute('select * from employee')
        # for result in self.cur:
        #     print(result)
        #
        # self.cur.close()
        # self.db.close()

    def __del__(self):
        self.cur.close()
        self.db.close()

    def insert(self, item):
        pass

    def select(self, key):
        pass

    def update(self, item):
        pass

    def delete(self, item):
        pass

    def sql_execute(self, command):
        self.cur.execute(command)

    def commit(self):
        self.db.commit()





