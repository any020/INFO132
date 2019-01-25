#Oppgave 2
#1.Primærminnet
# 2.“Alt” som en programmerer gjør både koden og dataene ligger i RAM(Primærminnet)
# men selve Python-filen ligger ikke lagret i primærminnet(rettelse)
# 3.Tolker

#Oppgave 3
#Alternativ A

#Verdi X, skriver X
x = 2
print(x)

#Ny kode, bytter X og Y
x = 3
y = 2

def swap(x, y):
    nyVerdi = x
    x = y
    y = nyVerdi

    swap(x, y)
    
print(x,y)


#Verdien Y, skriver Y
y = 3
print(y)


