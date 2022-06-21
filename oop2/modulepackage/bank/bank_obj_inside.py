#this file is inside bank package
#call modul
from customer import Customer
from account import Account

cus1 = Customer()
cus1.new_customer()

cus1_acc =Account()
cus1_acc.open_account(cus1.name, 'Saving', '141-0434-907',500)
#print(cus1.cus_info())

print("****** Opne Bank Account Detil*******")
print(cus1.cus_info())
print(cus1_acc.display_balance())