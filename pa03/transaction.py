import sqlite3
import os

def toDict(t):
    print('t=' + str(t))
    transaction = {'item #':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description':t[4]}
    return transaction

def Transaction():
    def __init__(self):
        self.runQuery('''CREATE TABLE IF NOT EXISTS transaction 
                    (item # text, amount int, category text, date text, description text)''',())

    def showTrans(self):
        return self.runQuery("SELECT * FROM transaction",())
    
    def addTrans(self, item):
        return self.runQuery("INSERT INTO transaction (?,?,?,?)",(item['amount'], item['category'], item['date]'], item['description']))
                             
    def deleteTrans(self,itemid):
        return self.runQuery("DELETE FROM transaction WHERE item # = (?)",(itemid,))
    
    def sumTransbyDate(self):
        return self.runQuery("SELECT date, SUM(amount) FROM transaction GROUP BY date",())
    
    def sumTransbyMonth(self):
        '''
        Summarize all the transactions by sum of the months
        Author: Charles Cai
        '''

        return self.runQuery('''
        SELECT strftime("%Y-%M", date) AS month, SUM(amount) AS sum 
        FROM transaction 
        GROUP BY month
        ORDER BY month DESC''',())

    def sumTransbyYear(self):
        '''
        Summarize all the transactions by sum of the years
        Author: Charles Cai
        '''

        return self.runQuery('''
        SELECT strftime("%Y", date) AS year, SUM(amount) AS sum 
        FROM transaction 
        GROUP BY year
        ORDER BY year DESC''',())

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