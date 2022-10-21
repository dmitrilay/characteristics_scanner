DEBUG = False


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


if DEBUG:
    from settings_local import *
else:
    from settings_dev import *


"""Категории"""
CATEGORY_CSV = {
    'portativnyie-kolonki': 'Портативные-колонки',
    'smartfony': 'Смартфоны',
    'portativnaya-akustika': 'Портативные-колонки',
    'mobilnyie-telefonyi': 'Мобильные-телефоны',
    'fitnes-brasletyi-i-chasyi': 'Фитнес-браслеты',
    'naushniki': 'Наушники',
}
