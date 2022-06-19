class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients
    
    def __repr__(self):
        #ส่งค่าคืนที่สามารถพิมพ์ได้
        return f'Rizza({self.ingredients})'

    @classmethod
    def marherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])
    
    @staticmethod
        #มักใช้เป็น uillity หรือ helper function เพื่อทำให้ code เป็น moduler
    def size(ch):
        ch = ch.upper()
        if ch == 'S':
            return 'small: 6 inches, 4 slices'
        elif ch == 'L':
            return 'Large: 14 inches, 10 slices'
        else:
            return 'Defaulf Medium: 12 inches, 8 slices'
#create instance
my_pizza = Pizza('Cheese, Meat')
print(my_pizza)
print(my_pizza.marherita())

# static method
print('---- Static Method')
print(Pizza.size('L'))

# class method
print('---- Class Method ----')
print(Pizza.marherita())
print(Pizza.prosciutto())
print(my_pizza.marherita())
print(Pizza.ingredients) #cannot access instance instance variale
