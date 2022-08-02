import requests
from bs4 import BeautifulSoup as bs
from parcing_recipe import new_table

for nw in new_table['Ссылка на категорию']:  # находим ингридиенты каждого блюда с помощью парсера внутренних страниц
    ing_list = []
    url_nw = nw
    req_nw = requests.get(url_nw )
    soup_nw = bs(req_nw.text, 'html.parser')
    ingredients = soup_nw.find('div', class_='ingr_str')
    ing_list.append(ingredients)
    # print(ingredients.text)

# for f in first_link:
#     url_f = f
#     print(url_f)
#     req_f = requests.get(url_f)
#     soup_f = bs(req_f.text, 'html.parser')
#     ingredients = soup_f.find('div', class_='ingr_str')
#     ing_first.append(ingredients)
#     # print(ing_first)
