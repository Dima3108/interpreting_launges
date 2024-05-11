#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
import base64
connection = sqlite3.connect('painting_database.db')
print("Content-type: text/html\n")

print()
print('''
<!DOCTYPE html> 
<html>
    <head>
        <meta charset="cp-1251" lang="ru">
    </head>
    <body>
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
    <main>
        <form method="post" action="setpaint.py">
          <table>
             <tr>
               <th></th>
               <th>Вид картины</th>
               <th>Автор картины<th>
             </tr>
             <tr>
                 <td>
            <label for="pname">Название картины:</label>
             <input type="text" name="pname">
                </td><td>
                   <select name="typeid">
      ''')
    #База данных
cursor = connection.cursor()
cursor.execute("SELECT id,type FROM type_of_painting") 
s='"'  
for elem in cursor.fetchall():
    print("<option value='%s'>%s</option>" %(elem[0],elem[1]))
print(''''
                   </select>
      </td><td>
           <select   name="authorid">
      ''')
    #База данных
cursor = connection.cursor()
cursor.execute("SELECT id,author FROM authors") 
for elem in cursor.fetchall():
    print("<option value='%s'>%s</option>" %(elem[0],elem[1]))
print('''
           </select>
               </td>
               </tr>
             <button type="submit">Отправить</button>
           </table>
        </form>
    </main>
    </body>
</html>
''')