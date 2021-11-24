from json2xml import json2xml

f = open("c:/Users/Dmankus/Documents/Labs/inf/Lab4/schedule.json", "r", encoding="UTF-8")
json = ''.join(f.readlines()).strip()
f.close()
print(json2xml.Json2xml(json).to_xml())