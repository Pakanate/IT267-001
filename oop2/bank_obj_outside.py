#this file is inside bank package
#call modul
#from customer import Customer
#from account import Account
#from bank import customer,account
#from bank import customer,account
#cus1 = customer.Customer()
#cus1_acc = account.Account

#from bank.customer import Customer
#from bank.account import Account

from bank.customer import Customer
from bank.account import Account
cus1 = customer.Customer()
cus1.new_customer()

cus1_acc = account.Account()
cus1_acc.open_account(cus1.name, 'Saving', '141-0434-907',500)
#print(cus1.cus_info())

print("****** Opne Bank Account Detil*******")
print(cus1.cus_info())
print(cus1_acc.display_balance())