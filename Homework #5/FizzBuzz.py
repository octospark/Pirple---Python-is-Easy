"""
The program checks every number from 1 to 100 first if it is a prime number
then if it both divides 3 and five and after that if it divides one of them.
In each case a special message is printed.
"""

def isPrime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True



for i in range(1, 101):
    if isPrime(i):
        print("Prime")
    elif i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

        
