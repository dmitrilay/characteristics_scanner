from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import os
from time import sleep
import json

from selenium.webdriver.common.action_chains import ActionChains

options_web = {
    # 'profile.managed_default_content_settings.javascript': 2,
    'profile.managed_default_content_settings.images': 2,
    # 'profile.managed_default_content_settings.mixed_script': 2,
    'profile.managed_default_content_settings.media_stream': 2,
    'profile.managed_default_content_settings.stylesheets': 2,
}


class parserSpecMVM():
    def __init__(self, name, url):
        self.web = self.browser_ch()
        self.name = name
        self.url = url

    def browser_ch(self):
        # Запуск браузера
        address, name_file = os.path.split(__file__)
        options = Options()
        options.add_experimental_option('prefs', options_web)
        options.binary_location = "C:\\\Programs\\Chrome\\\Application\\chrome.exe"
        name_ch = os.path.normpath(f'{address}/chromedriver/chromedriver.exe')
        chrome = webdriver.Chrome(name_ch, options=options)
        return chrome

    def action(self):
        # Действия на странице в браузере
        self.web.get(self.url)
        sleep(10)
        _char = self.web.find_elements(By.CSS_SELECTOR, ".characteristics--link")
        step = 1000
        for _i in range(10):
            self.web.execute_script(f"window.scrollTo(0, {step*_i})")
            sleep(3)
            _char = self.web.find_elements(By.CSS_SELECTOR, ".characteristics--link")
            if _char:
                _char[0].click()
                sleep(10)
                break

    def save_html(self):
        pageSource = self.web.page_source
        head, tail = os.path.split(__file__)
        fix_name = self.name.replace('/', '+')
        full_name = os.path.normpath(f'{head}/data/html_page/{fix_name}.html')
        with open(full_name, 'w', encoding='utf-8') as file:
            file.write(pageSource)


def startParserSpecMVM(entrance):
    for key, value in entrance.items():
        new_web = parserSpecMVM(name=key, url=value['url'])
        new_web.action()
        new_web.save_html()


# entrance = {
#     'Xiaomi Redmi 9A 32GB Peacock Green': {
#         'url': 'https://www.mvideo.ru/products/smartfon-xiaomi-redmi-9a-32gb-peacock-green-30051226',
#         'category': 'smartfony'},
#     'Xiaomi Redmi 10C 4GB+64GB Mint Green': {
#         'url': 'https://www.mvideo.ru/products/smartfon-xiaomi-redmi-10c-4gb64gb-mint-green-30063082',
#         'category': 'smartfony'}
# }

# startParserSpecMVM(entrance)
