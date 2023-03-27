import requests


# создание объявления
data = requests.post('http://127.0.0.1:5000/ads/',
                     json={'description': 'test', 'owner': 'mikhail'})

print(data.status_code)
print(data.text)


# получение объявления
data = requests.get('http://127.0.0.1:5000/ads/1/')

print(data.status_code)
print(data.text)


# изменение объявления
data = requests.patch('http://127.0.0.1:5000/ads/1/', json={'owner': 'john'})
print(data.status_code)
print(data.json())

data = requests.get('http://127.0.0.1:5000/ads/1/')

print(data.status_code)
print(data.text)


# удаление объявления
data = requests.delete('http://127.0.0.1:5000/ads/1/')
print(data.status_code)
print(data.json())

data = requests.get('http://127.0.0.1:5000/ads/1/')

print(data.status_code)
print(data.text)
