#<> 2 Mynt og Kron- spill
from random import randrange

# Terningspill.

# <>Ber brukeren tippe ett tall mellom 1-6 (1)
tippetTekst = input("Tipp ett tall(1-6)")

# <>Input tallet (2)
tippetTall = int(tippetTekst)

# <> Tilordner vi et tilfeldig heltall mindre enn 7 (0 eller 1).
faktiskTall = randrange(1,7)

# <>Sjekker om input-tallet stemmer overens med randRange(true,false)  (3)
tippetRiktig = tippetTall == faktiskTall

print("Du tippet")
print(tippetTall)
print("Riktig tall var")
print(faktiskTall)
print("Hadde du rett?")
print(tippetRiktig)
