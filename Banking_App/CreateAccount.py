import random
acc1 = 0
accountno = str(random.randint(99,9999999999))
def acc_create():
    name = str(raw_input('Enter Name : '))
    address = str(raw_input('Address :'))
    phonenum = str(raw_input('Phone Number :'))
    balance = str(float(0))
    print name, address, phonenum
    confirmation()
    f1 = open("accounts.txt", "a+")
    f1.write(accountno+'.name = '+name+'\n')
    f1.write(accountno+'.address = '+address+'\n')
    f1.write(accountno+'.phonenumber = '+phonenum+'\n')
    f1.write(accountno+'.balance = '+balance+'\n')
    print "Account Created.\n Please note your account number: ", accountno
    acc_holders()

def confirmation():
    confirm = str(raw_input("Is your information correct? Y/N : "))
    if confirm == 'Y' or confirm == 'y' or confirm == 'yes' or confirm == 'Yes':
        print ("Saving your details.")
    elif confirm == 'N' or confirm == 'n' or confirm == 'no' or confirm == 'No':
        print "Enter details again."
        acc_create()
    else:
        print "Invalid input, please try again"
        confirmation()

def acc_holders():
    global acc1
    acc_h = str(raw_input("Would you like to add Account Holders? Y/N"))
    if acc_h == 'Y' or acc_h == 'y' or acc_h == 'yes' or acc_h == 'Yes':
        acc1 += 1
        name_acc_h = str(raw_input("Enter Name of Account Holder"))
        f1 = open("accounts.txt", "a+")
        f1.write(accountno+'.name'+str(acc1)+' = '+ name_acc_h+'\n')
        acc_holders()
    elif acc_h == 'N' or acc_h == 'n' or acc_h == 'no' or acc_h == 'No':
        f1 = open("accounts.txt", "a+")
        f1.write(accountno+'.numofacc_h'+' = '+str(acc1)+'\n')
        print 'Thank You!'
    else:
        print "Invalid input, please try again"
        acc_holders()