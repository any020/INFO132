


class Successor():
    # Konstruktøren:
    def __init__(self, n, booboo):

        self.n = n
        self.booboo = booboo == 'y'


    #Eneste metode i klassen(Successor)
    def get_next(self):

        restartloop = True
        harloopet = False

        while restartloop:
            for i in range(0, self.n):
                result = str(i)
                if harloopet:
                    result = 'None'

                print('Number/None: ' + result)
                # sjekker om du vil quite loopen, om ikke fortsetter loopen å kjøre
                quitter = str(input("Enter anything to quit: "))
                if quitter == 'q':
                    restartloop = False
                    break

                if i == self.n - 1 and not self.booboo:
                    harloopet = True


def main():
    input_size = int(input("Skriv size: "))
    loopy = str(input("Loop [y/n]? : "))

    #

    #Kjøreliste
    n = Successor(input_size, loopy)
    n.get_next()

if __name__ == '__main__':
    main()