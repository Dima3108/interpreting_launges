#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cgi
import sqlite3
form = cgi.FieldStorage()  
connection = sqlite3.connect('painting_database.db')
#form = cgi.FieldStorage()  
#connection = sqlite3.connect('painting_database.db')
paintname=str(form.getvalue("pname"))
painttypeid=int(form.getvalue("typeid"))
paintauthorid=int(form.getvalue("authorid"))
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
ch="'"
names=paintname
types=painttypeid
auth_id=paintauthorid
cursor.execute("select * from iatp where iatp.name= '"+str(names)+"' and iatp.type = '"+str(types)+"' and iatp.authorid = '"+str(auth_id)+"'")
stat_=-1
for elem in cursor.fetchall():
    stat_=1
if(stat_==1):
    print("указанный тип ("+paintname+":"+paintauthorid+":"+painttypeid+") существует!" %(paintname,paintauthorid,painttypeid))
else:
    s='''insert into iatp(name,type,authorid) VALUES('''+"'"+str(names)+ch+','+ch+str(types)+ch+','+ch+str(auth_id)+ch+')'
    print(s)
    cursor.execute(s)
    connection.commit()
    #cursor.execute("insert into iatp(name,type,authorid) VALUES("+paintname+","+painttypeid+","+paintauthorid+")" )
    print("указанный тип ("+str(paintname)+":"+str(paintauthorid)+":"+str(painttypeid)+") успешно добавлен" )
    #connection.commit()
print('''
       <a href="index.py">На главную</a>
  </body>
</html>
''')
connection.close()