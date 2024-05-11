#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
import base64
connection = sqlite3.connect('painting_database.db')
print("Content-type: text/html\n")
print()
print('''
<!DOCTYPE html>
<body>
  <head lang="ru" >
    <!--<meta charset="UTF-8">-->

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
    <main>
       <div>
        <strong>Виды:</strong>
        <div id="content">
      ''')
#Содержимое БД
cursor = connection.cursor()
cursor.execute("SELECT type FROM type_of_painting")
#s="<ol>"
for elem in cursor.fetchall():
    print("<div> %s</div>\n" %(elem))
    #s=s+"\n<li>\n"
    #s=s+str(elem)
    #s=s+"\n</li>\n"
#s=s+"</ol>\n"
#print(s)
print('''
        </div>
      
       </div>
       <div>
        <strong>Авторы:</strong>
        <div id="acontent">
      ''')
#Содержимое бд
cursor = connection.cursor()
cursor.execute("SELECT author FROM authors")
#print("<ol>")
#t=""
for elem in cursor.fetchall():
    print("<div> %s</div>\n" %(elem))

print('''
        </div>
         <div>
          <strong>
            Картины
          </strong>
          <div id="imcontent">
''')
cursor = connection.cursor()
cursor.execute("SELECT authors.author ,type_of_painting.type,iatp.name  FROM authors,iatp,type_of_painting"+
               " WHERE iatp.type = type_of_painting.id and iatp.authorid = authors.id")
print('''
    <table style="position: relative;display: flex; justify-content: center;border: 2px solid blue;text-align: center; ">
      <tr style="background-color:blueviolet; font-size:xx-large">
         <th>Название картины</td>
         <th>Вид картины</td>
         <th>Автор картины</td>
      </tr>
''')
for elem in cursor.fetchall():
    print('''
    <tr class="trow">
          <td>%s</td>
          <td>%s</td>
          <td>%s</td>
    </tr>
    ''' %(elem[2],elem[1],elem[0]))
print('''
    </table>
      <style>
            .trow {
               font-size: x-large;
               background-color: aquamarine;
               text-align: center;
               
            }
     </style>
''')
print('''
          </div>
        </div>
       </div>
       
    </main>
</body>
''')
#file=open("cgi-bin\index.html","r")
#print(file.read())
connection.close()