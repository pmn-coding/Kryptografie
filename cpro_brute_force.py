#brute force - 4 stelliger zahlencode

geheim = input("Zu Entschlüsselnder Text: ").upper()

for p in range(1000,10000):
    key = p
    
    keylist = []
    key = str(key)
    for i in range(len(key)):
        keyslice = slice(i,i+1,1)
        keylist.append(int(key[keyslice]))
    es =""
    count = 1
    for c in geheim:
        if c == "°":
            es += " "
        else:
            if count == 1:
                n = ord(c)
                m = n - keylist[0]
                if m > ord("Z"):
                    m += 26
                nm = chr(m)
                es += nm
                count += 1
            elif count == 2:
                n = ord(c)
                m = n - keylist[1]
                if m > ord("Z"):
                    m += 26
                nm = chr(m)
                es += nm
                count += 1
            elif count == 3:
                n = ord(c)
                m = n - keylist[2]
                if m > ord("Z"):
                    m += 26
                nm = chr(m)
                es += nm
                count += 1
            elif count == 4:
                n = ord(c)
                m = n - keylist[3]
                if m > ord("Z"):
                    m += 26
                nm = chr(m)
                es += nm
                count = 1
    print("Schlüssel: ",key)
    print("Entschlüsselt: ",es)
