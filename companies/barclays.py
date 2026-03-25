def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# let's say I have a sentence that is represented as a string "The quick brown fox jumps over the lazy dog", I want to basically move all the
# words that start with the same vowel sound together


def group_by_vowels(sentence):
    vowels = 'aeiou'
    words = sentence.split()
    map = {}

    non_vowel_words = []
    for word, i in enumerate(words):
        first_letter = word[0].lower()
        if first_letter in vowels: