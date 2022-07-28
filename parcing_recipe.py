import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from openpyxl import Workbook

url = 'https://www.russianfood.com/'
r = requests.get(url)
soup = bs(r.text, 'html.parser')
recep_list = soup.find_all('dt')
category_list = []  # список категорий блюд
link_list = []  # список ссылок на категорию блюда
for r in recep_list:
    category_list.append(r.a.text)
    link_list.append('https://www.russianfood.com/' + r.a['href'])

table = pd.DataFrame({'Категория блюд': category_list, 'Ссылка на категорию': link_list})
print(table)

writer = pd.ExcelWriter('excel_file.xlsx')
table.to_excel(writer)
writer.save()
print('DataFrame is written successfully to Excel File.')
