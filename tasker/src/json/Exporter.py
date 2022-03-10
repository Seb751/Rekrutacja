import json


class Exporter:

    def __init__(self):
        pass

    def save_tasks(self, tasks):
        # TODO zapisz taski do pliku tutaj
        with open('taski.json', 'w', encoding='utf8') as json_file:
            json.dump(tasks, json_file)
