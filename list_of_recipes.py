import requests
from bs4 import BeautifulSoup as bs


url = 'https://www.russianfood.com/'
header = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
           'upgrade-insecure-requests': '1',
           'cookie': 'mos_id=CllGxlx+PS20pAxcIuDnAgA=; session-cookie=158b36ec3ea4f5484054ad1fd21407333c874ef0fa4f0c8e34387efd5464a1e9500e2277b0367d71a273e5b46fa0869a; NSC_WBS-QUBG-jo-nptsv-WT-443=ffffffff0951e23245525d5f4f58455e445a4a423660; rheftjdd=rheftjddVal; _ym_uid=1552395093355938562; _ym_d=1552395093; _ym_isad=2'}

req = requests.get(url, headers=header)
for key, value in req.request.headers.items():
    print(key+": "+value)
print(req.status_code)

soup = bs(req.text, 'html.parser')
recep_list = soup.find_all('dt')  # html категорий блюд
category_list = []  # список категорий блюд
for r in recep_list:
    category_list.append(r.a.text)


first_eat_list = soup.find_all('a', class_='resList')[1:21] # html первых блюд

first_list = []  # пустой список для первых блюд
first_link = [] # пустой список ссылок первых блюд
ing_first = []
for fl in first_eat_list:
    first_link.append('https://www.russianfood.com/' + fl['href'])  # список ссылок на первые блюда
    first_list.append(fl.text)  # список первых блюд

second_eat_list = soup.find_all('a', class_='resList')[22:85]  # html вторых блюд
second_list = []  # список вторых блюд
second_link = []
for s in second_eat_list:
    second_link.append('https://www.russianfood.com/' + s['href'])
    second_list.append(s.text)

zag_eat_list = soup.find_all('a', class_='resList')[86:98]  # html заготовок
zag_list = []  # список заготовок
zag_link = []
for z in zag_eat_list:
    zag_link.append('https://www.russianfood.com/' + z['href'])
    zag_list.append(z.text)

snacks_eat_list = soup.find_all('a', class_='resList')[99:131]  # html закусок
snacks_list = []  # список закусок
snacks_link = []
for s in snacks_eat_list:
    snacks_link.append('https://www.russianfood.com/' + s['href'])
    snacks_list.append(s.text)

bakery_eat_list = soup.find_all('a', class_='resList')[132:193]  # html изделий из теста
bakery_list = []  # список изделий из теста
bakery_link = []
for b in bakery_eat_list:
    bakery_link .append('https://www.russianfood.com/' + b['href'])
    bakery_list.append(b.text)

marinade_eat_list = soup.find_all('a', class_='resList')[194:202]  # html маринада
marinade_list = []  # список маринада
marinade_link = []
for m in marinade_eat_list:
    marinade_link.append('https://www.russianfood.com/' + m['href'])
    marinade_list.append(m.text)

drink_eat_list = soup.find_all('a', class_='resList')[203:232]  # html напитков
drink_list = []  # список напитков
drink_link = []
for d in drink_eat_list:
    drink_link.append('https://www.russianfood.com/' + d['href'])
    drink_list.append(d.text)

spice_eat_list = soup.find_all('a', class_='resList')[233:234]  # html приправ
spice_list = []  # список приправ
spice_link = []
for sp in spice_eat_list:
    spice_link.append('https://www.russianfood.com/' + sp['href'])
    spice_list.append(sp.text)

sweet_eat_list = soup.find_all('a', class_='resList')[235:279]  # html сладостей
sweet_list = []  # список сладостей
sweet_link = []
for sw in sweet_eat_list:
    sweet_link.append('https://www.russianfood.com/' + sw['href'])
    sweet_list.append(sw.text)

sauces_eat_list = soup.find_all('a', class_='resList')[280:300]  # html соусов
sauces_list = []  # список соусов
sauces_link = []
for sa in sauces_eat_list:
    sauces_link.append('https://www.russianfood.com/' + sa['href'])
    sauces_list.append(sa.text)
           
