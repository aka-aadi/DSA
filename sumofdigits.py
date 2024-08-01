
def sum_of_digits_up_to(n):
    if n < 0:
        return 0

    sum = 0
    fact = 1
    while fact <= n:
        l = n - (n // fact) * fact
        curr = (n // fact) % 10
        h = n // (fact * 10)
      
        sum += h * fact * 45
        sum += (curr * (curr - 1) // 2) * fact
        sum += (l + 1) * curr
        fact *= 10

    return sum

def sum_of_digits_between(a, b):
    return sum_of_digits_up_to(b) - sum_of_digits_up_to(a - 1)

a, b = map(int, input().strip().split())
result = sum_of_digits_between(a, b)
print(result)