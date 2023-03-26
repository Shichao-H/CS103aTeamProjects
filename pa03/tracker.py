from transaction import Transaction
import sys

def print_usage():
    print('''usage:
            quit: quit the program
            show: show transactions
            add: add a transaction (format: amount category YYYY-MM-DD description)
            delete: delete a transaction
            summarize by date: summarize transactions by date 
            summarize by month: summarize transactions by month
            summarize by year: summarize transactions by year
            summarize by category: summarize transactions by category
            print: print this menu
        '''
        )

def print_trans(trans):
    ''' print the transactions '''
    if len(trans)==0:
        print('no transaction to print')
        return
    print('\n')
    print("%-10s %-10s %-30s %-10s"%('item #','amount','category','date','description'))
    print('-'*40)
    for item in trans:
        values = tuple(item.values())
        print("%-10s %-10s %-30s %2d"%values)

def process_args(arglist):
    transaction = Transaction()
    if arglist==[]:
        print_usage()
    elif arglist[0]=="show":
        print_trans(transaction.showTrans())
    elif arglist[0]=="add":
        if len(arglist)!=5:
            print_usage()
        else:
            trans = {'amount':arglist[1],'category':arglist[2],'date':arglist[3],'description':arglist[4]}
            transaction.addTrans(trans)
    elif arglist[0]=="delete":
        if len(arglist)!= 2:
            print_usage()
        else:
            print_trans(transaction.deleteTrans(arglist[1]))
    elif arglist[0]=='summarize':
        if arglist[2]== 'date':
            print_trans(transaction.sumTransbyDate())
        elif arglist[2]=='month':
            print_trans(transaction.sumTransbyMonth())
        elif arglist[2]=='year':
            print_trans(transaction.sumTransbyYear())
        elif arglist[2]=='category':
            print_trans(transaction.sumTransbyCategory())
           
       
def toplevel():
    ''' read the command args and process them'''
    if len(sys.argv)==1:
        print_usage()
        args = []
        while args!=['']:
            args = input("command> ").split(' ')
            if args[0]=='add':
                args = ['add',args[1]," ".join(args[2:])]
            process_args(args)
            print('-'*40+'\n'*3)
    else:
        args = sys.argv[1:]
        process_args(args)
        print('-'*40+'\n'*3)

toplevel()
            
