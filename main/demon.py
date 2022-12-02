"""version 0.1.0"""
import threading
import time
from main import auto

PAUSE = 120


def timer():
    print(f"Пауза {PAUSE} секунд")
    time.sleep(PAUSE)
    print("Запуск")
    for t in range(1, 10):
        print(f' -- {t} -- ')
        time.sleep(1)


while True:
    try:
        print('Поток запущен')
        _th = threading.Thread(target=auto, args=(), name='thr-1')
        _th.start()
        _th.join()
        timer()
    except:
        print('Ошибка')
