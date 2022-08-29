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
    def open_file_csv(file_folder):
        head, tail = os.path.split(__file__)
        file_folder = os.path.normpath(f'{head}/data/{file_folder}')
        with open(file_folder, 'r', encoding='utf-8') as file:
            file_reader = csv.reader(file, delimiter=",")
            return (list(file_reader))


# file = WorkFolderFiles()
# file.find_file()
# print(file.list_file)
