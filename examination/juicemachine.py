class JuiceOrder:
    def __init__(self,menu:str,size:str='R') ->None:
        self.menu = menu.upper()
        self.size = size.upper()
        self.price = 0

    def check_menu(self):
        menu_dictionary = {
            'OJ':25,
            'AJ':25,
            'WJ':30,
            'PJ':30
        }
        if self.menu in menu_dictionary:
            self.price = menu_dictionary.get(self.menu)

    def compute_price(self):
        if self.size == 'L':
            self.price += 5
        else:
            self.price
        JuiceOrder.total = self.menu * self.price
    def display_order(self):
        self.check_menu()
        self.compute_price()
        return f'{self.check_menu}, {self.compute_price}'

    def __del__(self):
        print("Object was destroyed")
if __name__=="__main__":
    order1 = JuiceOrder("WJ")
    print(order1.display_order())
    