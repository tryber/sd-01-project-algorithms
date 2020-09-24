def is_palindrome_recursive(word, first, last):
    if word == '':
        return False
    if first >= (len(word) // 2):
        return True
    if word[first] == word[last]:
        return is_palindrome_recursive(word, first + 1, last - 1)
    return False

word = ""
print(is_palindrome_recursive(word, 0, len(word) - 1))
