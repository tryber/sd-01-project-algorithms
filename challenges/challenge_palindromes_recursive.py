def is_palindrome_recursive(word, low, high):
    if word == "":
        return False

    if (low >= high):
        return True

    if word[low] != word[high]:
        return False
    return is_palindrome_recursive(word, low + 1, high - 1)


word = "omissíssimo"
print(is_palindrome_recursive(word, 0, len(word) - 1))
