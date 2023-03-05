import sqlite3
import os
import time
import os
import psycopg2


class DB_Manager:
    def __init__(self):
        self.conn = psycopg2.connect(os.environ["DATABASE_URL"])


    # record table creation
    def TableCreation(self):
        self.conn.execute('''CREATE TABLE ITEM
                (ID         INTEGER     PRIMARY KEY     AUTOINCREMENT,
                Name        TEXT        UNIQUE          NOT NULL,
                Price       INTEGER     NOT NULL,
                Description TEXT                        NOT NULL);''')
        print("ITEM Record table created successfully")

        self.conn.execute('''CREATE TABLE ORDERS
                (Order_ID       INTEGER     NOT NULL,
                Item_ID         INTEGER     NOT NULL,
                User_ID         INTEGER     NOT NULL,
                Table_Number    INTEGER     UNIQUE      NOT NULL,
                Order_Status    INTEGER     NOT NULL,
                Number          INTEGER     NOT NULL);''')
                
        print("ORDERS Record table created successfully")

       

    # Query all

    def QuarryAllItem(self):
        SUB = self.SqlQuarryExec("""select ID,Name,Price,Description
                                from ITEM;""")
        return ([[s[0] for s in SUB], [s[1] for s in SUB], [s[2] for s in SUB], [s[3] for s in SUB]])

    def QuarryItemPrice(self):
        SUB = self.SqlQuarryExec("""select Price
                                from Item;""")
        return ([s[0] for s in SUB])

    def QuarryItemDescriptiom(self):
        SUB = self.SqlQuarryExec("""select Description
                                from ITEM;""")
        return ([s[0] for s in SUB])

    def QuarryAllOrder(self):
        SUB = self.SqlQuarryExec("""select Order_ID,Item_ID,User_ID,Table_Number,Order_Status,Number
                                from ORDERS
                                order by ID asc;""")
        return ([[s[0] for s in SUB], [s[1] for s in SUB], [s[2] for s in SUB], [s[3] for s in SUB], [s[4] for s in SUB], [s[5] for s in SUB]])

    def QuarryOrderByUser_ID(self, ID):
        SUB = self.SqlQuarryExec("""select Order_ID,Item_ID,User_ID,Table_Number,Order_Status,Number
                                from ORDERS
                                where User_ID={0};""".format(ID))
        return ([[s[0] for s in SUB], [s[1] for s in SUB], [s[2] for s in SUB], [s[3] for s in SUB], [s[4] for s in SUB], [s[5] for s in SUB]])
   
 # adding to Record table

    def AddItem(self, Name, Price, Description):
        try:
            self.conn.execute("INSERT INTO ITEM (Name, Price, Description) VALUES (\"{0}\",{1},\"{2}\")".format(
                Name, Price, Description))
            self.Commit()
        except:
            self.conn.rollback()

    def AddOrder(self, Order_ID, Item_ID, User_ID, Table_Number, Order_Status,number):
        try:
            self.conn.execute("INSERT INTO ORDERS (Order_ID,Item_ID,User_ID,Table_Number,Order_Status,Number) VALUES ({0}, {1},{2},{3},{4},{5})".format(
                Order_ID,Item_ID,User_ID,Table_Number,Order_Status,number))
            self.Commit()
        except:
            self.conn.rollback()

    # removing from table

    def RemoveItembyItem_ID(self, Item_ID):
        try:
            self.conn.execute("DELETE from ITEM where Item_ID={0}".format(Item_ID))
            self.Commit()
        except:
            self.conn.rollback()

    def RemoveOrderbyItem_ID(self, ID):
        try:
            self.conn.execute(
                "DELETE from ORDERS where Order_ID={0}".format(ID))
            self.Commit()
        except:
            self.conn.rollback()

    def RemoveOrderbyUser_ID(self, ID):
        try:
            self.conn.execute(
                "DELETE from ORDERS where User_ID={0}".format(ID))
            self.Commit()
        except:
            self.conn.rollback()     

    def updateOrderNumber(self, Order_ID, number, Item_ID):
        try:
            self.conn.execute(
                "UPDATE ORDERS set Number={0} where Order_ID={1} and Item_ID={2}".format(number, Order_ID, Item_ID))
            self.Commit()
        except:
            self.conn.rollback()
    # Misc

    def SqlQuarryExec(self, quarry):
        c = self.conn.cursor()
        c.execute(quarry)
        return (c.fetchall())

    def Commit(self):
        self.conn.commit()

    # def DropTable(self, table):
    #     stm = "DROP TABLE {0};".format(table)
    #     self.SqlQuarryExec(stm)
    #     self.Commit()

if __name__=="__main__":
    DB_Manager().TableCreation()