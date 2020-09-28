def is_anagram(first_string, second_string):
    return sorted(first_string) == sorted(second_string)


first_string = "tggsa"
second_string = "asat"
print(is_anagram(first_string, second_string))
