def is_anagram(first_string: str, second_string: str) -> bool:
    sorted_fist_string = sorted(first_string)
    sorted_second_string = sorted(second_string)
    answer = True
    lentgh = len(first_string)
    pos = 0
    while pos < lentgh and answer:
        if sorted_fist_string[pos] == sorted_second_string[pos]:
            pos += 1
        else:
            answer = False
    return answer
