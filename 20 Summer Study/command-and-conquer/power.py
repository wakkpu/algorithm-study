def power1(a, n):

    if n == 0:
        return 1

    else:
        return a * power1(a, n-1)

def power2(a, n):

    if n == 0:
        return 1

    elif n % 2 == 0:
        return power2(a, n//2) ** 2

    else:
        return a * power2(a, n-1)

if __name__ == "__main__":

    a = 3
    n = 4

    print(power1(a, n))
    print(power2(a, n))
