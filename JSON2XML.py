def subj(txt):
    return txt[1:len(txt)-1]
    
def superstrip(lis):
    lis1 = ""
    cnt = 0
    for i in lis:
        if i=="\"":
            cnt += 1
        if i not in [" ", "\n", "\t"] or (cnt%2)==1:
            lis1 += i
    return lis1

def getdict(txt):
    p = txt.find(":")
    key = txt[0:p]
    key = subj(key) if key[0]=="\"" else key
    value = txt[p+1:]
    value = subj(value) if value[0]=='"' else value
    return {key: value} 

def commadel(txt):
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    lis = []
    save = 0
    for i in range(len(txt)):
        cnt1 += 1 if txt[i]=="{" else -1 if txt[i]=="}" else 0
        cnt2 += 1 if txt[i]=="[" else -1 if txt[i]=="]" else 0
        cnt3 += 1 if txt[i]=="\"" else 0
        if txt[i]=="," and cnt1==0 and cnt2==0 and (cnt3%2)==0:
            lis.append(txt[save:i])
            save = i+1
    lis.append(txt[save:])
    return lis

def parse(dson):
    for i, k in enumerate(dson):
        v = dson[k]
        if v[0]=="[":
            v = subj(v)
            l = []
            for x in commadel(v):
                if x[0]=="{":
                    x = subj(x)
                    l.append(parse(getdict(x)))
                else:
                    l.append(x)
            dson[k] = l
    return dson
                        

f = open("schedule.json", "r", encoding="UTF-8")
json = ''.join(f.readlines()).strip()
print("8888888888888888888")
f.close()
dicy = {}
for x in commadel(subj(superstrip(json))):
    dicy = {**dicy, **getdict(x)}
print(parse(dicy))