import json
from abc import ABC, abstractmethod


class Manager(ABC):
    @abstractmethod
    def save_data(self, *args, **kwargs):
        raise NotImplementedError


class JSONSaver(Manager):
    """Класс для сохранения полученного курса валют в JSON-файл"""

    def __init__(self, file_save):
        self.file_save = file_save

    def save_data(self, data) -> None:
        with open(self.file_save, 'w') as file:
            json.dump(data, file)
        print(f'Курс сохранен в {self.file_save}')

class FileManager:
    """Класс для обработки данных файла"""

    def __init__(self, file_path):
        self.file_path = file_path

    def json_data(self):
        """Получаем список словарей запросов курса"""
        with open(self.file_path, 'r') as file:
            return json.load(file)


