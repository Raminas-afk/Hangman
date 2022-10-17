
import requests
from bs4 import BeautifulSoup

page = requests.get('https://mokslai.lt/referatai/lietuviu-kalba/visi-zodziai-kurie-yra-vartojami-lietuviu-kalba.html')  # Getting page HTML through request
soup = BeautifulSoup(page.content, 'html.parser')  # Parsing content using beautifulsoup

print(soup.prettify())
list(soup.children)
[type(item) for item in list(soup.children)]
    