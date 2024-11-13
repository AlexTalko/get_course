import requests
from abc import ABC, abstractmethod

from config.settings import API_KEY


class API(ABC):
    """API base class"""

    @abstractmethod
    def get_course(self):
        pass


class APICourse(API):
    """Класс для получения курса доллара к рублю с https://currencylayer.com/dashboard"""

    def get_course(self):
        response = requests.get(
            f'https://api.currencylayer.com/live?access_key={API_KEY}&currencies=RUB')
        if response.status_code == 200:
            return response.json()
