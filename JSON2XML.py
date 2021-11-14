def subJ(txt, simb="{}"):
    up = 0
    dow = len(txt)
    check = False
    check2 = False
    cnt = 0
    if len(simb)==2:
        check2 = True
    for x in range(len(txt)):
        if txt[x]==simb[0]:
            if check:
                cnt+=1
            else:
                up = x 
                check = True
        if check2:
            if txt[x] == simb[1]:
                if cnt>0:
                    cnt-=1
                else:
                    dow = x
                    break
    return (up+1, dow-1)
    

f = open("schedule.json", "r", encoding="UTF-8")
json = ''.join(f.readlines()).strip()
print("8888888888888888888")
f.close()
up, dow = subJ(json)
print(list(map(str.strip, json[up: dow-up].split(","))))
