'''
functions tracker can call and use
'''
import sqlite3

def to_dict(transaction):
    '''
    construct new item to table
    '''
    transactions = {'item #':transaction[0], 'amount':transaction[1],
                    'category':transaction[2], 'year':transaction[3],
                    'month':transaction[4],  'day':transaction[5], 'description':transaction[6]}
    return transactions

class Transaction():
    '''
    all functions tracker can call and use
    Author: Xiaoyang Zhang
    '''
    def __init__(self):
        '''Create a new Transaction table
        '''
        self.run_query('''CREATE TABLE IF NOT EXISTS transactions
                    (rowid INTEGER PRIMARY KEY AUTOINCREMENT, amount int, 
                    category text, year int, month int, day int, description text)''',())

    def show_transaction(self):
        '''
        show current all transactions
        Author: Shichao He
        '''
        return self.run_query("SELECT * FROM transactions",())

    def add_transaction(self, item):
        '''
        Add a new Transaction
        Author: Shichao He, Charles Cai, Xiaoyang Zhang
        '''

        splited_date = item['date'].split("-")
        # splite the date from YYYY-MM-DD into a list of [YYYY,MM,DD]

        return self.run_query('''INSERT INTO transactions (amount, category, year, month,
                            day, description) VALUES (?, ?, ?, ?, ?, ?)''',
                             (item['amount'], item['category'], int(splited_date[0]),
                              int(splited_date[1]),
                              int(splited_date[2]), item['description']))
    def delete_transaction(self,itemid):
        '''
        delete an exist Transaction
        Author: Shichao He
        '''
        return self.run_query("DELETE FROM transactions WHERE rowid=(?)",(itemid,))

    def sum_trans_by_date(self):
        '''
        Summarize all transactions by date
        Author: Shichao He, Charles Cai
        '''
        return self.run_query("SELECT * FROM transactions ORDER BY year, month, day, amount ASC",())

    def sum_trans_by_month(self, month):
        '''
        Summarize all the transactions by sum of the months
        Author: Charles Cai
        '''
        return self.run_query("SELECT * FROM transactions WHERE month=(?);", (month,))

    def sum_trans_by_year(self, year):
        '''
        Summarize all the transactions by sum of the years
        Author: Charles Cai
        '''

        return self.run_query("SELECT * FROM transactions WHERE year=(?);", (year,))

    def sum_trans_by_category(self, category):
        '''
        Summarize all transactions by category
        Author: Shichao He, Charles Cai
        '''

        return self.run_query("SELECT * FROM transactions WHERE category=(?);", (category,))

    def run_query(self, query, tran_tuple):
        '''
        Get results of all the SQL lines in the query
        Author: Shichao He
        '''
        con = sqlite3.connect('transactions.db')
        cur = con.cursor()
        cur.execute(query,tran_tuple)
        tuples = cur.fetchall()
        con.commit()
        con.close()
        return [to_dict(t) for t in tuples]
    
