# 동기(Syncronous)
# A 작업 -> B 작업

import time

def hello():
    time.sleep(3)
    print("hello")

hello() 

