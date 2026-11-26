def count_vowels(text):
    if text is None:
        return 0
    return sum(1 for c in text if c in "aeiouAEIOU")
