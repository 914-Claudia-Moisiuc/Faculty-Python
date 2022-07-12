
#15. Generate the largest perfect number smaller than a given natural number n. If such a number does not exist, a message should be displayed. A number is perfect if it is equal to the sum of its divisors, except itself. (e.g. 6 is a perfect number, as 6=1+2+3).

def perfect_number(n):
    """
    the function calculates the sum of the given n number's divisors
    :param n:natural number n
    :return:the sum of n's divisors
    """
    sum=0
    for i in range(1,int(n/2)+1):
        if n%i==0:
            sum=sum+i
    return sum

def perf_smaller_than_n(n):
    """
    the function generates the largest perfect number smaller than a given natural number n
    :param n: natural number n
    :return: the largest perfect number smaller than n
    """
    for i in range(n-1,-1,-1):
        if i == perfect_number(i):
            return i
    return -1

if __name__ == '__main__':
    n= input ("Citeste n=")
    x= perf_smaller_than_n(int(n))
    if x==-1:
        print("a perfect number smaller than n does not exist")
    else:
        print (x)

#hello
