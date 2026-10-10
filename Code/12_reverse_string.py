def reverse_string(text):
    reversed_text = ""
    for ch in text:
        reversed_text = ch + reversed_text
    return reversed_text


if __name__ == "__main__":
    print(reverse_string("python"))
