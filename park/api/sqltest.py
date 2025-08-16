import mysql.connector


class Server:
    def __init__ (self):
        self.mydb=mysql.connector.connect(host='localhost',
                                          user='root',
                                          passwd = 'srujanvaidya',
                                          database = 'parking')
        self.mycursor=self.mydb.cursor()
        self.mycursor.execute("use parking")

    def find(self):
        self.mycursor.execute("select * from lot")
        data = self.mycursor.fetchall()
        return data

    def park1 (self,carno,slot):
        self.mycursor.execute("update lot set carno = %s where slot = %s",(carno,slot))
        self.mydb.commit()

    def exit1 (self,k):
        self.mycursor.execute("update lot set carno = %s where slot = %s",("free",k))
        self.mydb.commit()











