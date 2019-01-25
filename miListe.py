minListe = [5,2,-4,2,-1,0,2,-2,3,0,7]

def funksjon1():
    sum = 0
    for number in minListe:
        if number > 0:
            continue
            sum += number


def funksjon2():
    neg_num = []
    for i in minListe:
        if i<0:
            neg_num.append(i)
            return neg_num
        break

def funksjon3():
    oddetall_numbers = 0
    negative_numbers = 0
    for n in minListe:
        if n % 2 == 0:
            oddetall_numbers += 1
        elif n < 0:
            negative_numbers += n

        return [oddetall_numbers, negative_numbers]


def main():
    funksjon1()
    funksjon2()
    funksjon3()


if __name__ == '__main__':
    main()