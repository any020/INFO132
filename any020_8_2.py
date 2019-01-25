
#Deler opp listen i ulike elementer. Hvert element blir en liste
def split_all(the_list, sep):
    index = 0
    while index < len(the_list):
        line = the_list[index]
        the_list[index] = line.split(sep)
        index = index + 1


def abbreviate(the_list):
    index = 0
    for insidelist in the_list:
        #det første elementet i hvert element til seg selv
        the_list[index] = insidelist[0]
        index += 1
    return the_list

def keep(the_list, target):
    #oppretter en kopi av den originale listen
    listekopi = the_list.copy()

    #ny liste basert på kopien du oppretter
    for keep_list in listekopi:
        if keep_list == target:
            pass
        else:
            the_list.remove(keep_list)
    return the_list


def main():


    filename = 'noder_50_50.csv'
    filename_open = open(filename, 'r')
    filename_check = filename_open.read()
    sep = "\t"
    the_list = filename_check.split('\n')
    split_all(the_list, sep)

    abbreviate(the_list)

    target = input("input 'male' or 'female':  ")
    keep(the_list, target)
    print(the_list)

if __name__ == '__main__':
    main()
