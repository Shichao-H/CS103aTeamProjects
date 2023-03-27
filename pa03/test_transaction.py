import os
import sqlite3
import pytest

from transaction import Transaction

def data():
    '''
    Create the sample data for testing
    Author: Yukun Zhang
    '''
    return [(1, 45, 'book', '2023-03-25', 'scifi novels'), (2, 50, 'clothes', '2022-11-20', 'for winter'), (3, 15, 'pens', '2021-7-11', 'for writing')]

def test_path(dir):
    '''
    Create temporary database for testing.
    Author: Yukun Zhang
    '''
    yield dir / 'test.db'

def db_data(test_path, data):
    '''
    Create and initialize the transaction database in directory.
    Author: Yukun Zhang
    '''
    con = sqlite3.connect(test_path)
    con.execute('''CREATE TABLE IF NOT EXISTS transactions (
        item INTEGER PRIMARY KEY,
        amount REAL,
        category TEXT,
        date TEXT,
        description TEXT
    )''')
    con.executemany('INSERT INTO transactions VALUES (?, ?, ?, ?, ?)', data)
    con.commit()
    transaction = Transaction(test_path)
    yield transaction
    con.execute('DROP TABLE transactions')
    con.commit()

def test_show_trans(transaction, data):
    '''
    Test show_trans method that returns the transaction
    Author: Yukun Zhang
    '''
    assert transaction.show_transaction() == data

def test_add_trans(transaction, data):
    '''
    Test if the add_trans method correctly adds the data
    Author: Yukun Zhang
    '''
    transaction.add_transaction(100.0, 'football', '2022-11-20', 'for sports')
    assert transaction.show_transaction() == data + [(4, 100.0, 'football', '2022-11-20', 'for sports')]

def test_delete_trans(transaction, data):
    '''
    Test that delete_transaction removes a transaction from the database
    Author: Yukun Zhang
    '''
    transaction.delete_transaction(1)
    assert transaction.showTrans() == data[1:]

def test_trans_by_date(transaction, data):
    '''
    Test trans_by_date method that summarizes transactions by date
    Author: Yukun Zhang
    '''
    assert transaction.sum_trans_by_date() == [('2021-7-11', 15.0), ('2022-11-20', 150.0)]
