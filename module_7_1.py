class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return(f'{self.name}, {self.weight}, {self.category}')

class Shop:
    def __init__(self):
        self.__file_name = open('products.txt', 'a')
        self.__file_name.close()

    def get_products(self):
        get_file = open('products.txt', 'r')
        product_name = get_file.read()
        get_file.close()
        return product_name

    def add(self, *products):
        for product in products:
            if str(product) in self.get_products():
                print(f'Продукт {product} уже есть в магазине.')
            else:
                file = open('products.txt', 'a+')
                file.write(f'{str(product)}\n')
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())