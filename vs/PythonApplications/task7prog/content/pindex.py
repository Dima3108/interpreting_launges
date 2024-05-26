
# -*- coding: utf-8 -*-
import sqlite3
import base64


def get_content():
    connection = sqlite3.connect('painting_database.db')
    content=""
    cursor = connection.cursor()
    cursor.execute("SELECT type FROM type_of_painting")

    for elem in cursor.fetchall():
        content=content+"<div>"+str(elem)+"</div>\n"
    content=content+'''
        </div>
      
       </div>
       <div>
        <strong>Авторы:</strong>
        <div id="acontent">
      '''
    #Содержимое бд
    cursor = connection.cursor()
    cursor.execute("SELECT author FROM authors")  
    for elem in cursor.fetchall():
       content=content+"<div>"+str(elem)+"</div>\n"
       #print("<div> %s</div>\n" %(elem))
    content=content+'''
        </div>
         <div>
          <strong>
            Картины
          </strong>
          <div id="imcontent">
'''
    cursor = connection.cursor()
    cursor.execute("SELECT authors.author ,type_of_painting.type,iatp.name  FROM authors,iatp,type_of_painting"+
               " WHERE iatp.type = type_of_painting.id and iatp.authorid = authors.id")
    content=content+'''
    <table style="position: relative;display: flex; justify-content: center;border: 2px solid blue;text-align: center; ">
      <tr style="background-color:blueviolet; font-size:xx-large">
         <th>Название картины</td>
         <th>Вид картины</td>
         <th>Автор картины</td>
      </tr>
'''
    for elem in cursor.fetchall():
    #print(
      content=content+'''
    <tr class="trow">
          <td>'''+str(elem[2])+'''</td>
          <td>'''+str(elem[1])+'''</td>
          <td>'''+str(elem[0])+'''</td>
    </tr>\n
    '''
    content=content+'''
    </table>
      <style>
            .trow {
               font-size: x-large;
               background-color: aquamarine;
               text-align: center;
               
            }
     </style>
'''
    content=content+'''
          </div>
        </div>
       </div>
       
    </main>
</body>
''' 
    connection.close()
    return content

