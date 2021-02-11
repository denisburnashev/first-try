import json
import hashlib


with open('countries.json', encoding='utf-8') as countries:
    info = json.load(countries)

countries_list = []
url_list = []

url = 'https://en.wikipedia.org/wiki/'


class Iteratorq:

    def __init__(self, data):
        self.info = data
        self.counter = 0

    def __getitem__(self, i):
        return self.info[i]

    def __next__(self):
        if self.counter < len(info):
            self.counter += 1
        else:
            raise StopIteration


s_iter1 = Iteratorq(info)
for name in s_iter1:
    for keys, values in name.items():
        if keys == 'name':
            for common, count in values.items():
                if common == 'common':
                    countries_list.append(count)
print(countries_list)

for country in countries_list:
    names = country.replace(' ', '_')
    urls = (url + names)
    q = (names, urls)
    url_list.append(q)
    print(names, '-', urls)
    with open('links.txt', 'a', encoding='utf-8') as link:
        link.writelines(f'{names} - {urls}\n')

with open('links.txt', encoding='utf-8') as country:
    links_info = country.readlines()


def hash_link(start):
    while start < len(info):
        yield start
        for each in links_info:
            sig = ''.join(each)
            sig = str.encode(sig, encoding='utf-8')
            sig = hashlib.md5(sig).hexdigest()
            print(sig)
            with open('md5.txt', 'a', encoding='utf-8') as countries_link:
                countries_link.writelines(f'{sig}\n')
                start += 1


for links in hash_link(0):
    print(links)
