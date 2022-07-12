#10. The palindrome of a number is the number obtained by reversing the order of its digits (e.g. the palindrome of 237 is 732). For a given natural number n, determine its palindrome.
def palindrom (n):
    """
    The function calculates the palindrom of a given number n
    :param n: natural number n
    :return: the palindrom of the number n
    """
    x=0
    while n!=0:
        x=x*10
        x=x+n%10
        n=int((n-n%10)/10)
    return x

if __name__ == '__main__':
    n= input ("Citeste n=")
    print(palindrom(int(n)))

