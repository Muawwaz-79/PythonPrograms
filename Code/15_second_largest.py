def second_largest(numbers):
    if len(numbers) < 2:
        return numbers[0] if numbers else None

    highest = max(numbers[0], numbers[1])
    second = min(numbers[0], numbers[1])

    for num in numbers[2:]:
        if num > highest:
            second = highest
            highest = num
        elif num > second:
            second = num

    return second


if __name__ == "__main__":
    print(second_largest([12, 35, 1, 10, 34, 1]))
