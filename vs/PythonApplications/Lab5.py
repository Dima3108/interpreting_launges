'''
Реализовать функцию, которая будет проверять, является ли 
введенная строка доменом из URL-адреса, возвращаемое значение True или 
False. Дополнительно реализовать функцию, которая выбрасывает исключение 
о некорректном аргументе, иначе возвращает домен из URL-адреса.
Доменные имена для протоколов http и https, с необязательным слешем 
в конце. Специальные символы не используются.
Примеры:
http://example.com/ – да
example.com – нет
кремль.рф – нет :(
'''

import re

def checking_string_validity_(url, domain_=None):
    start_val = "http"
    domain_ = ""
    if url is None or len(url) <= len(start_val):
        return (False,domain_)
    tmp = ""
    http_no_secure = "http:"
    http_secure = "https:"
    domain = ""
    last_point_position = 0
    pos = 0
    flag1 = 0
    flag2 = 0
    flag3 = 0
    domain_zone = ""
    the_rest_of_the_way = ""
    for c in url.lower():
        if pos < len(start_val):
            tmp += c
            pos += 1
        elif c != '/' and flag1 == 0:
            if c != 's' and c != ':':
                return (False,domain_)
            else:
                tmp += c
                pos += 1
                if c == ':':
                    if tmp != http_no_secure and tmp != http_secure:
                        return (False,domain_)
        else:
            tmp += c
            pos += 1
            if c == '/' and flag1 == 0:
                flag1 = 1
                if tmp != (http_no_secure + '/') and tmp != (http_secure + "/"):
                    return (False,domain_)
            elif flag1 == 1 and flag2 == 0:
                last_point_position = -1
                pos2 = pos
                while pos2 < len(url) and url[pos2] != '/':
                    if url[pos2] == '.':
                        last_point_position = pos2
                    pos2 += 1
                if last_point_position < 0:
                    return (False,domain_)
                flag2 = 2
            else:
                if pos < last_point_position and c != '/':
                    domain += c
                elif pos == last_point_position:
                    table = "qwertyuiopasdfghjklzxcvbnm.1234567890-"
                    for v in domain:
                        if v not in table:
                            return (False,domain_)
                else:
                    if flag3 == 0:
                        if c != '/':
                            if c != '.':
                                domain_zone += c
                        else:
                            table_domain = "qwertyuiopasdfghjklzxcvbnm"
                            for v in domain_zone:
                                if v not in table_domain:
                                    return (False,domain_)
                            flag3 = 1
                    else:
                        the_rest_of_the_way += c
    if the_rest_of_the_way:
        url_full_char_table = "qwertyuiopasdfghjklzxcvbnm/?&+;#1234567890-=._[]"
        for c in the_rest_of_the_way:
            if c not in url_full_char_table:
                return (False,domain_)
    domain_ = domain + "." + domain_zone
    return (True,domain_)

def checking_string_validity(url):
    (res,domain_)= checking_string_validity_(url,domain_=None)
    return res

def get_domain(url):
    
        (res,_domain_)= checking_string_validity_(url,domain_=None)
        if(res!=True):
            raise Exception("Некорректное имя домена!")
        

        url = url.lower()
        start_pos = 4
        if url[start_pos] == 's':
           start_pos += 1
        start_pos += 3
        domain = ""
        while url[start_pos] != '/':
              domain += url[start_pos]
              start_pos += 1
        _domain_=domain

        return _domain_
   


urls = [
    "https://www.google.com/search?q=base64+code+table&oq=base64+code+ta&gs_lcrp=EgZjaHJvbWUqBwgBEAAYgAQyBggAEEUYOTIHCAEQABiABDIKCAIQABiABBiiBDIKCAMQABiABBiiBDIKCAQQABiABBiiBDIKCAUQABiABBiiBDIKCAYQABiABBiiBNIBCjIyNjU1ajBqMTWoAgiwAgE&sourceid=chrome&ie=UTF-8",
    "http://example.com/",
    "example.com",
    "погода.ру",
    "http://qwert.@@@@/g.ru",
    "https://www.dns-shop.ru/",
    "https://www.dns-shop.ru/catalog/17a89a0416404e77/materinskie-platy/?stock=now-today-tomorrow-later&f[rv2z]=13iyb1&f[uq]=lxihi",
    "https://dotnet.microsoft.comen-us/apps/aspnet",
    "https://learn.microsoft.com/en-us/aspnet/core/blazor/security/?view=aspnetcore-8.0&WT.mc_id=dotnet-35129-website"
]

for url in urls:
    print(url)
    print("\n")
    print(checking_string_validity(url))
    try:
        print(get_domain(url))
    except Exception as e:
        print("error:")
        print(e)

