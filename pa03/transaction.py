import sqlite3
import os

def toDict(t):
    print('t=' + str(t))
    transaction = {'item #':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description':t[4]}
    return transaction

def Transaction():
    def __init__(self):
        self.runQuery('''CREATE TABLE IF NOT EXISTS transaction 
                    (amount int, category text, date text, description text)''',())

    def quit(self):
        return "hide transaction"

    def showTrans(self):
        return self.runQuery("SELECT * FROM transaction",())
    
    def addTrans(self, item):
        return self.runQuery("INSERT INTO transaction (?,?,?,?)",(item['amount'], item['category'], item['date]'], item['description']))
                             
    def deleteTrans(self,itemid):
        return self.runQuery("DELETE FROM transaction WHERE item # = (?)",(itemid,))
    
    def sumTransbyDate(self):
        return self.runQuery("SELECT date, SUM(amount) FROM transaction GROUP BY date",())
    
    def sumTransbyMonth(self):

    def sumTransbyYear(self):

    def sumTransbyCategory(self):
        return self.runQuery("SELECT category, SUM(amount) FROM transaction GROUP BY category",())
    
    def runQuery(self, query, tuple):
        con = sqlite3.connect(os.getenv('HOME') + '/transaction.db')
        cur = con.cursor()
        cur.excute(query, tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]