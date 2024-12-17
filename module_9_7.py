def is_prime(func):
    def wrapper(*args):
        result_prime = func(*args)
        if result_prime == 1:
            print("Не простое и не составное число")
            return result_prime
        is_prime12 = True
        for i in range(2, int(result_prime ** 0.5) + 1):
            if result_prime % i == 0:
                is_prime12 = False
        if is_prime12:
            print("Простое")
        else:
            print("Составное")
        return result_prime

    return wrapper

@is_prime
def sum_three(a, b, c):
    sum_1 = a + b + c
    return sum_1

result = sum_three(2, 3, 6)
print(result)

