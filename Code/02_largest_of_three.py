def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

if __name__ == "__main__":
    # Test cases manually checking outputs
    print(find_largest(10, 20, 3))
    print(find_largest(5, 5, 2))