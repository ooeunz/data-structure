def is_primes(n: int):
    a = [False,False] + [True] * (n-1)
    primes = []

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    return primes

if __name__ == "__main__":
    print(is_primes(1000))