import requests
from bs4 import BeautifulSoup as bs


url = 'https://www.russianfood.com/'
req = requests.get(url)
soup = bs(req.text, 'html.parser')

recep_list = soup.find_all('dt')

category_list = []  # список категорий блюд
link_list = []  # список ссылок на категорию блюда
for r in recep_list:
    category_list.append(r.a.text)
    link_list.append('https://www.russianfood.com/' + r.a['href'])

first_eat_list = soup.find('dd')  # html первых блюд
first_eat = first_eat_list.text  # строка первых блюд
first_list = []  # пустой список для первых блюд
first_list.append(first_eat)  # список первых блюд

second_eat_list = soup.find_all('a', class_='resList')[22:85]  # html вторых блюд

second_list = []  # список вторых блюд
for s in second_eat_list:
    second_list.append(s.text)

zag_eat_list = soup.find_all('a', class_='resList')[86:98]  # html заготовок
zag_list = []  # список заготовок
for z in zag_eat_list:
    zag_list.append(z.text)

snacks_eat_list = soup.find_all('a', class_='resList')[99:131]  # html закусок
snacks_list = []  # список закусок
for s in snacks_eat_list:
    snacks_list.append(s.text)

bakery_eat_list = soup.find_all('a', class_='resList')[132:193]  # html изделий из теста
bakery_list = []  # список изделий из теста
for b in bakery_eat_list:
    bakery_list.append(b.text)

marinade_eat_list = soup.find_all('a', class_='resList')[194:202]  # html маринада
marinade_list = []  # список маринада
for m in marinade_eat_list:
    marinade_list.append(m.text)

drink_eat_list = soup.find_all('a', class_='resList')[203:232]  # html напитков
drink_list = []  # список напитков
for d in drink_eat_list:
    drink_list.append(d.text)

spice_eat_list = soup.find_all('a', class_='resList')[233:234]  # html приправ
spice_list = []  # список приправ
for sp in spice_eat_list:
    spice_list.append(sp.text)

sweet_eat_list = soup.find_all('a', class_='resList')[235:279]  # html сладостей
sweet_list = []  # список сладостей
for sw in sweet_eat_list:
    sweet_list.append(sw.text)

sauces_eat_list = soup.find_all('a', class_='resList')[280:300]  # html соусов
sauces_list = []  # список соусов
for sa in sauces_eat_list:
    sauces_list.append(sa.text)