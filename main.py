import json
import hashlib
from pprint import pprint

url = 'https://en.wikipedia.org/wiki/'

with open('countries.json', encoding='utf-8') as countries:
    data = json.load(countries)

countries_list = []
url_list = []

for info in data:
    for name, oficial in info.items():
        if name == 'name':
            for common, count in oficial.items():
                if common == 'common':
                    countries_list.append(count)

for country in countries_list:
    names = country.replace(' ', '_')
    urls = (url+names)
    q = (names, urls)
    url_list.append(q)
    print(names, '-', urls)
    with open('links.txt', 'a', encoding='utf-8') as link:
        link.writelines(f'{names} - {urls}\n')


with open('links.txt', encoding='utf-8') as country:
    info = country.readlines()
    print(info)

for each in info:
    sig = ''.join(each)
    sig = str.encode(sig, encoding='utf-8')
    sig = hashlib.md5(sig).hexdigest()
    print(sig)
    with open('md5.txt', 'a', encoding='utf-8') as link:
        link.writelines(f'{sig}\n')

