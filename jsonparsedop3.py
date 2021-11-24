import jsonparse
import json2xmldop1
import jsonparsewithre
import time

t = time.time()
for i in range(10):
    jsonparse.maintask()
print("10 заданий номер 1 выполнены за ", time.time()-t)

t = time.time()
for i in range(10):
    json2xmldop1.dop1()
print("10 заданий номер 2 выполнены за ", time.time()-t)

t = time.time()
for i in range(10):
    jsonparsewithre.dop2()
print("10 заданий номер 3 выполнены за ", time.time()-t)