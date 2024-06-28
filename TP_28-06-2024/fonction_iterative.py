def fibonacci_iteratif(n):
    if n <= 0:
        return "Entrée invalide, n doit être un entier positif."

    if n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1

    for _ in range(2, n):
        a, b = b, a + b

    return b

print(fibonacci_iteratif(10))  
