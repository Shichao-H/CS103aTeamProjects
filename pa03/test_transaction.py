'''
This is the test for transaction method
'''
from transaction import Transaction

def test_add_transaction():
    '''
    Test if the add_transaction method correctly adds the data
    Author: Yukun Zhang
    '''
    test_data = Transaction()
    t_1 = {'amount': 45, 'category': 'book', 'date': '2023-3-25', 'description': 'novels'}
    t_2 = {'amount': 50, 'category': 'clothes', 'date': '2022-11-20', 'description': 'winter'}
    t_3 = {'amount': 15, 'category': 'pens', 'date': '2023-11-11', 'description': 'writing'}
    test_data.add_transaction(t_1)
    test_data.add_transaction(t_2)
    test_data.add_transaction(t_3)
    assert test_data.show_transaction() == [{'item #': 1, 'amount': 45, 'category': 'book'
    , 'year': 2023, 'month': 3, 'day': 25, 'description': 'novels'}
    , {'item #': 2, 'amount': 50, 'category': 'clothes', 'year': 2022, 'month': 11, 'day': 20
    , 'description': 'winter'}
    , {'item #': 3, 'amount': 15, 'category': 'pens', 'year': 2023, 'month': 11, 'day': 11
    , 'description': 'writing'}]

def test_delete_transaction():
    '''
    Test if delete_transaction correctly removes a transaction from the database
    Author: Yukun Zhang
    '''
    test_data = Transaction()
    test_data.delete_transaction(1)
    assert test_data.show_transaction() == [{'item #': 2, 'amount': 50, 'category': 'clothes'
    , 'year': 2022, 'month': 11, 'day': 20, 'description': 'winter'}
    , {'item #': 3, 'amount': 15, 'category': 'pens', 'year': 2023, 'month': 11, 'day': 11
    , 'description': 'writing'}]

def test_sum_trans_by_date():
    '''
    Test sum_trans_by_date method that summarizes transactions by date
    Author: Yukun Zhang
    '''
    test_data = Transaction()
    t_1 = {'amount': 45, 'category': 'book', 'date': '2023-3-25', 'description': 'novels'}
    test_data.add_transaction(t_1)
    assert test_data.sum_trans_by_date() == [{'item #': 2, 'amount': 50, 'category': 'clothes'
    , 'year': 2022, 'month': 11, 'day': 20, 'description': 'winter'}
    , {'item #': 4, 'amount': 45, 'category': 'book', 'year': 2023, 'month': 3, 'day': 25
    , 'description': 'novels'}
    , {'item #': 3, 'amount': 15, 'category': 'pens', 'year': 2023, 'month': 11, 'day': 11
    , 'description': 'writing'}]

def test_sum_trans_by_month():
    '''
    Test sum_trans_by_month method that summarizes transactions by month
    Author: Yukun Zhang
    '''
    test_data = Transaction()
    assert test_data.sum_trans_by_month(11) == [{'item #': 2, 'amount': 50, 'category': 'clothes'
    , 'year': 2022, 'month': 11, 'day': 20, 'description': 'winter'}
    , {'item #': 3, 'amount': 15, 'category': 'pens', 'year': 2023, 'month': 11, 'day': 11
    , 'description': 'writing'}]

def test_sum_trans_by_year():
    '''
    Test sum_trans_by_year method that summarizes transactions by year
    Author: Yukun Zhang
    '''
    test_data = Transaction()
    assert test_data.sum_trans_by_year(2023) == [{'item #': 3, 'amount': 15, 'category': 'pens'
    , 'year': 2023, 'month': 11, 'day': 11, 'description': 'writing'}
    , {'item #': 4, 'amount': 45, 'category': 'book', 'year': 2023, 'month': 3, 'day': 25
    , 'description': 'novels'}]

def test_sum_trans_by_category():
    '''
    Test sum_trans_by_category method that summarizes transactions by category
    Author: Yukun Zhang
    '''
    test_data = Transaction()
    t_1 = {'amount': 90, 'category': 'clothes', 'date': '2021-7-13', 'description': 'summer'}
    test_data.add_transaction(t_1)
    assert test_data.sum_trans_by_category('clothes') == [{'item #': 2, 'amount': 50
    , 'category': 'clothes', 'year': 2022, 'month': 11, 'day': 20, 'description': 'winter'}
    , {'item #': 5, 'amount': 90, 'category': 'clothes', 'year': 2021, 'month': 7, 'day': 13
    , 'description': 'summer'}]
