def display_acc_holders():
    input_accountno = str(raw_input('Account Number: '))
    print 'Checking details...'
    f2 = open('accounts.txt','r')
    f2split = f2.read().splitlines()
    line = [i.split(' =',1)[0] for i in f2split]
    if input_accountno+'.name' in line:
        print "Hello"+f2split[line.index(input_accountno+'.name')].split('=')[1]
        l = int(f2split[line.index(input_accountno+'.numofacc_h')].split('=')[1])
        for i in range(l):
            print 'Account Holder #'+str(i+1)+' ' + f2split[line.index(input_accountno + '.name'+str(i+1))].split('=')[1]
    else:
        print ("Sorry account number is invalid")