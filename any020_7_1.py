# Oppgave 1: Skrive filer

alphabet = "abcdefghijklmnopqrstuvwxyzæø˚a"


def legal_filname(entry):
    for letter in entry:
        if letter not in alphabet:
            return False

    return True


def write_message(filename):
    entry = input("Navngi fil: ")

    fhand = open(filename)
    while True:
        if entry == input(entry):
            entry == " "
        if entry == "**":
            break
    else:
        return ("\n")


    fhand.write = input(entry("This is line %d\r\n" % ("\n")))
    fhand.close()



def main():
    entry = input("Skriv noe her: ")

    print(legal_filname(entry))
    print(write_message(filename))

if __name__ == '__main__':
    main()

