# -*- coding: utf-8 -*-
#Задание 5. Создать CGI-сервер.
from http.server import HTTPServer, CGIHTTPRequestHandler
server_address = ("", 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)

httpd.serve_forever()