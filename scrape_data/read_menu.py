from bs4 import BeautifulSoup
import requests

from scrape_data.helpers import *

j2 = "https://hf-foodpro.austin.utexas.edu/foodpro/shortmenu.aspx?sName=University+Housing+and+Dining&locationNum=12&locationName=J2+Dining&naFlag=1"

response = requests.get(j2)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
else:
    print("J2 is not accessible")

soup = soup.body
soup = soup.find_all("table", recursive=False)[0]
date = read_date(soup)
soup = soup.find_all("table")[4]

b, l, d = soup.find_all('table', {'border': '0', 'cellpadding': '0', 'cellspacing': '1', 'width': '100%'})
menu = {
    'Breakfast': read_table(b),
    'Lunch': read_table(l),
    'Dinner': read_table(d)
}
save_data(menu, date)