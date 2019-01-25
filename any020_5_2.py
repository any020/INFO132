def hello():
  print('''Funksjon 1:
    Returnerer summen av alle positive tall i listen som er =  21

    Funksjon 2:
    Returnere summen av alle tallene frem til første null-tall.
    I minListe returnerer den 4.

    Funksjon 3:
    Funksjonen skal returnere antall tall i listen som er enten et oddetall,
    negativt, eller begge''')
hello()

#Egenretting, endret sum til total(?)

def funksjon1(minListe):
    total = 0
    for number in minListe:
        if number > 0:
            total += number
        else:
            continue
    return (total)


def funksjon2(minListe):
    count = 0
    for teller in minListe:
        if teller == 0:
            break
        else:
            count += teller
    return (count)


def funksjon3(minListe):
    count = 0
    x = 0

    for number in minListe:
        if number == 0:
            x = x + 1
            if x == 2:
                break

        elif number<0 or number % 2 == 1:
            count = count + 1

    return count

def main():
    minListe = [5, 2, -4, 2, -1, 0, 2, -2, 3, 0, 7]
    print(hello)
    print(funksjon1(minListe))
    print(funksjon2(minListe))
    print(funksjon3(minListe))


if __name__ == '__main__':
    main()





















