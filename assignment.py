import random
o = random.SystemRandom()


def function(n,a):
    d = n-1
    while d%2 == 0:
        d = d// 2
       

    if (a**d)%n == 1:
        return True

    while d < n -1: 
        if (a**d)%n == -1:
            return True

        d <<= 1
    return False

def prime_test(n,k=40):
    if n == 1:
        return False
    elif n == 2:
        print('the given number is prime')
    else:
    
        for i in range(k):
            a = o.randrange(2,n-1)
            if not function(n,a):
                return False
        print("the given number may be prime")
print(prime_test(45))
