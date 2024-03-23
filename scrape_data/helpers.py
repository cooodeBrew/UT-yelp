import json


def read_date(soup):
    date = soup.find('input', {'name': 'strCurSearchDays'})['value']
    date = ''.join(date.split('/'))
    return date



def read_table(meal):
    menu = {}
    for category_div in meal.find_all('div', class_='shortmenucats'):
        category_name = category_div.get_text(strip=True)
        menu[category_name] = {}

        next_siblings = category_div.find_parent('td').find_parent('tr').find_next_siblings('tr')
        for sibling in next_siblings:
            recipe_div = sibling.find('div', class_='shortmenurecipes')
            if recipe_div:
                recipe_name = recipe_div.get_text(strip=True)
                menu[category_name][recipe_name] = []

                img_tags = sibling.find_all('img')
                for img in img_tags:
                    menu[category_name][recipe_name].append(img['alt'].split()[0])
    return menu


def save_data(d, date):
    with open(f"data/{date}.json", "w") as f:
        json.dump(d, f, indent=4)
