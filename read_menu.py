from bs4 import BeautifulSoup
from lxml import html
import requests
import json

j2 = "https://hf-foodpro.austin.utexas.edu/foodpro/shortmenu.aspx?sName=University+Housing+and+Dining&locationNum=12&locationName=J2+Dining&naFlag=1"

def to_dict(l):
  segment_dict = {}
  current_key = None
  for item in l:
      if item.startswith("--"):
          current_key = item
          segment_dict[current_key] = []
      elif current_key:
          segment_dict[current_key].append(item)
  return segment_dict


def save_data(d, date):
    with open(f"data/{date}.json", "w") as f:
        json.dump(d, f, indent=4)


response = requests.get(j2)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Initialize a list to store the scraped data
    scraped_data = []

    # Find all divs with class 'shortmenucats' and 'shortmenurecipes' in the order they appear
    for element in soup.find_all(['div'], class_=['shortmenumeals', 'shortmenucats', 'shortmenurecipes']):
        text = element.get_text(strip=True)
        scraped_data.append(text)
    ib = scraped_data.index('Breakfast')
    il = scraped_data.index('Lunch')
    id = scraped_data.index('Dinner')
    b = scraped_data[ib+1:il]
    l = scraped_data[il+1:id]
    d = scraped_data[id+1:]
    breakfast = to_dict(b)
    lunch = to_dict(l)
    dinner = to_dict(d)
    final = {
        'Breakfast': breakfast,
        'Lunch': lunch,
        'Dinner': dinner
    }
    save_data(final, '03222024')
else:
    print("Failed to retrieve the webpage")