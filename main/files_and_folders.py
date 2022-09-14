import os
import json
import csv


class WorkFolderFiles():
    def __init__(self):
        """search_folder - будем искать файлы в этой папке"""
        self.search_folder = 'html_page'
        self.list_file = {}
        self.data = None
        self.json_data = None
        self.head, self.tail = os.path.split(__file__)

    def find_file(self):
        head, tail = os.path.split(__file__)
        _p = os.path.normpath(f'{head}/data/{self.search_folder}')
        for file_folder in os.listdir(_p):
            full_path = os.path.join(_p, file_folder)
            self.list_file[file_folder] = [full_path, file_folder]

    def write_file(self, file_folder, obj):
        with open(file_folder, 'w', encoding='utf-8') as file:
            file.write(obj)

    def open_file(self, file_folder):
        with open(file_folder, 'r', encoding='utf-8') as file:
            self.data = file.read()

    def save_to_json(self, obj):
        head, tail = os.path.split(__file__)
        _p = os.path.normpath(f'{head}/data/json/json.txt')
        self.json_data = json.dumps(obj)
        self.write_file(_p, self.json_data)

    @staticmethod
    def file_cleaner():
        """Переносим обработанные файлы в архив"""

        head, tail = os.path.split(__file__)
        file_folder_list = {'url_id': ['data/html_page', 'data/archive/html_page'], }

        for i in file_folder_list.values():
            u1 = os.path.normpath(f'{head}/{i[0]}')
            u2 = os.path.normpath(f'{head}/{i[1]}')

            for file_folder in os.listdir(u1):
                if file_folder.endswith(".html"):
                    file_folder1 = os.path.normpath(f'{u1}/{file_folder}')
                    file_folder2 = os.path.normpath(f'{u2}/{file_folder}')
                    os.replace(src=file_folder1, dst=file_folder2)

    @staticmethod
    def open_file_csv(file_folder):
        head, tail = os.path.split(__file__)
        file_folder = os.path.normpath(f'{head}/data/{file_folder}')
        with open(file_folder, 'r', encoding='utf-8') as file:
            file_reader = csv.reader(file, delimiter=",")
            return (list(file_reader))


# file = WorkFolderFiles()
# file.find_file()
# print(file.list_file)
