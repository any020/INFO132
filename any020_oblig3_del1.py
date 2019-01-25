from random import randrange

modus = 2
# én variabel: helltalls variabel modus med verdi 2
spor = randrange(modus)
# modus :: int = 2; spor (int) har verdi 0 eller 1


if spor:
    # modus er av typen int(integer) og har verdi = 2
    # spor er av typen int(integer) og har verdi = 1   < 1 >
    svar = input("Skriv et tall mindre enn 10:\n")
    # svar er lik, input i spor, som er av typen int og har verdien = 1
    # modus er av typen int(integer) og har verdi = 2  < 2 >

    try:
        # svar = #svar er lik, input i spor, som er av typen int og har verdien = 1
        # modus er av typen int(integer) og har verdi = 2  < 3 >
        svar = float(svar)

        # svar er type float, og float er, spor type:int verdi = 1,
        # modus type: int verdi = 2  < 4 >
        if 0 <= svar and svar < 10:
            print("Ok!")
        else:
            print("Nei!")
            # svar er type float, verdi = <0 eller >10, spor type_ int verdi = 1,
            # modus type:int verdi = 2 < 5 >

        # svar er type float, verdi er lik <=0 eller <10, spor type:int verdi = 1,
        # modus type:int verdi = 2 < 6 >
    except:
        # svar er av typen: str(string), spor type:int verdi = 1,
        # modus type:int verdi = 2 < 7 >
        print(svar, " er ikke et tall.")
else:
    #spor type:int verdi = 0, modus type:int verdi = 2 < 8 >
    modus = spor * modus
    #spor type:int verdi = 0, modus type:int verdi = 0 < 9 >
