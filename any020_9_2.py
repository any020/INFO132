import csv

def compile_names():

    data = {}
    counter = 0

    #åpner filen
    with open('noder_15_13.csv', 'r', encoding='utf=8') as filename:
        reader = csv.reader(filename, delimiter='\t')
        #Iterer gjennom radene i kanter, og legger de i 'data'
        for row in reader:
            name = row[1] + ' ' + row[2]
            data[counter]= name
            counter += 1

    filename.close()

    return data


def compile_friends_list():
    #nye dict
    dict2 = {}
    file2 = open('noder_15_13.csv', encoding='UTF-8')

    names = file2.read().split("\n")
    file2.close()

    data = compile_names()
    for value in data.values():
        dict2[value] = 0

    file = open('kanter_15_13.csv', encoding="UTF-8")
    file_content = file.read().split("\n")
    file.close()

    for line in file_content:
        values = line.split("\t")
        agent1 = names[int(values[0])].split('\t')
        agent2 = names[int(values[1])].split('\t')
        agent1 = agent1[1] + " " + agent1[2]
        agent2 = agent2[1] + " " + agent2[2]
        dict2[agent1] += 1
        dict2[agent2] += 1

    print(dict2)


def main():
    compile_names()
    compile_friends_list()

if __name__ == '__main__':
    main()