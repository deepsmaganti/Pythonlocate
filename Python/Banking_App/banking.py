import CreateAccount
import CheckBalance
import Delete
import Deposit
import DisplayAH
import WithdrawCash

userinput = int(raw_input(
    "Welcome to ABC bank!!\n"
    "What would you like to do today?\n"
    "1: Create a new Account\n"
    "2: Check Balance\n"
    "3: Withdraw Cash\n"
    "4: Make a Deposit\n"
    "5: Display all Account Holders\n"
    "6: Delete your account\n"
    "Enter your choice as number: "))

if userinput == 1:
    CreateAccount.acc_create()
elif userinput == 2:
    CheckBalance.check_balance()
elif userinput == 3:
    WithdrawCash.withdraw_amount()
elif userinput == 4:
    Deposit.deposit_amount()
elif userinput == 5:
    DisplayAH.display_acc_holders()
elif userinput == 6:
    do = Delete.delete_acc()
else:
    print "Invalid option please choose from the options above"
