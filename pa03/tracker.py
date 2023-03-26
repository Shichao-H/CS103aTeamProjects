from transaction import Transaction
import sys

def print_usage():
    print('''usage:
            transaction quit
            transaction show transactions
            transaction add
            transaction delete
            transaction summarize by date
            transaction summarize by month
            transaction summarize by year
            transaction summarize by category
            transaction print
        '''
        )

def print_trans(trans):

def process_args(arglist):
    transaction = Transaction()
    if arglist==[]:
        print_usage()
    elif arglist[0]=="show":
        print_trans(transaction.showTrans())
    elif arglist[0]=="add":
        if len(arglist)!=3:
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
        
        elif arglist[2]=='month':
        
        elif arglist[2]=='year':
            
