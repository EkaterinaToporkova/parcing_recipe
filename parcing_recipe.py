import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from openpyxl import Workbook
from itertools import chain
import numpy as np
import seaborn as sns
import beautiful_dataframe

url = 'https://www.russianfood.com/'
req = requests.get(url)
soup = bs(req.text, 'html.parser')

recep_list = soup.find_all('dt')
first_eat_list = soup.find('dd')  # html первых блюд
first_eat = first_eat_list.text  # строка первых блюд
first_list = []
first_list.append(first_eat)

category_list = []  # список категорий блюд
link_list = []  # список ссылок на категорию блюда

for r in recep_list:
    category_list.append(r.a.text)
    link_list.append('https://www.russianfood.com/' + r.a['href'])


table = pd.DataFrame({'Категория блюд': category_list, 'Ссылка на категорию': link_list, 'Перечень блюд': '1'})
table._set_value(0, 'Перечень блюд', *first_list) # новый столбец 'Перечень блюд' со значение в первой строке




splitted = table['Перечень блюд'].str.split(',\s*')

l = splitted.str.len()


# новая таблица для записи обновленных данных
new_table = pd.DataFrame({'Категория блюд': np.repeat(table['Категория блюд'], l),
                    'Ссылка на категорию': np.repeat(table['Ссылка на категорию'], l),
                   'Перечень блюд':np.concatenate(splitted.values)}, columns=['Категория блюд','Ссылка на категорию', 'Перечень блюд'])


if __name__ == '__main__':
    print (new_table)
    print('DataFrame is written successfully to Excel File.')

writer = pd.ExcelWriter('excel_file.xlsx')
new_table.to_excel(writer)
writer.save()

