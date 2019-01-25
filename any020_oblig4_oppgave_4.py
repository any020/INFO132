#fibonacci

def fibonacci(n):
    if n == 0:
        return  1
    if n == 1:
        return  1

    return fibonacci(n-2) + fibonacci(n-1)

def main():
    try:
        tall = int(input("Tall: "))
        fibonacci(tall)
        print(fibonacci(tall))
    except:
        print(("Må være positivt heltall"))

if __name__ == '__main__':
    main()




