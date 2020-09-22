def is_palindrome_recursive(word, low, high):
    if word == '':
        return False

    if low >= (len(word) // 2):
        return True

    if word[low] == word[high]:
        return is_palindrome_recursive(word, low + 1, high - 1)
    return False


word = ''
print(is_palindrome_recursive(word, 0, len(word) - 1))
