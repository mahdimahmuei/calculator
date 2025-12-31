
def adder(a,b):
    return a+b

def multiply(a, b):
    return a * b

def divider(a,b):
    return a/b


def main():
    print('1. Add')
    print('2. Sub')
    print('3. Multiply')
    print('4. Divide')
    c = input('choose: ')
    a = int(input('enter number 1: '))
    b = int(input('enter number 2: '))

    match c:
        case '1':
            print(adder(a, b))
        case '2':
            print(sub(a, b))
        case '3':
            print(multiply(a, b))
        case '4':
            print(divider(a, b))













if __name__ == "__main__":
    main()
