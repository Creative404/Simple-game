import time
from random import randint






while True:
    time.sleep(0.3)
    g = True
    a=0

    while g:

        time.sleep(0.3)

        aa = randint(0,100)

        print(a)

        a += 0.5

        if a == 5:
            a += 0.5
            print(999999999999999999999999999999)
            g= False


