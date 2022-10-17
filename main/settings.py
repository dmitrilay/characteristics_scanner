DEBUG = True


"""Настройки браузера"""
options_web = {
    'profile.managed_default_content_settings.javascript': 2,
    'profile.managed_default_content_settings.images': 2,
    'profile.managed_default_content_settings.mixed_script': 2,
    'profile.managed_default_content_settings.media_stream': 2,
    'profile.managed_default_content_settings.stylesheets': 2
}


"""Файловая система"""
FOLDERS = [
    'archive/html_page',
    'cat',
    'html_page',
    'json',
]


try:
    if DEBUG:
        from settings_local import *
    else:
        from settings_dev import *
except:
    print('settings_dev', 'settings_local', "файлы не найдены")

    """Авторизация"""
    url = 'https://online.smartlombard.ru/login/'
    username = ""
    password = ""

    """Авторизация на ch-shop.ru"""
    token = "111111111"

    """Данные для сайта"""
    PATH_NAME = 'smartlombard/v2/v2/v3'
    HOST = 'http://127.0.0.1:8000/'


"""Категории"""
CATEGORY_CSV = {
    'portativnyie-kolonki': 'Портативные-колонки',
    'smartfony': 'Смартфоны',
}
