import requests
import json
from config import API_ACCESS_KEY, ext_exchanges


class APIException(Exception):
    pass


class CurrenciesConverter:
    @staticmethod
    def get_price(base: str, symbols: str, amount: float):
        get_param = {
            'access_key': API_ACCESS_KEY,
            'base': 'EUR',  # бесплатный вариант аккаунта на exchangeratesapi.io поддерживает только одну базовую валюту
            'symbols': base + ',' + symbols
        }
        r = requests.get('http://api.exchangeratesapi.io/v1/latest', params=get_param)
        print(r.status_code)
        return amount * float(json.loads(r.content)['rates'][symbols]) / float(json.loads(r.content)['rates'][base])

    @staticmethod
    def convert(values):
        try:
            c1 = ext_exchanges[values[0].upper()]
        except KeyError:
            raise APIException(f'Таких денег у нас нет: {values[0]}')
        try:
            c2 = ext_exchanges[values[1].upper()]
        except KeyError:
            raise APIException(f'Таких денег у нас нет: {values[1]}')

        if c1 == c2:
            raise APIException(f'Вы пытаетесь конвертировать одинаковые валюты {c1}!')

        try:
            sum = float(values[2])
        except ValueError:
            raise APIException('Шо-то не та сумма денег')

        return f"`{sum} {c1} = {(CurrenciesConverter.get_price(c1, c2, sum)):.4f} {c2}`"