import requests
import lxml
from bs4 import BeautifulSoup


url = "https://www.rottentomatoes.com"
f = requests.get(url)
soup = BeautifulSoup(f.content, 'lxml')
movies = soup.find('section',{'class':'dynamic-text-list'}).find_all('a')
print(movies)
