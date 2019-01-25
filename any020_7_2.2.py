

def search_agents(csvfile, agentID):
    #sjekker om agentID finnes i filen
    csv_info = csvfile.read()
    agent_friends = 0

    #finnes ikke agenten
    if agentID not in csv_info:
        print("Can´t find agent")
    else:
        #går gjennom radene for å finne agentID
        for row in csv_info:
            if row == agentID:
                agent_friends += 1
        print("Agent",  agentID, "has", agent_friends, "friends")



def main():
    #variabler
    networkSIZE = input("Nettverk størrelse: ")
    networkID = input("Nettverks ID: ")
    agentID = input("Skriv agentID: ")

    csvfile = 'kanter_' + networkSIZE + '_' + networkID + '.csv'

    #Prøver om inputen stemmer med filnavnet
    try:
        csvfile = open(csvfile)
        print('kanter_' + networkSIZE + '_' + networkID + '.csv')
    #Om ikke inputen stemmer med filnavnet
    except ValueError:
        print("Could not find kanter_" + networkSIZE + "_" + networkID + ".csv")

    search_agents(csvfile, agentID)


if __name__ == '__main__':
    main()