import requests

def download_xml():
    url = 'https://www.treasury.gov/ofac/downloads/sanctions/1.0/sdn_advanced.xml'
    response = requests.get(url)
    with open('sdn_advanced.xml', 'w') as file:
        file.write(response.text)

download_xml()
