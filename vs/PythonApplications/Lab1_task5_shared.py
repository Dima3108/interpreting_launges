
#Дана строка. Необходимо найти все даты, которые описаны в 
#виде "31 февраля 2007".
import re

def scan(input_str):
    months = ["января", "февраля", "марта", "апреля", "мая", "июня",
              "июля", "августа", "сентября", "октября", "ноября", "декабря"]
    max_len = max(len(month) for month in months)
    result = []
    pos = 0
    month = ""
    success = False
    flag1 = 0
    for char in input_str.lower():
        if pos == 0:
            if char.isdigit():
                cesh = char
                pos = 1
            else:
                pos = 0
                cesh = ""
        else:
            if pos < 3:
                if char == " ":
                    pos = 3
                    success = False
                    cesh += char
                else:
                    if char.isdigit():
                        cesh += char
                        pos = 2
                    else:
                        pos = 0
                        cesh = ""
            else:
                if flag1 == 0:
                    if char != " ":
                        if len(month) <= max_len:
                            cesh += char
                            month += char
                            success = False
                            for m in months:
                                if m.startswith(month):
                                    if len(m) >= len(month):
                                        success = True
                                        break
                            if not success:
                                cesh = ""
                                month = ""
                                pos = 0
                    else:
                        cesh += char
                        flag1 = 1
                else:
                    if char.isdigit():
                        flag1 = 2
                        cesh += char
                    else:
                        if flag1 == 2:
                            result.append(cesh)
                            pos = 0
                            cesh = ""
                            month = ""
                            flag1 = 0
                        else:
                            pos = 0
                            cesh = ""
                            month = ""
                            flag1 = 0
    return result





s='''
"123 asdfgiiIIII  34 февраля 2021 года , 11 мая,   ________________" +
                "\n\n 2 Мая 1998-го года ,,,,,,,,,,," +
                "ууууууууууууууууrrrrYYYYYY11 июня 2011////" +
                "09 июня 2001 года, 11 Апрелят 2000 ------" +
                "111августа 2022 , ЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮЮ" +
                "-1 сентября 2011 года"
'''
r=scan(s)
print(r)