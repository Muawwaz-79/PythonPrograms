def find_duplicates(numbers):
    seen = set()
    duplicates = set()

    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return sorted(duplicates)


if __name__ == "__main__":
    print(find_duplicates([1, 2, 3, 2, 4, 1, 5]))
