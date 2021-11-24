from json import loads
from dicttoxml import dicttoxml

def dop1():
    f = open("c:/Users/Dmankus/Documents/Labs/inf/Lab4/schedule.json", "r", encoding="UTF-8")
    json = ''.join(f.readlines()).strip()
    f.close()
    parsed = loads(json)
    return dicttoxml(parsed).decode("UTF-8")