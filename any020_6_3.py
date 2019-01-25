import re
s = input("Skriv et uttrykk med paranteser: ")


def parChecker():
    if re.match('^[(-)]*$', s ):
        dybde = 0

        for entry in s:
            if entry == '(':
                dybde += 1
            elif entry == ')':
                dybde -= 1
            if dybde < 0:
                break
        if dybde == 0:
            print("Uttrykket er balansert")
        else:
            print("Uttrykket er ubalansert")
    else:
        print("Teksten er ugyldig!")




def main():
    parChecker()

if __name__ == '__main__':
    main()