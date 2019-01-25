
# Nettverk-klassen
class Network():
    def __init__(self):

        csvfile = open('kanter_5_1.csv', encoding='UTF-8')      # åpner kanter filen
        self.new_agent_network = csvfile.read().split('\n')     # leser filen og splitter på ny linje

    def add_agent(self, agent1, agent2):                        # Ny agent i nytt nettverk
        self.new_agent_network.append(agent1)                   # legger til agent 1
        self.new_agent_network.append(agent2)                   # legger til agent 2

    def friends_of(self, agent1):                               # finner venner/vennen til agent
        connections = []                                        # ny variabel for venner som blir funnet

        for line in self.new_agent_network:                     # loop som finner venner i det nye nettverket
            friend = line.split(' ')
            if friend[0] == agent1:                             # sjekker om venn tilhører agent
                connections.append(friend[1])                   # legger til funnet venn i oversikten

        return connections

    def friends_of_these(self, listoffriends):                  # liste med agentens venn sine venner
        friend_list = []
        for line in self.new_agent_network:
            friend_splitter = line.split(' ')
            for friend in listoffriends:                        # finner venn og legger den til i listen
                if friend == friend_splitter[0] or friend == friend_splitter[1]:
                    friend_list.append(friend_splitter[0])

        seen = set()
        unike = []

        for kopi in friend_list:                                   # sjekker for duplikater
            if kopi not in seen:
                unike.append(kopi)
                seen.add(kopi)

        return unike
