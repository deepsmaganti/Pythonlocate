def delete_acc():
    input_accountno = str(raw_input('Account Number: '))
    print 'Checking details...'
    f2 = open('accounts.txt', 'r')
    f2split = f2.readlines()
    line = [i.split(' =', 1)[0] for i in f2split]
    if input_accountno + '.name' in line:
        for j in f2split:
            if str(j.split('.')[0]) == str(input_accountno):
                print j
                f2split.remove(j)
        with open('accounts.txt', 'w') as f3:
            f3.writelines(f2split)
    else:
        print ("Sorry account number is invalid")
