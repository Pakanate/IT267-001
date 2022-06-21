from cusorder.customer import Customer
from cusorder.order import Order
#create object of customer
name1  = Customer('Jame', 'Nontaburi')
#create order of customer
order1  = Order('15-06-2022', 'packed')
#display info
print(f'Order of {name1.name} on {order1.date} is {order1.status}')

