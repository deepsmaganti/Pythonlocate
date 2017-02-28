def check_balance():
    input_accountno = str(raw_input('Account Number: '))
    print 'Checking details...'
    f2 = open('accounts.txt','r')
    f2split = f2.read().splitlines()
    line = [i.split(' =',1)[0] for i in f2split]
    if input_accountno+'.balance' in line:
        print "Hello"+f2split[line.index(input_accountno+'.name')].split('=')[1]
        print "Your Balance is"+f2split[line.index(input_accountno+'.balance')].split('=')[1]
    else:
        print ("Sorry account number is invalid")