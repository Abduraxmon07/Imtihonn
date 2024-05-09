#       1-masala
import psycopg2


conn = psycopg2.connect(database="n42",
                        user="postgres",
                        password="A03072007S",
                        host="localhost",
                        port=5432)

cur = conn.cursor()

create_product_table = """
    create table if not exists product(
        id serial PRIMARY KEY,
        name varchar(100) not null unique,
        price float not null,
        color varchar(20) not null,
        image varchar(25) not null
    );
"""

conn.commit(create_product_table)
cur.close()
conn.close()


#       2-masala
def insert_product():
    insert_into_query = '''insert into product(name, price, color, image) values (%s,%s,%s,%s)'''
    cur.execute(insert_into_query, ('Apple', 12000, 'Red', 'Mazali'))
    conn.commit()

def select_all_products():
    select_product_query = '''select * from product;'''
    cur.execute(select_product_query)
    conn.commit()

def update_product():
    update_query = """update departments set name = %s where id = %s;"""
    cur.execute(update_query, ('Banana', 1))
    conn.commit()

def delete_product():
    delete_query = '''ALTER TABLE products DROP COLUMN image;'''
    cur.execute(delete_query)
    conn.commit()

insert_product()
select_all_products()
update_product()
delete_product()

cur.close()
conn.close()


#       3-masala
class Alphabet:
    def __init__(self) -> None:
        self.harflar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.index = 0
    
    def __next__(self):
        if self.index == 0:
            return self.harflar[self.index]
        elif self.index > 26:
            self.index += 1
            return self.harflar[self.index]
        else:
            return StopIteration
        
a = Alphabet() 

while True:
    try:
        print(a.__next__())
    except StopIteration:
        break


#       4-masala
import time
import threading

def print_numbers():
    for i in range(1,6):
        print(f'First => {i}')
        time.sleep(2)

def print_leters():
    for i in 'ABCDE':
        print(f'Second => {i}')
        time.sleep(2)

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_leters)

thread1.start()
thread2.start()
        

#       5-masala
class Product:
    def __init__(self,
                 id: int | None = None,
                 name: str | None = None,
                 price: float | None = None,
                 color: str | None = None,
                 image: str | None = None):
        self.id = id
        self.name = name
        self.price = price
        self.color = color
        self.image = image

    def save(self):
        insert_into_query = '''insert into product(name,price,color,image) values (%s,%s,%s,%s)'''
        cur.execute(insert_into_query, (self.name, self.price, self.color, self.image))
        conn.commit()

product = Product(1,'BMW', 120000, 'Black', 'Beautiful')
product.save()


#       6-masala
db_params = {
    'host': 'localhost',
    'database': 'n42',
    'user': 'postgres',
    'password': 'A03072007S',
    'port': 5432
}

class DbConnect:
    def __init__(self, db_params):
        self.db_params = db_params

    def __enter__(self):
        self.conn = psycopg2.connect(**self.db_params)
        return self.conn

    def __exit__(self):
        self.conn.commit()
        self.conn.close()

with DbConnect(db_params) as conn:
    with conn.cursor() as cur:
        cur.execute(create_product_table)