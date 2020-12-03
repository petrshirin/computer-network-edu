from typing import List, Dict
import json
import csv


ANDROID_VERSION_TO_API = {
    "1.0": 1,
    "1.1": 2,
    "1.5": 3,
    "1.6": 4,
    "2.0": 5,
    "2.0.1": 6,
    "2.1": 7,
    "2.2": 8,
    "2.3": 9,
    "2.3.3": 10,
    "3.0": 11,
    "3.1": 12,
    "3.2": 13,
    "4.0": 14,
    "4.0.3": 15,
    "4.1": 16,
    "4.2": 17,
    "4.3": 18,
    "4.4": 19,
    "4.4W": 20,
    "5.0": 21,
    "5.1": 22,
    "6.0": 23,
    "7.0": 24,
    "7.1.1": 25,
    "8.0": 26,
    "8": 27,
    "9.0": 28,
    "10.0": 29,
}


def read_csv(file_str: str) -> List[Dict]:
    data = []
    with open(file_str, 'r', encoding='utf-8') as f:
        lines = csv.reader(f, delimiter=',')
        keys = lines.__next__()
        for line in lines:
            element = {}
            for i in range(len(keys)):
                try:
                    element[keys[i]] = line[i].replace('"', '').replace('\n', '')
                except IndexError:
                    continue
            data.append(element)

    return data


def format_to_int(num: str) -> int:
    result = 0
    mult = 1
    split_num = num.replace('+', '').replace(',', '')
    if split_num.lower() == 'free':
        return 0
    for i in range(len(split_num) - 1, -1, -1):
        result += mult * int(split_num[i])
        mult *= 10
    return result


def format_data(data: List[Dict]) -> None:
    for elem in data:
        elem['Android Ver'] = ANDROID_VERSION_TO_API.get(elem.get('Android Ver', '0').split(' ')[0], 10000)
        elem['Installs'] = format_to_int(elem.get('Installs', ''))
        price = elem.get('Price', '0.0')
        if len(price) > 1:
            price = price[1:]
        if elem.get('Price', '0.0').lower() != 'everyone':
            elem['Price'] = bool(float(price))
        else:
            elem['Price'] = False
        elem['Genres'] = elem.get('Genres', '').split(';')


if __name__ == '__main__':
    data = read_csv('googleplaystore.csv')
    format_data(data)
    with open('apps_parser.json', 'w') as f:
        f.write(json.dumps(data))
