#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sqlite3
connection = sqlite3.connect('painting_database.db')
print("Content-type: text/text;Accept-Charset: utf-8")

#print()
cursor = connection.cursor()
cursor.execute("SELECT author FROM authors")
#print("<ol>")
t=""
for elem in cursor.fetchall():
    t=t+elem+" "
print(t)
#print("</ol>")
connection.close()