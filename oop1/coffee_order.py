class CoffeeOrder:
    def __init__(self,meun_type:str, total:float, customer_name: str, menu: str, num: int, size: str, prie:float) -> None:
        self.meun_type = 'Coffee'
        self.total = 0
        self.customer_name 
        self.menu = menu
        self.num 
        self.size
        self.price

    def check_menu(self, menu):
        meun_dictionary ={'CM':5.99,'CP':4.99,'AM':4.99,'CL':4.99,'VL':4.75,'ES':3.00}:
        if menu == 'CM':
            return d['CM']
        elif menu == 'CP':
            return d['CP']
        elif menu == 'AM':
            return d['AM']:
        elif menu == 'CL':
            return d['CL']
        elif menu == 'VL':
            return ['VL']
        elif menu == 'ES':
            return ['ES']
    def compute_price(size):
        size = size.upper
        if size == 'L':
            price = price + 1
        elif size == 'XL':
            price = price + 1.5

    def display_detal(self):
        print(f'{customer_name}, {menu} ({num}{size}* ${price})-> ${total}')

if __name__ == '__main__':
    john