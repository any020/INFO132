# Oppgave 1
import string

def check(filename, agents):
    filename_open = open(filename, 'r')
    filename_check = filename_open.read().split("\n")


    # variabeler for second_col og _third_col og alfabet
    alphabet = "abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"
    row_count = 0

    if len(filename_check) != agents:
        print("Expected", len(filename_check), " lines. Found", agents)

    # sjekker radene i filname
    for row in filename_check:
        col = row.split("\t")
        first_col = col[0]

        #if not row.inputequal('male') and not row.inputequal('female'):
        if first_col !='male' and first_col !='female':
            print(row,"First col does not start with male of female ")
        # har kolonne ikke 3 rader
        if not len(col) == 3:
            print(row, " line has not 3 column")
            break

        # variabler for 2 og 3 kolonne
        second_col = col[1]
        third_col = col[2]

        # er lengden på 2 og 3 kolonne mindre eller lik 2
        if len(second_col) < 2 or len(third_col) < 2:
            print('2 or more symbols is needed')

        # variabel for beggge kolonner
        both_col = third_col + second_col
        # sjekker om bokstavene finnes i alfabetet
        for letter in both_col:
            if letter not in alphabet:
                print(row,'contains the illegal character', letter)

        # variabel for å telle rader
        lower_second_col = second_col.lower()
        lower_third_col = third_col.lower()
        if lower_second_col == second_col and lower_third_col == third_col:
            print(row, ' has only lowercase characters')

        row_count += 1




def main():
    check('noder_50_50_feil_3.csv', 50)


if __name__ == '__main__':
    main()
