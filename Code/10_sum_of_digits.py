def sum_of_digits(n):
    if n < 0:
        n = -n

    total = 0
    while n > 0:
        total += n % 10
        n //= 10

    return total


if __name__ == "__main__":
    print(sum_of_digits(1234))
    print(sum_of_digits(-123))
