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
table = pd.DataFrame({'Категория блюд': lor.category_list, 'Перечень блюд': '1', 'Ссылка на категорию': '1'})
table._set_value(0, 'Перечень блюд', ', '.join(lor.first_list))  # новый столбец 'Перечень блюд' со значениями на каждой строке
table._set_value(0, 'Ссылка на категорию', ', '.join(lor.first_link))  # перечень ссылок на первый блюда
table._set_value(0, 'Ингредиенты', ', '.join(lor.first_link))  # перечень ссылок на первый блюда
table._set_value(1, 'Перечень блюд', ', '.join(lor.second_list))  # добавлен перечень вторых блюд на каждой строке
table._set_value(1, 'Ссылка на категорию', ', '.join(lor.second_link))
table._set_value(2, 'Перечень блюд', ', '.join(lor.zag_list))  # добавлен перечень заготовок на каждой строке
table._set_value(2, 'Ссылка на категорию', ', '.join(lor.zag_link))
table._set_value(3, 'Перечень блюд', ', '.join(lor.snacks_list))  # добавлен перечень закусок на каждой строке
table._set_value(3, 'Ссылка на категорию', ', '.join(lor.snacks_link))
table._set_value(4, 'Перечень блюд', ', '.join(lor.bakery_list))  # добавлен перечень изделий из теста на каждой строке
table._set_value(4, 'Ссылка на категорию', ', '.join(lor.bakery_link))
table._set_value(5, 'Перечень блюд', ', '.join(lor.marinade_list))  # добавлен перечень маринада на каждой строке
table._set_value(5, 'Ссылка на категорию', ', '.join(lor.marinade_link))
table._set_value(6, 'Перечень блюд', ', '.join(lor.drink_list))  # добавлен перечень напитков на каждой строке
table._set_value(6, 'Ссылка на категорию', ', '.join(lor.drink_link))
table._set_value(7, 'Перечень блюд', ', '.join(lor.spice_list))  # добавлен перечень приправ на каждой строке
table._set_value(7, 'Ссылка на категорию', ', '.join(lor.spice_link))
table._set_value(8, 'Перечень блюд', ', '.join(lor.sweet_list))  # добавлен перечень сладостей на каждой строке
table._set_value(8, 'Ссылка на категорию', ', '.join(lor.sweet_link))
table._set_value(9, 'Перечень блюд', ', '.join(lor.sauces_list))  # добавлен перечень соусов на каждой строке
table._set_value(9, 'Ссылка на категорию', ', '.join(lor.sauces_link))

splitted = table['Перечень блюд'].str.split(',\s*')

l = splitted.str.len()

splitted_link = table['Ссылка на категорию'].str.split(',\s*')



# новая таблица для записи обновленных данных
new_table = pd.DataFrame({'Категория блюд': np.repeat(table['Категория блюд'], l),
                          'Перечень блюд': np.concatenate(splitted.values),
                          'Ссылка на категорию': np.concatenate(splitted_link.values)},
                         columns=['Категория блюд', 'Перечень блюд', 'Ссылка на категорию'])

if __name__ == '__main__':
    print(new_table)
    print('DataFrame is written successfully to Excel File.')

writer = pd.ExcelWriter('excel_file.xlsx')
new_table.to_excel(writer)
writer.save()
