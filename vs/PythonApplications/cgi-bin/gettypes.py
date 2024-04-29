#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
import base64
connection = sqlite3.connect('painting_database.db')
print("Content-type: text/html;Accept-Charset: utf-8;Accept-Language:ru-RU")

print()
cursor = connection.cursor()
cursor.execute("SELECT type FROM type_of_painting")
s="<ol>"
for elem in cursor.fetchall():
    s=s+"\n<li>\n"
    s=s+str(elem)
    s=s+"\n</li>\n"
s=s+"</ol>\n"
en=base64.b64encode(s)
print(en)
#print("<ol>")
#for elem in cursor.fetchall():
    #print("<li>")
    #val=elem
    #print(str(val))
    #print("</li>")
#print("</ol>")
#connection.close()