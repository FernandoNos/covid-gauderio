import requests

url = 'https://distanciamentocontrolado.rs.gov.br/wp/api/dcrs/get_cidades/'


def getRSCovidStatuses():
    response = requests.get(url, verify=False)

    return response.json()['posts']