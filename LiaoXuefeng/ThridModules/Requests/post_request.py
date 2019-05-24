import requests

#要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据：
r = requests.post('https://accounts.douban.com/login', data={'form_emaill': 'abc@example.com', 'form_password': '123456'})
print(r.status_code)
print(r.text)

#requests默认使用application/x-www-form-urlencoded对POST数据编码。如果要传递JSON数据，可以直接传入json参数：
params = {'key': 'value'}
r = requests.post(url, json=params)

#类似的，上传文件需要更复杂的编码格式，但是requests把它简化成files参数：
upload_files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=upload_files)

#除了能轻松获取响应内容外，requests对获取HTTP响应的其他信息也非常简单。例如，获取响应头：
print(r.headers)

