import requests
from bs4 import BeautifulSoup as soup 


url_raw = 'https://www.google.com/search?q='
url = ''
data = ''
s1 = ''

def get_query():
  query = str(input('Enter your search term: '))
  query = query.replace(' ', '+')
  global url 
  url = url_raw + query
  return

def grab_file():
  global data
  try:
    data = requests.get(url)
  except Exception as e:
    print(e)
  return

def cook_soup():
  global s1
  s1 = soup(data.content, 'html.parser')

get_query()
grab_file()
cook_soup()
