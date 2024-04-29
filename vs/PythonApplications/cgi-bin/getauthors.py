#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
connection = sqlite3.connect('painting_database.db')
print("Content-type: text/html;Accept-Charset: utf-8;Accept-Language:ru-RU")

print()
cursor = connection.cursor()
cursor.execute("SELECT author FROM authors")
print("<ol>")
for elem in cursor.fetchall():
    print("<li>")
    print(str(elem))
    print("</li>")
print("</ol>")
connection.close()