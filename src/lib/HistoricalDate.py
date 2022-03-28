import requests
from datetime import datetime as dt
import random
import time
from lib.Validate import Validate

URL = 'https://api.wikimedia.org/feed/v1/wikipedia/en/onthisday/all/'

HEADERS = {
    'User-Agent': 'Flask Historical Dates (github.com/jmartinezl)'
}

LIMIT = 20

class HistoricalDate(object):
    """docstring for ClassName."""


    def __get_wikimedia_feed(self, t_date: str):
        data = None
        try:
            response = requests.get(URL + t_date, headers=HEADERS)
            data = response.json()
        except requests.exceptions.RequestException as e:  # This is the correct syntax
            raise SystemExit(e)
            
        return data


    def __random_date(self) -> str:
        d = random.randint(1, int(time.time()))
        return dt.fromtimestamp(d).strftime('%m/%d')


    def __extract_data(self, data: object) -> object:
        return {'year' : data['year'], 'text' : data['text']}


    def get_day(self, tdate: str) -> object:

        Validate.validate_date(tdate)
        
        data = self.__get_wikimedia_feed(tdate)

        result = map(self.__extract_data, data['events'][:20])

        result = list(result)

        return result      


    def get_random(self) -> object:
        random_date = self.__random_date()

        data = self.__get_wikimedia_feed(random_date)

        result = map(self.__extract_data, data['events'][:20])

        result = list(result)

        return result


    def get_today(self) -> object:

        today = dt.now()
        today_date = today.strftime('%m/%d')

        data = self.__get_wikimedia_feed(today_date)

        result = map(self.__extract_data, data['events'][:20])

        result = list(result)
        
        return result
