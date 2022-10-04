"""version 0.1.0"""
import threading
import time
from main import auto


while True:
    print('Поток запущен')
    _th = threading.Thread(target=auto, args=(), name='thr-1')
    _th.start()
    _th.join()
    time.sleep(60)
