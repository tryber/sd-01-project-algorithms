def is_palindrome_recursive(word: str, index: int = 0) -> bool:
    if len(word) == 0:
        return False
    if index == len(word) // 2:
        return True
    if word[index] == word[(index + 1) * -1]:
        return is_palindrome_recursive(word, index + 1)
    return False


# def is_palindrome_recursive(word):
#     return (
#         is_palindrome_recursive(word[1:-1]) and False
#         if (word == "")
#         else (True if len(word) < 2 or (word[0] == word[-1]) else False)
#     )


# print(is_palindrome_recursive("SOCOS"))
