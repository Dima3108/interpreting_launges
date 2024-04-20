import sqlite3
connection = sqlite3.connect('painting_database.db')
#. Создать БД в соответствии с предметной областью.
#Вариант 10. Живопись.
#Задание 2. БД должна содержать не менее трех связанных таблиц.
#1 таблица - авторы
#2 таблица - вид картины
#3 таблица - картина , название , автор
cursor = connection.cursor()
#создание 1 таблицы если она не существует
cursor.execute('''
CREATE TABLE IF NOT EXISTS authors(
       id INTEGER PRIMARY KEY,
       author TEXT NOT NULL  UNIQUE              
)
''')
#создание 2 таблицы
cursor.execute('''
CREATE TABLE IF NOT EXISTS type_of_painting(
       id   INTEGER PRIMARY KEY,
       type TEXT  UNIQUE     
)
''')
#создание 3 таблицы   information about the painting
cursor.execute('''
CREATE TABLE IF NOT EXISTS iatp(
      id   INTEGER PRIMARY KEY,
      name TEXT,
      type INTEGER,
      
      authorid INTEGER, 
      FOREIGN KEY (type) REFERENCES type_of_painting(type) ,          
      FOREIGN KEY (authorid)  REFERENCES authors(authorid)   
)
''')
#Задание 3. Заполнить таблицы БД информацией с помощью 
#SQL- запросов.
cursor.execute('SELECT * FROM authors')
if((cursor.fetchall()).__len__()<3):
 cursor.execute('''
 insert into authors(author) VALUES('Иванов')
 ''')
 cursor.execute('''
 insert into authors(author) VALUES('Петров')
 ''')
 cursor.execute('''
 insert into authors(author) VALUES('Сидоров')
 ''')
 connection.commit()
cursor.execute('''
SELECT * FROM type_of_painting
''')
ch="'"
if((cursor.fetchall()).__len__()<3):
  top=['Пейзаж','Натюрморт','Портрет']
  print(top)
  for top_  in top:
    print(top_)
    cursor.execute('''
    insert into type_of_painting(type) VALUES (''' +ch+ str(top_)+ch +''')'''
    )
    connection.commit()
cursor.execute('SELECT * FROM iatp')
auth_id=[0,1,2,1,2]
types=[1,1,2,0,0]
names=['картина1','картина2','картина3','картина4','картина5']
if((cursor.fetchall()).__len__()<len(auth_id)):
  i=0
  while(i<len(names)):
    cursor.execute('''
    insert into iatp(name,type,authorid) VALUES(
    ''' +ch+str(names[i])+ch+','+ch+str(types[i])+ch+','+ch+str(auth_id[i])+ch+
    ')'
    )
    i=i+1  
  connection.commit()
#Задание 4. Написать не менее трех статистических запросов (SELECT)
connection.close()