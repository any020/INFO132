table = "female\tIngelin\tAleksandersen\nmale\tJohnny\tDigre\nmale\tOsman\tBremseth\nfemale\tCathrine\tDagestad\nfemale\tTirill\tBakker"



def show_table():
    print(table)

def show_every_cell(table):
    element = ''
    row_nr = 0
    cell_nr = 0

# Går gjennom radene i tabellen
    #Legger til rad om ikke \n
    for row in table:
        if row != "\n":
            element += row
        #Neste rad om element ("\t")
        else:
            element = element.split("\t")
            for cell in element:
                print("Row: ", row_nr, " ", "Col: ", cell_nr, " ", "Cell: ", cell)
                cell_nr += 1
            row_nr += 1
            element = ''




def main():
    show_table()
    show_every_cell(table)


if __name__ == "__main__":
    main()