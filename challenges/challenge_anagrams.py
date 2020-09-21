def is_anagram(first_string, second_string):
    first_string_sorted = sorted(first_string)
    second_string_sorted = sorted(second_string)

    if first_string_sorted == second_string_sorted:
        return True
    return False


first_string = "amor"
second_string = "roma"
print(is_anagram(first_string, second_string))
