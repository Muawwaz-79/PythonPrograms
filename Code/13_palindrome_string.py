def is_palindrome_string(text):
    normalized = text.lower()
    left = 0
    right = len(normalized) - 1

    while left < right:
        if normalized[left] != normalized[right]:
            return False
        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    print(is_palindrome_string("radar"))
    print(is_palindrome_string("python"))
