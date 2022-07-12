#5. Generate the largest prime number smaller than a given natural number n. If such a number does not exist, a message should be displayed.

def prime(n):
    """ The function tests if a given number n is prime or not
    :param n: natural number n
    :return: 1 if the number is prime and 0 otherwise
    """
    if n==2:
        return 1
    if n<=1 or n%2==0:
        return 0
    for i in range(n-1,2,-1):
        if n%i==0:
            return 0
    return 1



def search (n):
    """
    The function searches for the largest prime number smaller than a given number n
    :param n: natural number n
    :return: 1 if the prime number smaller than n exists and 0 otherwise
    """
    for i in range(n-1,1,-1):
        if prime(i)==1:
            return i
    return 0

if __name__ == '__main__':
    n = input("Citeste n = ")
    x = search(int(n))
    if x == 0:
        print('there is no prime number smaller that '+str(n))
    else:
        print(x)


