def is_palindrome_recursive(word, low, high):
    if word == "":
        return False

    if low >= (len(word) // 2):
        return f"{word} é um palídromo"

    if word[low] == word[high]:
        return is_palindrome_recursive(word, low + 1, high - 1)
    return f"{word} não é um palídromo"


word = "anssnfa"
print(is_palindrome_recursive(word, 0, len(word) - 1))
