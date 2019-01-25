from any020_11_2_network import Network                         # Importerer funksjoner fra networkfilen

def main():
    agent1 = input('Skriv agentnummer til agent 1: ')           # input 1
    agent2 = input('Skriv agentnummer til agent 2: ')           # input 2

    # Kjøreliste:
    new_network = Network()
    new_network.add_edge(agent1, agent2)                        # kan legge inn direkte input her: agent nummer 'space' antall venner
    connections = new_network.friends_of(agent1)                # antall venner
    friends = new_network.friends_of_these([agent1, agent2])    # venner tilknyttet

    # Printeliste:
    print(connections)
    print(friends)

if __name__ == '__main__':
    main()