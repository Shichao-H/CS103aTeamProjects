# CS103aTeamProjects
This is the github repository for team 31. It contains the code written for PA03 from COSI-103A class.

This program allows users to add their recent transactions with details including amount, data, type, and description. And user can choose to display their transactions in various ways including by date, month, year and category,


## Result of running pylint

```
PS C:\Users\Lenovo\Desktop\CS103aTeamProjects\pa03> pylint tracker.py         
************* Module tracker
tracker.py:40:0: R0912: Too many branches (15/12) (too-many-branches)

------------------------------------------------------------------
Your code has been rated at 9.82/10 (previous run: 8.95/10, +0.88)

PS C:\Users\Lenovo\Desktop\CS103aTeamProjects\pa03> pylint transaction.py
************* Module transaction
transaction.py:94:0: C0303: Trailing whitespace (trailing-whitespace)

------------------------------------------------------------------
Your code has been rated at 9.67/10 (previous run: 4.00/10, +5.67)

PS C:\Users\Lenovo\Desktop\CS103aTeamProjects\pa03> pylint test_transaction.py

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

## Result of running pytest
```
================================================================== 6 passed in 0.09s ================================================================== 
PS C:\Users\Lenovo\Desktop\CS103aTeamProjects\pa03> pytest -v                 
================================================================= test session starts =================================================================
platform win32 -- Python 3.11.2, pytest-7.2.2, pluggy-1.0.0 -- C:\Users\Lenovo\AppData\Local\Programs\Python\Python311\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Lenovo\Desktop\CS103aTeamProjects\pa03
collected 6 items

test_transaction.py::test_add_transaction PASSED                                                                                                 [ 16%]
test_transaction.py::test_delete_transaction PASSED                                                                                              [ 33%]
test_transaction.py::test_sum_trans_by_date PASSED                                                                                               [ 50%]
test_transaction.py::test_sum_trans_by_month PASSED                                                                                              [ 66%]
test_transaction.py::test_sum_trans_by_year PASSED                                                                                               [ 83%]
test_transaction.py::test_sum_trans_by_category PASSED                                                                                           [100%]

================================================================== 6 passed in 0.08s ==================================================================
```


## Running tracker.py and demonstrate all features
```
PS C:\Users\Lenovo\Desktop\CS103aTeamProjects\pa03> python tracker.py
usage:
            quit: quit the program
            show: show transactions
            add "amount" "category" "YYYY-MM-DD" "description": add a transaction
            delete itemID: delete a transaction
            sum by date: summarize transactions by date
            sum by month MM: summarize transactions by month
            sum by year YYYY: summarize transactions by year
            sum by category XXX: summarize transactions by category
            help: print this menu

command> add 30 food 2023-03-20 lunch
--------------------------------------------------



command> add 40 food 2023-03-21 dinner
--------------------------------------------------



command> add 25 travel 2022-11-30 uber 
--------------------------------------------------



command> add 65 travel 2023-02-28 train
--------------------------------------------------



command> show


item #  amount  category   date    description
--------------------------------------------------
1       30      food    2023-3-20       lunch
2       40      food    2023-3-21       dinner
3       25      travel  2022-11-30      uber
4       65      travel  2023-2-28       train
--------------------------------------------------



command> sum by date 


item #  amount  category   date    description
--------------------------------------------------
3       25      travel  2022-11-30      uber
4       65      travel  2023-2-28       train
1       30      food    2023-3-20       lunch
2       40      food    2023-3-21       dinner
--------------------------------------------------



command> sum by month 03


item #  amount  category   date    description
--------------------------------------------------
1       30      food    2023-3-20       lunch
2       40      food    2023-3-21       dinner
--------------------------------------------------



command> sum by year 2023


item #  amount  category   date    description
--------------------------------------------------
1       30      food    2023-3-20       lunch
2       40      food    2023-3-21       dinner
4       65      travel  2023-2-28       train
--------------------------------------------------



command> sum by category travel


item #  amount  category   date    description
--------------------------------------------------
3       25      travel  2022-11-30      uber
4       65      travel  2023-2-28       train
--------------------------------------------------



command> sum by category food


item #  amount  category   date    description
--------------------------------------------------
1       30      food    2023-3-20       lunch
2       40      food    2023-3-21       dinner
--------------------------------------------------



command> delete 4
--------------------------------------------------



command> show


item #  amount  category   date    description
--------------------------------------------------
1       30      food    2023-3-20       lunch
2       40      food    2023-3-21       dinner
3       25      travel  2022-11-30      uber
--------------------------------------------------



command> help
usage:
            quit: quit the program
            show: show transactions
            add "amount" "category" "YYYY-MM-DD" "description": add a transaction
            delete itemID: delete a transaction
            sum by date: summarize transactions by date
            sum by month MM: summarize transactions by month
            sum by year YYYY: summarize transactions by year
            sum by category XXX: summarize transactions by category
            help: print this menu

--------------------------------------------------
```
