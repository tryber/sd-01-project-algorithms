def is_palindrome_recursive(word, low, high):
    if word == "":
        return False

    if low >= (len(word) // 2):
        return f"{word} é um palídromo"

    character_count = low + 1

    if word[low] == word[high]:
        return is_palindrome_recursive(word, character_count, len(word) - (1 + character_count))
    else:
        return f"{word} não é um palídromo"


word = ""
print(is_palindrome_recursive(word, 0, len(word) - 1))
