def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for ch in text:
        if ch.isalpha():
            if ch in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count


if __name__ == "__main__":
    print(count_vowels_consonants("hello world"))
