from datetime import datetime


def time_now():
    """Возвращает текущее время в Unix"""
    td_since_epoch = datetime.now() - datetime(1970, 1, 1)
    total_seconds = td_since_epoch.total_seconds()
    return int(total_seconds)


def compare_time_requests(b):
    """Сравнивает время запроса в Unix timestamp. Если не прошло 10 секунд возвращает False"""
    a = time_now()
    if a - b < 10:
        exit()
