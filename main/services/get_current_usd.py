from main.services.api import APICourse
from main.services.file_manager import JSONSaver, FileManager
from main.services.func import compare_time_requests

# Загружаем историю запросов
file = FileManager('history.json')

# Проверяем прошло ли 10 секунд с последнего запроса
time_last_req = file.json_data()[-1]['timestamp']
compare_time_requests(time_last_req)
print(time_last_req)
print(compare_time_requests(time_last_req))

# Подключаем API https://api.currencylayer.com/live
api = APICourse()

# Получаем актуальный курс доллара к рублю
course = api.get_course()

#
data = file.json_data()
data.append(course)

# создаем JSON-файл
file = JSONSaver('history.json')

# сохраняем полученный курс валют в JSON-файле history.json
file.save_data(data)