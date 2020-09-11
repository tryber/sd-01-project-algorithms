def is_palindrome_recursive(word: str, index: int = 0) -> bool:
    if len(word) == 0:
        return False
    if index == len(word) // 2:
        return True
    if word[index] == word[(index + 1) * -1]:
        return is_palindrome_recursive(word, index + 1)
    return False
