import sys
#Program som skriver været om du befinner deg i USA eller Norge, om ikke er
#tjenesten utilgjengelig

#variabler
født = input('Hvor kommer du fra?\n')
nå = input('Hvor er du nå?\n')
nå = nå.lower()
født_og_nå = ("Du får gradene ")
usausa = ("fahrenheit")
nornor = ("celcius")
# print variabler
temp = int(input('Hvordan er værmeldingen?\n'))
melding = ('Værmeldingen er: ')
ukjent = ('Dette stedet kjenner jeg ikke til. Beklager\n')

#Befinner du deg i Norge, skrives værmeldingen i C
if født == 'norge' and nå == 'norge':
    print(født_og_nå + nornor)

elif født == 'usa' and nå == 'usa':
    print(født_og_nå + usausa)

if nå == 'norge':
    temp = (temp)
    print(melding,temp)

#Befinner du deg i USA, skriver temp i F
elif nå == 'usa':
    temp = temp * 9 / 5 + 32
    print(melding,temp)


#Om du ikke befinner deg hverken i Norge eller USA, skrives ukjent
else:
    print(ukjent)


    
    
    







        

                 
    
    
    
    
    









    

    
        









    
    
    
    

   






    




