def char_frequency(text):
    frequency = {}
    for ch in text:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1
    return frequency


if __name__ == "__main__":
    print(char_frequency("banana"))
