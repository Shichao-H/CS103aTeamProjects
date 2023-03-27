import sqlite3
import os

def toDict(t):
    print('t=' + str(t))
    transactions = {'item #':t[0], 'amount':t[1], 'category':t[2], 'date':t[3], 'description':t[4]}
    return transactions

class Transaction():
    def __init__(self):
        '''
        Create a new Transaction table
        '''
        self.run_query('''CREATE TABLE IF NOT EXISTS transactions 
                    (rowid INTEGER PRIMARY KEY AUTOINCREMENT, amount int, category text, date text, description text)''',())

    def quit(self):
        return "hide transactions"

    def show_transaction(self):
        '''
        show current all transactions
        Author: Shichao He
        '''
        return self.run_query("SELECT * FROM transactions",())
    
    def add_transaction(self, item):
        '''
        Add a new Transaction
        Author: Shichao He
        '''
        return self.run_query("INSERT INTO transactions (amount, category, date, description) VALUES (?, ?, ?, ?)",
                             (item['amount'], item['category'], item['date'], item['description']))
                             
    def delete_transaction(self,itemid):
        '''
        delete an exist Transaction
        Author: Shichao He
        '''
        return self.run_query("DELETE FROM transactions WHERE rowid=(?)",(itemid,))
    
    def sum_trans_by_date(self):
        '''
        Summarize all transactions by date
        Author: Shichao He
        '''
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
        '''
        Summarize all transactions by category
        Author: Shichao He
        '''
        return self.run_query("SELECT category, SUM(amount) FROM transactions GROUP BY category",())
    
    def run_query(self, query, tuple):
        '''
        Get results of all the SQL lines in the query
        Author: Shichao He
        '''
        con = sqlite3.connect('transactions.db')
        cur = con.cursor()
        cur.execute(query,tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [toDict(t) for t in tuples]