import sqlite3


def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as error:
        print(f"Error connecting to database: {error}")
    return connection


conn = create_connection("hw_8.db")


def get_cities():
    try:
        sql = '''
            SELECT id, title FROM cities
        '''
        cursor = conn.cursor()
        cursor.execute(sql)
        cities = cursor.fetchall()
        return cities
    except sqlite3.Error as error:
        print(error)


def get_students_by_city(city_id):
    try:
        sql = '''
            SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area
            FROM students
            JOIN cities ON students.city_id = cities.id
            JOIN countries ON cities.country_id = countries.id
            WHERE cities.id = ?
        '''
        cursor = conn.cursor()
        cursor.execute(sql, (city_id,))
        students = cursor.fetchall()
        return students
    except sqlite3.Error as error:
        print(f"Error selecting all products: {error}")


cities = get_cities()
print("id городов, для выхода из программы введите 0:")
for city in cities:
    print(f"{city[0]} {city[1]}")

while True:
    city_id = int(input("Введите id города: "))
    if city_id == 0:
        break
    students = get_students_by_city(city_id)
    if students:
        for student in students:
            print(student)
    else:
        print("В этом городе нет учеников.")


conn.close()


