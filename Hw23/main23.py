from peewee import *
import datetime
# db = SqliteDatabase('Myshop.sqlite')


class Customer(Model):
    '''Клас модель, для опису таблиці з даними покупця'''
    idCustomer = AutoField(primary_key=True)
    Name = CharField(null=False)
    Surname = CharField(null=False)
    email = CharField(max_length=120)
    Country = CharField(max_length=40)

    class Meta:
        database = SqliteDatabase('Myshop.sqlite3')
        table_name = 'Customer'


class Product(Model):
    '''Клас модель, для опису таблиці з даними про товари'''
    idProduct = AutoField(primary_key=True)
    NameProduct = CharField(null=False)
    Price = IntegerField(null=False)
    Sold = IntegerField(null=False)
    Date_of_Manufacture = DateField()

    class Meta:
        database = SqliteDatabase('Myshop.sqlite3')
        table_name = 'Product'


class ShopAssistant(Model):
    '''Клас модель, для опису таблиці з даними про продавців'''
    idAssistant = AutoField(primary_key=True)
    NameAssistant = CharField(max_length=24, null=False)
    Phone = CharField(max_length=24, null=False)

    class Meta:
        database = SqliteDatabase('myShop.sqlite3')
        table_name = 'ShopAssistant'


class Review(Model):
    '''Клас модель, для опису таблиці з даними про відгуки'''
    Feedback = CharField(max_length=500,null=True)
    Rating = IntegerField(null=True)
    Date = DateField()

    class Meta:
        database = SqliteDatabase('Myshop.sqlite3')
        table_name = 'Review'


Customer.create_table()
Product.create_table()
ShopAssistant.create_table()
Review.create_table()


Customer.insert_many(
    [
        {'Name': 'Галина', 'Surname': 'Маринівна', 'email': 'alone@5a4m32e.com', 'Country': 'Ukrain'},
        {'Name': 'Денис', 'Surname': 'Зайко', 'email': 'byeboy5@4e32mple.com', 'Country': 'Latvia'},
        {'Name': 'Анна', 'Surname': 'Сулейма', 'email': 'suleimansha@e5m4p32.com', 'Country': 'France'},
        {'Name': 'Юлія', 'Surname': 'Бойко', 'email': 'bro@5e432p.com', 'Country': 'Poland'},
        {'Name': 'Олександр', 'Surname': ' Усік', 'email': 'УСІК@022.com', 'Country': 'Ukrain'}
    ]
).execute()

Product.insert_many(
    [
        {'NameProduct': 'Шкаф',
            'Sold': '100', 'Price': '4000', 'Date_of_Manufacture': datetime.date(2023, 5, 20)},
        {'NameProduct': 'Стіл',
            'Sold': '103', 'Price': '5999', 'Date_of_Manufacture': datetime.date(2024, 2, 10)},
        {'NameProduct': 'Двері',
            'Sold': '87', 'Price': '21000', 'Date_of_Manufacture': datetime.date(2009, 1, 21)},
        {'NameProduct': 'Табурет',
            'Sold': '156', 'Price': '729', 'Date_of_Manufacture': datetime.date(2021, 5, 5)},
        {'NameProduct': 'Ліжко',
            'Sold': ' 234', 'Price': '15000', 'Date_of_Manufacture': datetime.date(2022, 8, 18)}]
).execute()


ShopAssistant.insert_many(
    [
        {'Phone': '+420 2 4177 0449'},
        {'Phone': '+420 2 4172 5555'},
        {'Phone': '+1 (650) 253-0000'},
        {'Phone': '+1 (212) 221-3546'},
        {'Phone': '+1 (408) 996-1010'}
    ]
).execute()


Review.insert_many(
    [
        {'Feedback': 'nice'},
        {'Feedback': 'Es ist fantastisch', 'Rating': '100'},
        {'Feedback': 'Аmazing!', 'Rating': '95'},
        {'Feedback': 'Excellent service', 'Rating': '100'},
        {'Rating': '99'}
    ]
).execute()

max_price = Product.select(fn.MAX(Product.Price))
name_product = Product.select().where(Product.Price == max_price).get()

print(f'{name_product.NameProduct} - {name_product.Price}')

popular_product = Product.select(fn.MAX(Product.Sold))
name_product2 = Product.select().where(Product.Sold == popular_product).get()
print(f'{name_product2.NameProduct} - {name_product2.Sold}')

date = Product.select(fn.MAX(Product.Date_of_Manufacture))
name_product3 = Product.select().where(Product.Date_of_Manufacture == date).get()
print(f'{name_product3.NameProduct} - {name_product3.Date_of_Manufacture}')

