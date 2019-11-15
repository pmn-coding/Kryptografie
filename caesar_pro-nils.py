#Verschlüsselung mit einem 4 stelligen zahlencode

import string as s

def caesar(w, key):

    keylist = []
    key = str(key)
    for i in range(4):
        keyslice = slice(i,i+1,1)
        keylist.append(int(key[keyslice]))


    sp = s.punctuation
    vs = ""

    w = w.replace("Ä","AE")
    w = w.replace("Ü","UE")
    w = w.replace("Ö","OE")
    w = w.replace("ß","SS")

    count = 1
    for c in w:
        if c in sp:
            vs += ""
            print("True")
        else:
            if c == " ":
                vs += "°"       #Mit dem ° Zeichen werden Leerzeichen markiert wenn nicht gewünscht einfach anstatt dieser Zeile folgendes einsetzen: vs += ""
            else:
                if count == 1:
                    n = ord(c)
                    m = n + keylist[0]
                    if m > ord("Z"):
                        m -= 26
                    nm = chr(m)
                    vs += nm
                    count += 1
                elif count == 2:
                    n = ord(c)
                    m = n + keylist[1]
                    if m > ord("Z"):
                        m -= 26
                    nm = chr(m)
                    vs += nm
                    count += 1
                elif count == 3:
                    n = ord(c)
                    m = n + keylist[2]
                    if m > ord("Z"):
                        m -= 26
                    nm = chr(m)
                    vs += nm
                    count += 1
                elif count == 4:
                    n = ord(c)
                    m = n + keylist[3]
                    if m > ord("Z"):
                        m -= 26
                    nm = chr(m)
                    vs += nm
                    count = 1
    
    return vs
klar = input("Zu Verschlüsselndes Wort oder Text: ").upper()
verschiebung = int(input("Verschiebungszahl (Länge 4 Stellen) : "))
while not len(str(verschiebung)) == 4:
    print("Invalid length")
    verschiebung = int(input("Verschiebungszahl (Länge 4 Stellen) : "))
else:
    geheim = caesar(klar, verschiebung)
    print(geheim)
