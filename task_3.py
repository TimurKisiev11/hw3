# Задача 3, НОК и НОД чисел, введенных из консоли


def gcd(a, b):
    """НОД"""
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """НОК"""
    return abs(a * b) // gcd(a, b)


numbers = list(map(int, input("Введите числа через пробел: ").split()))
result_gcd = numbers[0]
result_lcm = numbers[0]

for number in numbers[1:]:
    result_gcd = gcd(result_gcd, number)
    result_lcm = lcm(result_lcm, number)

print("НОД чисел:", result_gcd)
print("НОК чисел:", result_lcm)
