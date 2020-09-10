def is_anagram(first_string, second_string):
    # Faça o código aqui.
    for i in range(len(first_string)):
        ok = False
        for j in second_string:
            if(first_string[i] == j):
                ok = True
                pass
        if not ok:
            return ok
    return True


def is_anagram2(first_string, second_string):
    # Faça o código aqui.
    for i in range(len(first_string)):
        



# first_string = "pedra"
# second_string = "perda"


first_string = "pato"
second_string = "tapo"


# first_string = "coxinha"
# second_string = "empada"


print(is_anagram(first_string, second_string))


