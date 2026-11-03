import re
haslo=input("Podaj haslo, ktore chceesz sprwadzic: ")
strength=0
if len(haslo)>=8:
    print("Haslo ma bezpieczna dlugosc")
    strength+=1
else:
    print("Haslo powinno miec dlugosc co najmniej 8!")
if re.search(r"\d",haslo):
    print("Haslo posiada cyfry, jest dobrze!")
    strength+=1
else:
    print("Dodaj cyfry do hasla!!")
if re.search(r"[a-z]",haslo):
    if re.search(r"[A-Z]",haslo):
        print("Halso zawiera duze i male litery !")
        strength+=1
    else:
        print("Dodaj wielkie litery, pomieszaj je !")
else:
    print("Dodaj male liteyr, pomieszaj je!")
if re.search(r"[!@#$%^&*(),.?_]",haslo):
    print("Haslo posiada znaki specjalne")
    strength+=1
else:
    print("Dodaj znaki specjalne!")

print("-----------------------------------")
print("Podsumowanie")

print(f"Twoje haslo zdobylo {strength}pkt na 4")

if(strength==4):
    print("Haslo jest BARDZO SILNE! Dobra robota!")
if(strength==3):
    print("Haslo jest SREDNIE, ale mozna je jeszcze ulepszyc!")
if(strength==2):
    print("Haslo jest SLABE, latwo je zlamac - lepiej je popraw!")
if(strength<=1):
    print("Haslo jest TRAGICZNE, szybko je zmien !!!!!")
