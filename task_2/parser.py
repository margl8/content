"""
парсер собирает последние 20 постов со стены сообщества
и выгружает их в json файл в виде словаря
в дальейшем просмотры, лайки и т.д. будут высчитываться прямиком из json-файла
но я пока не поняла, как это делать...
"""

#импорты
import requests

#глобальные переменные: аутентификция
token = "fcf784d2fcf784d2fcf784d206ffe7472fffcf7fcf784d29fdf12d1cff39e144bbbaa42"
version = 5.131
domain = "welltex_perm"

#глобальные переменные: расчёт ER 
likes = int(input('Введите число лайков'))
comments = int(input('Введите число комментариев'))
reposts = int(input('Введите число репостов'))
subscribers = int(input('Введите число подписчиков'))
views = int(input('Введите число основного охвата'))

"""
Wall.get
Stats.getPostReach
Расчёт ЕР
"""

response = requests.get ("https://api.vk.com/method/wall.get", 
    params={
        'access_token': token,
        'v': version,
        'domain': domain
    } 
    )
data = response.json()
print(data)
