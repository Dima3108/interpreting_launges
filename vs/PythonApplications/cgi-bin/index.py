#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print("Content-type: text/html;Accept-Charset: utf-8")
print()
file=open("cgi-bin\index.html","r")
print(file.read())
