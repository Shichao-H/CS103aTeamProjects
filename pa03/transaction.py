import sqlite3
import os

def toDict(t):
    print('t=' + str(t))
    transactions = {'item #':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description':t[4]}
    return transactions

class Transaction():
    def __init__(self):
        self.run_query('''CREATE TABLE IF NOT EXISTS transactions 
                    (rowid INTEGER PRIMARY KEY AUTOINCREMENT, amount int, category text, date text, description text)''',())

    def quit(self):
        return "hide transactions"

    def show_transaction(self):
        return self.run_query("SELECT * FROM transactions",())
    
    def add_transaction(self, item):
        return self.run_query("INSERT INTO transactions (amount, category, date, description) VALUES (?, ?, ?, ?)",
                             (item['amount'], item['category'], item['date'], item['description']))
                             
    def delete_transaction(self,itemid):
        return self.run_query("DELETE FROM transactions WHERE rowid=(?)",(itemid,))
    
    def sum_trans_by_date(self):
        return self.run_query("SELECT date, SUM(amount) FROM transaction GROUP BY date",())
    
    def sum_Trans_by_month(self):
        '''
        Summarize all the transactions by sum of the months
        Author: Charles Cai
        '''

        return self.run_query('''
        SELECT strftime("%Y-%M", date) AS month, SUM(amount) AS sum 
        FROM transactions 
        GROUP BY month
        ORDER BY month DESC''',())

    def sum_trans_by_year(self):
        '''
        Summarize all the transactions by sum of the years
        Author: Charles Cai
        '''

        return self.run_query('''
        SELECT strftime("%Y", date) AS year, SUM(amount) AS sum 
        FROM transactions 
        GROUP BY year
        ORDER BY year DESC''',())

    def sum_trans_by_category(self):
        return self.run_query("SELECT category, SUM(amount) FROM transactions GROUP BY category",())
    
    def run_query(self, query, tuple):
        con = sqlite3.connect('transactions.db')
        cur = con.cursor()
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]
