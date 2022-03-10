import json
import requests
from datetime import date


class RatioObtainer:
    base = None
    target = None

    def __init__(self, base, target):
        self.base = base
        self.target = target

    def was_ratio_saved_today(self):
        # TODO
        # This function checks if given ratio was saved today and if the file with ratios is created at all
        # should return false when file doesn't exist or if there's no today's exchange rate for given values at all
        # should return true otherwise
        today = date.today()
        with open('ratios.json') as json_file:
            data = json.load(json_file)
            today_Date = today.strftime("%Y-%m-%d")
            for i in range(len(data)):
                if (data[i]['date_fetched'] == today_Date) and (data[i]['base_currency'] == self.base) and (
                        data[i]['target_currency'] == self.target):
                    return True
            return False

    def fetch_ratio(self):
        # TODO
        # This function calls API for today's exchange ratio
        # Should ask API for today's exchange ratio with given base and target currency
        # and call save_ratio method to save it

        url = 'https://api.exchangerate.host/latest'
        parameters = {'base': self.base, 'symbols': self.target}
        response = requests.get(url, params=parameters)
        data = response.json()
        self.save_ratio(data['rates'][self.target])

    def save_ratio(self, ratio):
        # TODO
        # Should save or update exchange rate for given pair in json file
        # takes ratio as argument
        # example file structure is shipped in project's directory, yours can differ (as long as it works)

        with open('ratios.json') as json_file:
            data = json.load(json_file)
            today = date.today()
            for i in range(len(data)):
                if (data[i]['base_currency'] == self.base) and (data[i]['target_currency'] == self.target):
                    data[i]['date_fetched'] = today.strftime("%Y-%m-%d")
                    data[i]['ratio'] = ratio
                    break
                elif i == len(data) - 1:
                    exchange = {'base_currency': self.base,
                                'target_currency': self.target,
                                'date_fetched': today.strftime("%Y-%m-%d"),
                                'ratio': ratio}
                    data.append(exchange)

            with open('ratios.json', 'w') as json_write_file:
                json.dump(data, json_write_file)

    def get_matched_ratio_value(self):
        # TODO
        # Should read file and receive exchange rate for given base and target currency from that file

        with open('ratios.json') as json_file:
            data = json.load(json_file)
            for i in range(len(data)):
                if (data[i]['base_currency'] == self.base) and (data[i]['target_currency'] == self.target):
                    return data[i]['ratio']
