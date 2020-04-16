import sys


def usage():
    print("Usage: python operations.py <number1> <number2>\
            \nExample:\
            \n    python operations.py 10 3")


def operations():
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        print("Sum:         ", a + b)
        print("Difference:  ", a - b)
        print("Product:     ", a * b)
        print("Quotient:    ", a / b)
        print("Remainder:   ", a % b)
    except ValueError:
        print("InputError: only numbers\n")
        usage()
    except ZeroDivisionError:
        print("Quotient:     ERROR (div by zero)")
        print("Remainder:    ERROR (modulo by zero)")
    except IndexError:
        usage()


def main():
    n = 0
    for i in sys.argv:
        n += 1
    if n >= 4:
        print("InputError: too many arguments\n")
        usage()
        exit()
    operations()


if __name__ == '__main__':
    sys.exit(main())
