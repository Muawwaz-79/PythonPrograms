def word_frequency(sentence):
    if sentence == "":
        return {}

    frequency = {}
    for word in sentence.split():
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency


if __name__ == "__main__":
    print(word_frequency("hello world hello"))
