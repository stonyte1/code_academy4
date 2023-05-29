from bs4 import BeautifulSoup
import requests
import random
from game_front import window

response = requests.get('http://quotes.toscrape.com')

try:
    response.status_code == 200
except:
    print(response.status_code)

link = response.content
soup = BeautifulSoup(link, 'html.parser') 

quotes = soup.select('.text')
authors = soup.select('.author')

quotes_list = []
authors_list = []

for quote in quotes:
    quotes_list.append(quote.get_text())

for author in authors:
    authors_list.append(author.get_text())

number_of_quotes = len(quotes_list)
index = random.randint(0, number_of_quotes - 1)

player_guess = window(quotes_list[index], index, authors_list)

if player_guess == True:
    index = random.randint(0, number_of_quotes - 1)
    player_guess = window(quotes_list[index], index, authors_list)

