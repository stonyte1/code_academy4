from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.lrt.lt')
if response.status_code == 200:
    html = response.content
html_soup = BeautifulSoup(html, 'html.parser')
print(html_soup.select('h1')[0].get_text)

