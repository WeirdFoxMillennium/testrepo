def sieve_of_eratosthenes(n):
    primes = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1

    prime_numbers = [p for p in range(2, n) if primes[p]]
    return prime_numbers

# Запрос ввода числа n с клавиатуры
n = int(input("Введите число n для поиска простых чисел: "))
print(f"Простые числа до {n}:")
print(sieve_of_eratosthenes(n))