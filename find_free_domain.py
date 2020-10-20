import requests
import json
import re
import sys
import whois


def download_register():
    response = requests.get('https://reestr.rublacklist.net/api/v2/domains/json')
    with open('register.json', 'w') as f:
        try:
            response.json()
            f.write(response.text)
        except json.JSONDecodeError:
            print('Invalid response type, need json')


def check_domains_for_free():
    with open('register.json', 'r') as f:
        data = json.loads(f.read())
    for domain in data:
        try:
            d = domain
            if '*.' in d:
                d = d[2:]

            if check_on_whois(d):
                print(d)

        except Exception as err:
            print(err)


def check_on_whois(domain: str) -> bool:
    response = requests.get(f'http://api.whois.vu/?q={domain}')
    try:
        data = response.json()
        if data['available'] == "yes":
            return True
        else:
            return False
    except json.JSONDecodeError:
        return False
    except KeyError:
        return False


if __name__ == '__main__':
    download_register()
    check_domains_for_free()



