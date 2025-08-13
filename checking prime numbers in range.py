def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,int(n**0.5),2):
        if n % i == 0:
            return False
    return True

def num_range(start,end):
    """checking prime numbers in range from start to end"""
    primes=[]
    for num in range(start,end+1):
        if is_prime(num):
            primes.append(num)
    return primes
print(num_range(1,100))