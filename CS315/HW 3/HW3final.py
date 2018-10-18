from random import *
from math import *

#I: number of bits hardcoded into main
#O: a random binary number as a list
def generate_random(n):
    new_number = []
    new_number.append(1)    
    
    for i in range(n-1):
        new_bit = randint(0, 1)
        new_number.append(new_bit)
    return new_number

#I: a binary number as a list
#O: a boolean, True if the number is prime, False if it is not
#this uses 3^(N-1)modN = 1 modN form
def test_primality_FERMAT(check):
    x = 3
    N = decimal(check)
    check[0] = 0
    y = list(reversed(check))
    z = 1
    for i in range(0, len(y)):
        z = (z**2)%N
        if (y[i] == 1):
            z = (z*x)%N 
    check[0] = 1
    if (z == 1):
        return True
    else:
        return False

#I: a presumably prime binary number as a list
#O: a definitive answer as to whether or not it is prime
def test_primality_BRUTE(check):
    N = decimal(check)
    for x in range(2, round(sqrt(N))):
        check[0] = 0
        y = list(reversed(check))
        z = 1
        for i in range(0, len(y)):
            z = (z**2)%N
            if (y[i] == 1):
                z = (z*x)%N
        if (z != 1):
            check[0] = 1
            return False
    check[0] = 1
    return True  

#I: a binary number as a list
#O: a decimal value equilvalent to the original binary number list
def decimal(list_to_dec):
    decimal = 0
    for i in range(len(list_to_dec)):
        decimal += list_to_dec[i]*(2**i)        
    return decimal
    
def main():
    n = 16                     #SET THE NUMBER OF BITS HERE**********
    before_prime = 0
    primes = []
        
    while(len(primes) < 100): #getting 100 presumed primes
        number = generate_random(n)
        if (len(primes) < 1):
            before_prime += 1
        if (test_primality_FERMAT(number) == True):  #testing for primality
            print(decimal(number))
            primes.append(number)
            
    #testing for primality - BRUTE
    false_prime_counter = 0
    for i in range(len(primes)):
        if (test_primality_BRUTE(primes[i]) == False):
            false_prime_counter += 1 
    print("tries before prime ", before_prime)
    print("false primes: ", false_prime_counter)    
        
#calculating the runtime
import time
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))

wait = input("PRESS ENTER TO CONTINUE.")
