from hangman import correct_guess


losning = 'hangman'

forsok = 'efgh'

neste = ''

def main():
    neste = input('Skriv ett tegn: \n')

    if correct_guess(losning,forsok, neste) == None:
        print('Ikke gyldig tegn')
    elif correct_guess(losning, forsok, neste) == True:
        print('Riktig')
    else:
        print('Du gjettet feil')

if __name__ == '__main__':