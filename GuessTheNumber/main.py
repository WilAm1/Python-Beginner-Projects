"""What’s My Number?

Between 1 and 1000, there is only 1 number that meets the following criteria:

    The number has two or more digits.
    The number is prime.
    The number does NOT contain a 1 or 7 in it.
    The sum of all of the digits is less than or equal to 10.
    The first two digits add up to be odd.
    The second to last digit is even and greater than 1.
    The last digit is equal to how many digits are in the number.
    """


            

def isPrime(num):
    """Prime number is a natural number where the
    factors are only one and itself."""
    if type(num) != int:
        return False
    if num <=2:
        return False
    for n in range(3,int(num**.5+1 ),2):
        if num % n == 0 :
            return False
    return True

print(isPrime(523),'is it?')
for n in range(10,1001):
    n_string = str(n)
    if '1' in n_string or '7' in n_string:
        continue
    if sum([int(digit) for digit in n_string]) > 10:
        continue
    if ((int(n_string[0]) + int(n_string[1])) % 2 ==0):
        continue
    second  = int(n_string[-2])
    last = int(n_string[-1])
    if isPrime(n):
        if second %2 == 0 and second > 1:
            
            if int(n_string[-1]) == len(n_string):
                
                
                print(n)


