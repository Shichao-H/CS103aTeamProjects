'''
tracker of this app
'''
import sys
from transaction import Transaction

def print_usage():
    '''
    print all command line arguments
    '''
    print('''usage:
            quit: quit the program
            show: show transactions
            add "amount" "category" "YYYY-MM-DD" "description": add a transaction
            delete itemID: delete a transaction
            sum by date: summarize transactions by date 
            sum by month MM: summarize transactions by month
            sum by year YYYY: summarize transactions by year
            sum by category XXX: summarize transactions by category
            help: print this menu
        '''
        )

def print_trans(trans):
    ''' print the transactions 
        Author: Xiaoyang Zhang
    '''
    if len(trans)==0:
        print('no transaction to print')
        return
    print('\n')
    #print("%-7s %-7s %-10s %-7s %-30s"%('item #','amount','category','date','description'))
    print(f"{'item #':<7} {'amount':<7} {'category':<10} {'date':<7} {'description':<30}")
    print('-'*50)
    for item in trans:
        date = str(item['year']) + "-" + str(item['month']) + "-" + str(item['day'])
        values = (item['item #'], item['amount'], item['category'], date, item['description'])
        print(f"{values[0]}\t{values[1]}\t{values[2]}\t{values[3]}\t{values[4]}\t")

def process_args(arglist):
    '''process user's request
    '''
    transaction = Transaction()
    if arglist==[]:
        print_usage()
    elif arglist[0]=="help":
        print_usage()
    elif arglist[0]=="show":
        print_trans(transaction.show_transaction())
    elif arglist[0]=="add":
        if len(arglist)!=5:
            print_usage()
        else:
            trans = {'amount':arglist[1],'category':arglist[2],
                     'date':arglist[3], 'description':arglist[4]}
            transaction.add_transaction(trans)
    elif arglist[0]=="delete":
        if len(arglist)!= 2:
            print_usage()
        else:
            transaction.delete_transaction(arglist[1])
    elif arglist[0]=='sum':
        if arglist[2]== 'date':
            print_trans(transaction.sum_trans_by_date())
        elif arglist[2]=='month':
            print_trans(transaction.sum_trans_by_month(arglist[3]))
        elif arglist[2]=='year':
            print_trans(transaction.sum_trans_by_year(arglist[3]))
        elif arglist[2]=='category':
            print_trans(transaction.sum_trans_by_category(arglist[3]))
    elif arglist[0]=='quit':
        sys.exit()

def toplevel():
    ''' read the command args and process them
        Author: Xiaoyang Zhang
    '''
    if len(sys.argv)==1:
        print_usage()
        args = []
        while args!=['']:
            args = input("command> ").split(' ')
            if args[0]=='add':
                args = ['add',args[1],args[2],args[3],args[4]]
            process_args(args)
            print('-'*50+'\n'*3)
    else:
        args = sys.argv[1:]
        process_args(args)
        print('-'*60+'\n'*3)

toplevel()
