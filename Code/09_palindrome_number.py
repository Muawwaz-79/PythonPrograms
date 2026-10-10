def is_palindrome_num(n):
    if n < 0:
        return False

    original = n
    reversed_num = 0

    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10

    return reversed_num == original


if __name__ == "__main__":
    print(is_palindrome_num(121))
    print(is_palindrome_num(123))
