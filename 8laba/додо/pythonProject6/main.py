import sqlite3

con = sqlite3.connect('labDODO.db')
cursor = con.cursor()

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS Rabotnik(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    f TEXT,
    i TEXT,
    o TEXT,
    doljnost TEXT,
    dtr TEXT,
    adress TEXT,
    phone TEXT)''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS Ingridient(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    nalichie TEXT)''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS Pitsa(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    idINGRIDIENTS INTEGER REFERENCES Ingridient(id),
    price INTEGER)''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS Client(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT)''')

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS Zakaz(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Client_id INTEGER REFERENCES Client(id),
    Pitsa_id INTEGER REFERENCES Pitsa(id),
    kolvo INTEGER,
    itogprice INTEGER,
    datatime TEXT)''')

con.commit()

print('Выберите таблицу для добавления данных:')
print('1 - Rabotnik; 2 - Ingridient; 3 - Pitsa; 4 - Client; 5 - Zakaz')
table_choice = int(input())

if table_choice == 1:
    f = input('Введите фамилию: ')
    i = input('Введите имя: ')
    o = input('Введите отчество: ')
    doljnost = input('Введите должность: ')
    dtr = input('Введите дату трудоустройства: ')
    adress = input('Введите адрес: ')
    phone = input('Введите номер телефона: ')
    cursor.execute('''INSERT INTO Rabotnik(f, i, o, doljnost, dtr, adress, phone) VALUES (?, ?, ?, ?, ?, ?, ?);''',
                   (f, i, o, doljnost, dtr, adress, phone))
elif table_choice == 2:
    name = input('Введите название ингредиента: ')
    description = input('Введите описание: ')
    nalichie = input('Наличие: ')
    cursor.execute('''INSERT INTO Ingridient(name, description, nalichie) VALUES (?, ?, ?);''',
                   (name, description, nalichie))
elif table_choice == 3:
    name = input('Введите название пиццы: ')
    description = input('Введите описание: ')
    id_ingridients = input('Введите id ингредиента: ')
    price = input('Введите цену: ')
    cursor.execute('''INSERT INTO Pitsa(name, description, idINGRIDIENTS, price) VALUES (?, ?, ?, ?);''',
                   (name, description, id_ingridients, price))
elif table_choice == 4:
    name = input('Введите имя клиента: ')
    cursor.execute('''INSERT INTO Client(name) VALUES (?);''', (name,))
elif table_choice == 5:
    client_id = input('Введите id клиента: ')
    pitsa_id = input('Введите id пиццы: ')
    kolvo = input('Введите количество: ')

    # Получаем цену пиццы из таблицы Pitsa по её id
    cursor.execute('''SELECT price FROM Pitsa WHERE id = ?;''', (pitsa_id,))
    price_data = cursor.fetchone()

    if price_data:
        price = float(price_data[0])
        itogprice = int(price) * int(kolvo)
        datatime = input('Введите дату и время: ')
        cursor.execute('''INSERT INTO Zakaz(Client_id, Pitsa_id, kolvo, itogprice, datatime) VALUES (?, ?, ?, ?, ?);''',
                       (client_id, pitsa_id, kolvo, itogprice, datatime))
    else:
        print('Пицца с указанным id не найдена.')
else:
    print('Неверный выбор.')
print('Цена пиццы:', itogprice)
con.commit()
con.close()
