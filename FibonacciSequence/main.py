"""A program that deals with fibonacci sequence"""


def makeFibonacci(n):
    """Returns integer of the sum of fibonacci sequence. Initial sides are at 0 and 1."""
    n1 = 0
    n2 = 1
    for _ in range(n):
        n3 = n1 + n2
        n1 = n2
        n2=n3
    return n3

if __name__ == '__main__':
    """The program wil run if executed natively."""
    while True:
        number = int(input("Please input the number for iterations you want in integer only. : "))
        print(makeFibonacci(number))
        if input('Do you want to use the program again? Type "yes" to continue :  ').lower() == 'yes':
            continue
        else:
            break
