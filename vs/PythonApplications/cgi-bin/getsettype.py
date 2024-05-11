#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print("Content-type: text/html\n")
print()
#file=open("cgi-bin\settype.html","r")
#print(file.read())
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
            <a href="">Добавить картину</a>
        </div>
    </div>
</header>

<body>
    <form method="post" action="settype.py">
        <label for="name">Введите вид(тип) картины</label>
        <input type="text" name="type">
        <button type="submit">Отправить</button>
    </form>
</body>

</html>
''')