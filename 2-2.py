from urllib.request import urlopen, Request
import urllib.parse

url = "http://127.0.0.1:8000"

data = "language=python&framework=django"
data = data.encode('utf-8')

req = Request(url, data=data, method='POST')
req.add_header('Content-Type', 'application/x-www-form-urlencoded')

with urlopen(req) as f:
    response = f.read().decode('utf-8')
    print(response)

"""출력
HomeView.post()...
language : python
framework : django
name : 홍길동
email : hong@gmail.com
url : http://google.co.kr
[02/Jul/2024 13:51:33] "POST / HTTP/1.1" 200 2084

"""
