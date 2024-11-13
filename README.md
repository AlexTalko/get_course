# Тестовое на Python:

### Реализован базовый проект на Django 3.* согласно ТЗ.

#### Для запуска требуется:
* регистрация на сайте [API Валюты](https://currencylayer.com/dashboard) 
* API_KEY согласно *.env.sample*

#### При вызове "/get_current_usd/" :

* Запрос к API https://api.currencylayer.com/ возвращает актуальный курс доллара к рублю в формате JSON и 10 последних
  запросов курсов.
* Вывод в консоль истории запросов;
* Сохраняет историю запросов в JSON файле.