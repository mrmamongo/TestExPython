## requests
По ссылке ```https://line14.bkfon-resources.com/live/currentLine/ru``` получить все футбольные матчи в **Лайве**.
Данные записать в словарь по названию игроков в виде ```gamer_name = "Игрок 1 - Игрок 2"```.
Словарь должен быть в виде: ```{id1: gamer_name1, id2: gamer_name2, .... idN: gamer_nameN}```
**id** - уникальный идентификатор в md5
Для получения идентификатора использовать модуль ```hashlib```

## selenium
Из полученных данных выбрать любую игру. в Браузере через Selenium открыть игру по названию на сайте ```fonbet.ru``` (не по url). 
В консоль вывести название выбранной игры.
Использовать Chrome.
