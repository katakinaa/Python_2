import sqlite3


def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as error:
        print(f"Error connecting to database: {error}")
    return connection


conn = create_connection("exam_2.db")


def get_stores():
    try:
        sql = '''
            SELECT store_id, title FROM store
        ''' 
        cursor = conn.cursor()
        cursor.execute(sql)
        store = cursor.fetchall()
        return store
    except sqlite3.Error as error:
        print(error)


def get_products_by_store(store_id):
    try:
        sql = '''
            SELECT products.title, categories.title, products.unit_price, products.stock_quantity
            FROM products
            JOIN store ON products.store_id = store.store_id 
            JOIN categories ON products.category_code = categories.code
            WHERE store.store_id = ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, (store_id,))
        product = cursor.fetchall()
        return product
    except sqlite3.Error as error:
        print(f"Error selecting all products: {error}")


stores = get_stores()
print(
    "Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0: ")
for store in stores:
    print(f"{store[0]} {store[1]}")

while True:
    store_id = int(input("Введите id магазина: "))
    if store_id == 0:
        break
    products = get_products_by_store(store_id)
    if products:
        for product in products:
            print(product)
    else:
        print("В этом магазине нет продуктов.")

conn.close()
