
#!/usr/bin/env python3
# -*- coding: cp-1251 -*-
import base64
import cgi
import sqlite3
form = cgi.FieldStorage()  
connection = sqlite3.connect('painting_database.db')
aname=str( form.getvalue('name'))
print("Content-type: text/html;")

print('''
<!DOCTYPE html>
<html>
    <head lang="ru">
       <!-- <meta charset="UTF-8">-->
    
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
                <a href="getsetpaint.py">Добавить картину</a>
            </div>
        </div>
    </header>
    <body>
''')
cursor = connection.cursor()
cursor.execute("select id from authors where authors.author='%s'" %aname)
stat_=-1
for elem in cursor.fetchall():
    stat_=1
#stat_=1
if(stat_==1):
    print("указанный (%s)  автор существует!" %aname)
else:
    cursor.execute("insert into authors(author) VALUES('%s')" %aname)
    print("указанный (%s) автор успешно добавлен" %aname)
    connection.commit()
print('''
      <a href="index.py">На главную</a>
  </body>
</html>
''')
connection.close()