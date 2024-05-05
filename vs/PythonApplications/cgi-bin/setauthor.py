
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
import sqlite3
form = cgi.FieldStorage()  
connection = sqlite3.connect('painting_database.db')
aname=str(form.getvalue('name'))
print("Content-type: text/html;Accept-Charset: utf-8")
print('''
<!DOCTYPE html>
<html>
    <head lang="ru">
        <meta charset="UTF-8">
    
    </head>
    <header>
    
        <div>
            <div>Задание 6</div>
            <div>
                <a href="getsetauthor.py">Добавить автора</a>
    
            </div>
            <div>
                <a href="getsettype.py">Добавть тип картины</a>
            </div>
            <div>
                <a href="">Добавить картину</a>
            </div>
        </div>
    </header>
    <body>
''')
cursor = connection.cursor()
cursor.execute("select id from authors where authors.author={aname}")
stat_=-1
for elem in cursor.fetchall():
    stat_=1
if(stat_==1):
    print("указанный автор существует!")
else:
    cursor.execute("insert into authors(author) VALUES({aname})")
    print("указанный автор успешно добавлен")
    connection.commit()
print('''
  </body>
</html>
''')
connection.close()