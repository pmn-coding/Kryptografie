#Entschlüsselung mit einem 4 stelligen zahlencode

geheim = input("Zu Entschlüsselnder Text: ").upper()
key = int(input("Entschlüsselungszahl eingeben: "))
while not len(str(key)) == 4:
    print("Invalid length")
    key = int(input("Entschlüsselungszahl eingeben: "))
    
keylist = []
key = str(key)
for i in range(4):
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
print(es)
