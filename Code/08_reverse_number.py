def reverse_number(n):
    if n == 0:
        return 0

    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_num = 0

    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10

    return reversed_num * sign


if __name__ == "__main__":
    print(reverse_number(1234))
    print(reverse_number(-123))
