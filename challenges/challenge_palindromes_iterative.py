def is_palindrome_iterative(word: str) -> bool:
    if word == "":
        return False
    return word == word[::-1]
