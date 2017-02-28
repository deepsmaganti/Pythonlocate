def withdraw_amount():
    input_accountno = str(raw_input('Account Number : '))
    input_withdraw = float(raw_input('Withdraw Amount : '))
    f2 = open('accounts.txt','r')
    f2split = f2.readlines()
    line = [i.split(' =', 1)[0] for i in f2split]
    if input_accountno+'.balance' in line:
        linenum = line.index(input_accountno+'.balance')
        old_balance = float(f2split[line.index(input_accountno+'.balance')].split('=')[1])
        new_balance = float(old_balance) - float(input_withdraw)
        if new_balance > 0:
            f2split[linenum] = input_accountno+'.balance = '+str(new_balance)+'\n'
            print "Hello" + f2split[line.index(input_accountno+'.name')].split('=')[1]
            print "Your New Balance is" + f2split[linenum].split('=')[1]
            with open('accounts.txt','w') as f3:
                f3.writelines(f2split)
        else:
            print "Unable to withdraw, requested amount not available in the account."
    else:
        print "Sorry account number is invalid"