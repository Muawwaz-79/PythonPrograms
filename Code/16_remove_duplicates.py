def remove_duplicates(numbers):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers


if __name__ == "__main__":
    print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
