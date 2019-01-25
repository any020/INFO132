
alphabet = "abcdefghijklmnopqrstuvwxyzæøå ?"
entry = input("Skriv noe: ")
entry_number = int(input("Skriv tall: "))


def clean_text():
    for x in entry:
        if x not in alphabet:
            entry = entry.replace(x, "?")


def symbol_add(symbol, key):
    index = 0
    new_symbol = ''

    for x in alphabet:
        if x == symbol:
            new_symbol = alphabet[(index + key) % len(alphabet)]
        index += 1
    return new_symbol



def cipher(data, key):
    new_data = ''
    for symbol in data:
        if symbol not in alphabet:
            print("ugyldig symbol")
            break
        else:
            new_data = new_data + symbol_add(symbol, key)

    return new_data



def main():

    print(cipher(entry, entry_number))


if __name__ == '__main__':
    main()