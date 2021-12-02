import concurrent.futures
import threading
import math

# def odlicz():
#     for x in range(1,6):
#         print(x)
#
# t1 = threading.Thread(target=odlicz)
# t2 = threading.Thread(target=odlicz)
# t1.start()
# t2.start()

with concurrent.futures.ThreadPoolExecutor() as ex:
    t1 = ex.submit(math.radians, 180)
    t2 = ex.submit(math.sqrt, 36)
    print(t1.result())
    print(t2.result())

print(math.sqrt(36))