from main.services.api import APICourse
from main.services.file_manager import JSONSaver, FileManager
from main.services.func import compare_time_requests, time_now



def __main__():
    # Загружаем историю запросов
    file = FileManager('history.json')

    # Проверяем прошло ли 10 секунд с последнего запроса
    time_last_req = file.json_data()[-1]['timestamp']
    time_req = compare_time_requests(time_last_req)

    if time_req:
        """Если с предыдущего запроса прошло 10 сек выполняем новый запрос курса и сохраняем в файл"""
        print('Запрос курса доллара к рублю выполнен')
        # Подключаем API https://api.currencylayer.com/live
        api = APICourse()
        # Получаем актуальный курс доллара к рублю
        course = api.get_course()

        # Записываем в историю запросов timestamp текущего запроса и полученный курс
        data = file.json_data()
        data.append(course)

        # Выводим последние 10 запросов курса
        print('Последние 10 запросов курса:')
        for req in data[-10:]:
            print(f'Время запроса в UNIX: {req["timestamp"]}, Курс: 1$ = {req["quotes"]["USDRUB"]}₽')


        # Сохраняем полученный курс валют в JSON-файле history.json
        file = JSONSaver('history.json')
        file.save_data(data)
    else:
        print('Запрос курса доллара к рублю не выполнен, так как прошло менее 10 секунд с последнего запроса')

if __name__ == '__main__':
    __main__()
