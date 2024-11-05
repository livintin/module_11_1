import pandas as pd
import numpy as np
import requests

url1 = 'https://jsonplaceholder.typicode.com/posts/1'
response = requests.get(url1)

data = response.json()  # Если ответ в формате JSON
print('Данные:', data)

url2 = 'https://jsonplaceholder.typicode.com/posts'
data = {'title': 'foo', 'body': 'bar', 'userId': 1}
response = requests.post(url2, json=data)

print('Статус код:', response.status_code)
print('Ответ:', response.json())

url3 = 'https://jsonplaceholder.typicode.com/posts/1'
data = {'id': 1, 'title': 'updated title', 'body': 'updated body', 'userId': 1}
response = requests.put(url3, json=data)

print('Статус код:', response.status_code)
print('Ответ:', response.json())

url4 = 'https://jsonplaceholder.typicode.com/posts/1'
response = requests.delete(url4)

print('Статус код:', response.status_code)  # Ожидается 204 при успешном удалении
url5 = 'https://jsonplaceholder.typicode.com/posts/1'
response = requests.head(url5)
print('Заголовки:', response.headers)

url6 = 'https://jsonplaceholder.typicode.com/posts/1'

response = requests.options(url6)
print('Поддерживаемые методы:', response.headers.get('Allow'))

data = {
    'Студент': ['Ян', 'Дима', 'Алина', 'Марина', 'Ирина', 'Евгений'],
    'Возраст': [18, 19, 20, 21, 18, 19],
    'Оценка': [4, 5, 5, 2, 3, 2]
}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)

adults = df[df['Возраст'] == 18]
print("\n1 курс:"), print(adults)
adults = df[df['Возраст'] == 19]
print("\n2 курс:"), print(adults)
adults = df[df['Возраст'] == 20]
print("\n3 курс:"), print(adults)
adults = df[df['Возраст'] == 21]
print("\n4 курс:"), print(adults)
print()
df['Список отчисления'] = df['Оценка'] < 3
print("\nОбновленный DataFrame с оценками:")
print(df)

print('----------------------------')
print(df.head(2))
print('----------------------------')
print(df.tail(2))
print('----------------------------')
print(df.describe())

print('----------------------------')
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b = np.array([[1, 2, 3], [4, 5, 6]])
print(a.ndim, b.ndim)
print(a.shape, b.shape)
print(a.dtype, b.dtype)
print(np.zeros(2), np.ones(3), np.empty(4))
print(np.arange(2, 9, 3))
print('--------------------------')
a1 = a * 2
print(a1)
a2 = a + a1
print(a2)
