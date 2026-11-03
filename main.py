import re
haslo=input("Podaj haslo, ktore chceesz sprwadzic: ")
if len(haslo)>=8:
    print("Haslo ma bezpieczna dlugosc")
else:
    print("Haslo powinno miec dlugosc co najmniej 8!")