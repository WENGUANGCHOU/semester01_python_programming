# This Program will print first N Prime Numbers
# Input N Should be given.

def isprime(n):
    if n == 2:
        return True
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True


def n_primes(N):
    count = 0
    lis = []
    i = 0
    while True:
        i = i + 1
        if isprime(i):
            lis.append(i)
            count += 1

        if len(lis) == N:
            return "First", N, "Prime Numbers are: ", lis


def main():
    print("For Example: Test cases")
    print(n_primes(10))
    print(n_primes(5))
    print(n_primes(115))
    x = int(input("enter a number: "))
    print(n_primes(x))


if __name__ == "__main__":
    main()

