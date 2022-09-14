from ast import Lambda
from collections import defaultdict
from multiprocessing.sharedctypes import Value
from re import X
from tkinter.messagebox import NO
from turtle import title
from bs4 import BeautifulSoup
from files_and_folders import *
import csv

processed_data = {}


class parser_html:
    def __init__(self, data, name_product):
        self.data = data
        self.name_product = name_product.replace('.html', '')
        self.pr_data = dict()

    def parser_mvm(self):
        product_spec_dict = dict()
        soup = BeautifulSoup(self.data, 'lxml')
        characteristics = soup.find_all('div', attrs={'class': 'characteristics'})
        spec_and_value = characteristics[0].find_all(attrs={'class': 'item-with-dots'})
        for i in spec_and_value:
            spec = i.find(attrs={'class': 'item-with-dots__title'})
            value = i.find(attrs={'class': 'item-with-dots__value'})
            product_spec_dict[spec.text.strip()] = value.text.strip()

        title = soup.find(attrs={'class': 'bar__product-title'}).text.strip()
        product_spec_dict['Бренд'] = title

        self.pr_data[self.name_product] = product_spec_dict


class ConversionTemplate():
    def __init__(self, f_csv, processed_data):
        self.f_csv = f_csv
        self.processed_data = processed_data
        self.search_for_changes = None
        self.all_data_csv = None

    def m_search_for_changes(self):
        """Удаляем данные в которых не нужно ничего менять"""
        def is_adalt(obj):
            el1, el2 = obj[0].split(';')
            return [el1, el2] if el1 != el2 and el2 != '' else 0

        _f = list(filter(lambda x: x != 0, (map(is_adalt, self.f_csv))))
        self.search_for_changes = _f

        def is_adalt(obj):
            el1, el2 = obj[0].split(';')
            return el1

        _f = list(filter(lambda x: x != 0, (map(is_adalt, self.f_csv))))
        self.all_data_csv = _f

    def replacement_in_masive(self):

        def special_logic(x, y, obj):
            i = x[3:4]
            if i == '1':
                main_camera = obj[y].split('/')
                count = len(main_camera)

                main_camera = max(map(lambda x: int(x) if x.isnumeric() else 0, main_camera))
                camera_module = obj[y]

                if count > 1:
                    obj['Основная камера МПикс'] = main_camera
                    obj['Модуль камер'] = camera_module

            elif i == '2':
                key_1, key_2 = 'Диагональ', 'Разрешение экрана'
                argument_1, argument_2 = obj[y].split('/')
                obj[key_1] = argument_1
                obj[key_2] = argument_2
                obj.pop(y)

            elif i == '3':
                arg = obj[y].split(' ')
                obj[y] = arg[1]

        for item in self.search_for_changes:
            for _i2 in self.processed_data.values():
                if _i2.get(item[0]):
                    if item[1][0:3] == '>=>':
                        special_logic(item[1], item[0], _i2)
                    else:
                        _i2[item[1]] = _i2[item[0]]
                        _i2.pop(item[0])

        """Удаление из списка полей которых не т в шаблоне"""
        _d = defaultdict(list)
        for product, list_value in self.processed_data.items():

            for title_value, item_value in list_value.items():
                try:
                    self.all_data_csv.index(title_value)
                    _d[product].append([title_value, item_value])
                except ValueError:
                    pass

        self.processed_data = _d


def startHtmlProcessing():
    processed_data = list()
    obj_file = WorkFolderFiles()
    obj_file.find_file()
    data = obj_file.list_file
    for key, value in data.items():
        obj_file.open_file(value[0])
        obj_spec_product = parser_html(obj_file.data, key)
        obj_spec_product.parser_mvm()

        f_csv = WorkFolderFiles.open_file_csv('cat/smartfony.csv')
        conversion = ConversionTemplate(f_csv, obj_spec_product.pr_data)
        conversion.m_search_for_changes()
        conversion.replacement_in_masive()

        processed_data.append(conversion.processed_data)
    return processed_data


# startHtmlProcessing()
