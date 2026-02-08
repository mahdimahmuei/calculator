
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
    print('5. Exit')
    c = input('choose: ')
    a = int(input('enter number 1: '))
    b = int(input('enter number 2: '))

    while True:
        try:
            match c:
                case '1':
                    print(adder(a, b))
                case '2':
                    print(sub(a, b))
                case '3':
                    print(multiply(a, b))
                case '4':
                    print(divider(a, b))
                case '5':
                    print('exsiting...')
                    exit(0)
        except Exception as e:
            print('ERROR:', e)












if __name__ == "__main__":
    main()
