def is_anagram(first_string, second_string):
    if first_string == "" or second_string == "":
        return False
    return sorted(first_string) == sorted(second_string)


first_string = "teste"
second_string = "tetes"
print(is_anagram(first_string, second_string))
