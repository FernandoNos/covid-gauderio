import requests
import re



url = 'https://distanciamentocontrolado.rs.gov.br/wp/api/dcrs/get_cidades/'

class Flag:
    def __init__(self, name):
        self.name = name
        self.cities = []


def getRSCovidStatuses():
    yellow = Flag('bandeira amarela')
    orange = Flag('bandeira laranja')
    red = Flag('bandeira vermelha')
    black = Flag('bandeira preta')

    flags = {'bandeira amarela':yellow, 'bandeira laranja':orange, 'bandeira vermelha':red, 'bandeira preta':black}
    response = requests.get(url, verify=False)
    posts = response.json()['posts']
    for post in posts:
        flag = post['bandeira'].lower()
        flag_group = re.search('^(bandeira \w+).*', flag,re.IGNORECASE)
        if flag_group:
            match = flag_group.group(1).lower()
            hash_flag_elem = flags[match]
            hash_flag_elem.cities.append(post)
    return flags
