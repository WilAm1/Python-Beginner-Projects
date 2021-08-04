"""A program that deals with fibonacci sequence"""


def makeFibonacci(n):
    n1 = 0
    n2 = 1
    for _ in range(n):
        n3 = n1+n2
        n1 = n2
        n2=n3
    return n3

result = makeFibonacci(6)
print(result)

