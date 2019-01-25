
# Finner agentnummer
def find_agent(
        search, noder_reader
        ):

    agents = dict()
    count_agents = 0
    noder = noder_reader.split('\n')

    #går gjennom noderfilen
    for line in noder:
        name = line.split('\t')
        agents[count_agents] = 'Agent ' + name[1] + ' ' + name[2] + ' ' + name[0]
        count_agents += 1
    # sjekker om key stemmer med brukerinput
    for key in agents:
        # sjekker stemmer over med input
        if key == search:
            agent = agents.get(search) + ' ' + str(key)
            print(agent)
            return agent

# Finner venner av agenten
def find_friends(
        kanter, noder,  search
        ):
    count_friends = 0
    friends = dict()
    kanter_reader = kanter.split('\n')
    noder_reader = noder.split('\n')
    find_friends_list = []
    friend_id = []

    # sjekker noder filen, oppretter dict, friendslist
    for line in noder_reader:
        friend = line.split('\t')
        friends[count_friends] = friend[1] + ' ' + friend[2] + ' (' + friend[0] + ') '
        count_friends += 1
    count_friends = 0

    # Går gjennom kanterfilen
    for line in kanter_reader:
        friend = line.split('\t')
        #sjekker om venn har samme value i kanterfilen
        if friend[0] == str(search) or friend[1] == str(search):
            count_friends += 1
            #om venn har samme value som input legges vennen til
            if friend[0] == str(search):
                find_friends_list.append(friends[int(friend[1])])
                friend_id.append(friend[1])
            elif friend[1] == str(search):
                find_friends_list.append(friends[int(friend[0])])
                friend_id.append(friend[1])
    return find_friends_list


    print(count_friends)

# Finner venners venner
def friend_of_friends(
        kanter, search
        ):

    kanter_reader = kanter.split('\n')
    friend_id = []

    for line in kanter_reader:
        friend = line.split('\t')
        # Sjekker og legger til venners id i friend_id listen
        if friend[0] == str(search) or friend[1] == str(search):
            if friend[0] == str(search):
                friend_id.append(friend[1])
            elif friend[1] == str(search):
                friend_id.append(friend[1])
    return friend_id

# Finner venners navn og kjønn
def find_friendname(
        noder, friend_id
        ):

    noder_reader = noder.split('\n')
    line = noder_reader[int(friend_id)]
    friend = line.split('\t')

    return friend[1] + ' ' + friend[2] + ' (' + friend[0] + ') '

# Hovedfunksjon
def main():
    search = int(input('Skriv agentID: '))

    noder = open('noder_25_3.csv', 'r', encoding='UTF-8')   # Åpner Noderfilen
    noder_reader = noder.read()                             # Leser Noderfilen
    print('Nodefil : noder_25_3.csv')                       # Skriver ut hvilken fil som leses

    kanter = open('kanter_25_3.csv', 'r', encoding='UTF-8') # Åpner Kanterfilen
    kanter_reader = kanter.read()                           # Leser Kanterfilen
    print('Kantfil : kanter_25_3.csv')                      # # Skriver ut hvilken fil som leses

    naboer = open('naboer_25_3.csv', 'r', encoding='UTF-8') # Åpner Nabofilen
    nabo_reader = naboer.read()                             # Leser Nabofilen
    print('Nabotfil : naboer_25_3.csv')                     # Skriver ut hvilken fil som leses

    #Kjører de ulike funksjonen:

    find_agent(search, noder_reader)                    # finner agentnummer
    find_friends(kanter_reader, noder_reader, search)   # liste med venner
    find_friends(nabo_reader, noder_reader, search)     # liste med naboer
    find_friends(kanter_reader, noder_reader, search)   # liste med naboers venner

    print('\n')

    # venners venner:
    friends = friend_of_friends(kanter_reader, search)
    searchName = find_friendname(noder_reader, search)
    # Søker etter venners id
    for id in friends:
        name = find_friendname(noder_reader, id)
        friend_of_friend = friend_of_friends(kanter_reader, id)
        for friendID in friend_of_friend:
            friendName = find_friendname(noder_reader, friendID)
            if search != friendID and id != friendID:
                print(f'{searchName} kjenner {name} som kjenner {friendName} som ikke kjenner {searchName}')
                break

    #Variabler for vennelisten og nabolisten:
    venneListe = find_friends(kanter_reader, noder_reader, search)  # Listen av venner
    naboListe = find_friends(nabo_reader, noder_reader, search)     # Liste av naboer

    newList = []                                                    # venneliste + naboliste = newlist

    print('\nVenner: ')
    for i in venneListe:
        print(i)

    print('\nNaboer: ')
    for j in naboListe:
        print(j)
    print('\n')

    # sammenligner lister med naboer og venner:
    for nabo1 in venneListe:
        # om navnet er å finne i nabolisten, legges det til
        if nabo1 in naboListe:
            newList.append(nabo1)
    print('Venner i samme by: ', len(newList), '\n')


    # venner som er venner, men ikke med første agent du søker på:
    naboMenIkVenn = []
    for name in naboListe:
        if name not in venneListe and name != searchName:
            naboMenIkVenn.append(name)

    print(f'{naboMenIkVenn[0]} og {naboMenIkVenn[1]} bor samme sted som {searchName} men de er ikke venner. ')


if __name__ == '__main__':
    main()
