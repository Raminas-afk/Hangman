from bs4 import BeautifulSoup
import requests

sunkiu_zodziu_sarasas = []
vidutiniu_zodziu_sarasas = []
lengvu_zodziu_sarasas = []

source = requests.get("https://1000mostcommonwords.com/1000-most-common-lithuanian-words/").text
soup = BeautifulSoup(source, 'html.parser')

blokai = soup.find_all('tr')


for blokas in blokai:
    try:
        zodis = blokas.find('td').next_element.next_element.next_element.text.strip()
        if len(zodis) >= 9:
            sunkiu_zodziu_sarasas.append(zodis.upper())
        elif 8 >= len(zodis) >= 6:
            vidutiniu_zodziu_sarasas.append(zodis.upper())
        elif 5 >= len(zodis) >= 4:
            lengvu_zodziu_sarasas.append(zodis.upper())

    except:
        pass



