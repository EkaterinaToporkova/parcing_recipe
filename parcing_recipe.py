import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from openpyxl import Workbook
from itertools import chain
import numpy as np
import seaborn as sns
import beautiful_dataframe as bd
import list_of_recipes as lor

# таблица для записи данных
table = pd.DataFrame({'Категория блюд': lor.category_list, 'Ссылка на категорию': lor.link_list, 'Перечень блюд': '1'})
table._set_value(0, 'Перечень блюд', *lor.first_list)  # новый столбец 'Перечень блюд' со значениями на каждой строке
table._set_value(1, 'Перечень блюд', ', '.join(lor.second_list))  # добавлен перечень вторых блюд на каждой строке
table._set_value(2, 'Перечень блюд', ', '.join(lor.zag_list))  # добавлен перечень заготовок на каждой строке
table._set_value(3, 'Перечень блюд', ', '.join(lor.snacks_list))  # добавлен перечень закусок на каждой строке
table._set_value(4, 'Перечень блюд', ', '.join(lor.bakery_list))  # добавлен перечень изделий из теста на каждой строке
table._set_value(5, 'Перечень блюд', ', '.join(lor.marinade_list))  # добавлен перечень маринада на каждой строке
table._set_value(6, 'Перечень блюд', ', '.join(lor.drink_list))  # добавлен перечень напитков на каждой строке
table._set_value(7, 'Перечень блюд', ', '.join(lor.spice_list))  # добавлен перечень приправ на каждой строке
table._set_value(8, 'Перечень блюд', ', '.join(lor.sweet_list))  # добавлен перечень сладостей на каждой строке
table._set_value(9, 'Перечень блюд', ', '.join(lor.sauces_list))  # добавлен перечень соусов на каждой строке

splitted = table['Перечень блюд'].str.split(',\s*')
l = splitted.str.len()

# новая таблица для записи обновленных данных
new_table = pd.DataFrame({'Категория блюд': np.repeat(table['Категория блюд'], l),
                          'Ссылка на категорию': np.repeat(table['Ссылка на категорию'], l),
                          'Перечень блюд': np.concatenate(splitted.values)},
                         columns=['Категория блюд', 'Ссылка на категорию', 'Перечень блюд'])

if __name__ == '__main__':
    print(new_table)
    print('DataFrame is written successfully to Excel File.')

writer = pd.ExcelWriter('excel_file.xlsx')
new_table.to_excel(writer)
writer.save()
