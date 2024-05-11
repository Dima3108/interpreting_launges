#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
import sqlite3
form = cgi.FieldStorage()  
connection = sqlite3.connect('painting_database.db')
#form = cgi.FieldStorage()  
#connection = sqlite3.connect('painting_database.db')
paintname=str(form.getvalue("pname"))
painttypeid=str(form.getvalue("typeid"))
paintauthorid=str(form.getvalue("authorid"))
print("Content-type: text/html;Accept-Charset: utf-8")
print('''
<!DOCTYPE html>
<html>
    <head lang="ru">
        <meta charset="cp-1251">
    
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
cursor.execute("select * from iatp where iatp.name='%s' and iatp.authorid = '%s' and iatp.type = '%s'" %(paintname,paintauthorid,painttypeid))
stat_=-1
for elem in cursor.fetchall():
    stat_=1
if(stat_==1):
    print("указанный тип (%s:%s:%s) существует!" %(paintname,paintauthorid,painttypeid))
else:
    cursor.execute("insert into iatp(name,type,authorid) VALUES('%s','%s','%s')" %(paintname,paintauthorid,painttypeid))
    print("указанный тип (%s:%s:%s) успешно добавлен" %(paintname,paintauthorid,painttypeid))
    connection.commit()
print('''
       <a href="index.py">На главную</a>
  </body>
</html>
''')
connection.close()