def is_palindrome_iterative(word):
    if word == "":
        return False
    word_reverse = word[::-1]
    return word_reverse == word
