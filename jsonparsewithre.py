import re
def subj(txt):
    m = re.search(r'^[\{\[\"](.*)[\}\]\"]$', txt)
    if m:
        return m[1]
    else:
        return txt
    
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
    m = re.search(r'^(.+?)\:(.+)$', txt)
    key = ""
    value = ""
    if m:
        key = m[1]
        key = subj(key) if key[0]=="\"" else key
        value = m[2]
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

def atom(txt):
    cnt =0
    for x in txt:
        if x=='"':
            cnt += 1 
        if x in ['{', '['] and cnt%2==0:
            return False
    return True


def parse(txt, t=0):
    ret = []
    if t==1:
        d = {}
        for x in commadel(txt):
            td = getdict(x)
            for i, k in enumerate(td):
                value = td[k]
                d[k] = value if atom(value) else parse(value)
        return d

    if t==2:
        for x in commadel(txt):
            if atom(x):
                ret.append(x)
            else:
                ret += (parse(x))
        return ret

    if txt[0]=='{':
        ret.append(parse(subj(txt), 1))
        return ret

    if txt[0]=='[':
        ret = parse(subj(txt), 2)
        return ret

def XMLing(parsed, add='', tag=''):
    ret = ''
    if isinstance(parsed, list):
        for x in parsed:
            if isinstance(x, dict):
                ret += XMLing(x, add, tag)
            else:
                ret += add+'<'+tag+'>'+x+'</'+tag+'>\n'
        return ret
    elif isinstance(parsed, dict):
        ret += '<'+tag+'>\n'+add if tag!='' else ''
        for x in parsed:
            if isinstance(parsed[x], dict):
                ret += XMLing(parsed[x], add, x)
            elif isinstance(parsed[x], list):
                ret += XMLing(parsed[x], add, x)
            else:
                ret += add+'<'+x+'>'+parsed[x]+'</'+x+'>\n'
        ret += '</'+tag+'>\n' if tag!='' else ''
    else:
        return parsed
    return ret

def toXML(txt):
    return '<root>\n' + XMLing(txt) + '</root>'
    #return '<?xml version="1.0" encoding="UTF-8" ?>\n' + XMLing(txt)
                        

def dop2():
    f = open("c:/Users/Dmankus/Documents/Labs/inf/Lab4/schedule.json", "r", encoding="UTF-8")
    json = ''.join(f.readlines()).strip()
    f.close()
    parsed = parse(superstrip(json))
    return toXML(parsed)