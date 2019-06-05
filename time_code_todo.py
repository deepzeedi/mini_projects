# Выполнение кода по времени
import datetime


# код


def realtim():
    global realtime
    now = datetime.datetime.now()
    realtime=str(now.hour)+":"+str(now.minute)


while True:
    realtim()
    if realtime == '11:22':
        try:
            # cюда выполнение кода
            print(realtime)
            break
        except:
            pass
    else:
        pass