from collections import defaultdict
import re
from bs4 import BeautifulSoup
from files_and_folders import *
from settings import CATEGORY_CSV

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
            spec = i.find(attrs={'class': 'item-with-dots__title'}).text.strip()
            value = i.find(attrs={'class': 'item-with-dots__value'}).text.strip()

            if product_spec_dict.get(spec):
                product_spec_dict[spec] = f'{product_spec_dict[spec]} {value}'
            else:
                product_spec_dict[spec] = value

        title = soup.find_all(attrs={'class': 'breadcrumbs__link'})
        product_spec_dict['Бренд'] = title[-1].text.strip() if title else 'NoBrand'
        self.pr_data[self.name_product] = product_spec_dict


class ConversionTemplate():
    def __init__(self, f_csv, processed_data):
        self.f_csv = [x[0].split(';') for x in f_csv]
        self.processed_data = processed_data
        self.search_for_changes = None
        self.all_data_csv = None

    def deleting_outside_template(self):
        """Удаление из списка полей которых нет в шаблоне csv"""
        pattern_from_csv = [x[0] for x in self.f_csv]
        _d = defaultdict(list)
        for product, list_value in self.processed_data.items():
            for title_value, item_value in list_value.items():
                if title_value in pattern_from_csv:
                    _d[product].append([title_value, item_value])
        self.processed_data = _d

    def replacement_in_masive(self):

        _t, *_ = [*self.processed_data.values()]
        basic_data = {x[0]: x[1] for x in _t}

        basic_csv = {x[0]: [x[1], x[2]] for x in self.f_csv}

        new_basic_data = {}

        for title_spec, value_spec in basic_data.items():
            if title_spec in basic_csv.keys():
                csv_value_spec, csv_type_spec = basic_csv[title_spec]

                if csv_value_spec[0:3] == '>=>':
                    _r = self.special_logic(csv_value_spec, title_spec, value_spec)
                    new_basic_data.update(_r)
                elif csv_type_spec == 'int':
                    _value_spec = self._clearing_letters(value_spec)
                    new_basic_data[csv_value_spec] = _value_spec
                else:
                    new_basic_data[csv_value_spec] = value_spec

        new_basic_data = [[x, y] for x, y in new_basic_data.items()]
        _key = [*self.processed_data.keys()]
        self.processed_data[_key[0]] = new_basic_data

    @staticmethod
    def _clearing_letters(_str):
        pattern = r'[\d\.]{1,10}'
        result = re.search(pattern, _str)
        return result.group(0)

    @staticmethod
    def special_logic(x, y, value):
        _r = {}
        i = x[3:4]

        if i == '1':
            """Ищум самую большую камеру по мега пикселям"""
            main_camera = max([int(x) if x.isnumeric() else 0 for x in value.split('/')])
            camera_module = value

            if str(main_camera) != camera_module:
                _r['Основная камера МПикс'] = main_camera
                _r['Модуль камер'] = camera_module
        elif i == '2':
            arg_1, arg_2 = re.search(r'\d{1,2}\.\d{1,2}"', value), re.search(r'\d{2,4}x\d{2,4}', value)
            _r['Диагональ'] = arg_1[0] if arg_1 else arg_1
            _r['Разрешение экрана'] = arg_2[0] + ' Пикс' if arg_2 else arg_2

        return _r


def startHtmlProcessing(obj):
    processed_data = list()
    obj_file = WorkFolderFiles()
    obj_file.find_file()
    for name_product, value in obj.items():
        name_product_file, _ = obj_file.list_file[f'{name_product}.html']
        category = CATEGORY_CSV[value['category']]
        obj_file.open_file(name_product_file)
        obj_spec_product = parser_html(obj_file.data, name_product)
        obj_spec_product.parser_mvm()

        f_csv = WorkFolderFiles.open_file_csv(f'cat/{category}.csv')
        conversion = ConversionTemplate(f_csv, obj_spec_product.pr_data)
        conversion.deleting_outside_template()
        conversion.replacement_in_masive()
        processed_data.append(conversion.processed_data)
    return processed_data
