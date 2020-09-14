from challenges.challenge_find_the_duplicate import find_duplicate


class Test_Duplicate:
    nums = {
        "1º mock": [1, 3, 4, 2, 2],
        "2º mock": [3, 1, 3, 4, 2],
        "3º mock": [1, 1],
        "4º mock": [1, 1, 2],
        "5º mock": [3, 1, 2, 4, 6, 5, 7, 7, 7, 8],
        "6º mock": [],
    }

    def test_when_an_input_has_a_duplicate_element_with_output_2(self):
        given = find_duplicate(self.nums["1º mock"])
        expected = 2
        assert given == expected

    def test_when_an_input_has_a_duplicate_element_with_output_3(self):
        given = find_duplicate(self.nums["2º mock"])
        expected = 3
        assert given == expected

    def test_when_an_input_has_a_duplicate_element_with_output_1(self):
        given = find_duplicate(self.nums["3º mock"])
        expected = 1
        assert given == expected

    def test_when_an_input_has_a_duplicate_element_with_output_1_(self):
        given = find_duplicate(self.nums["4º mock"])
        expected = 1
        assert given == expected

    def test_when_an_input_has_a_duplicate_element_with_output_7(self):
        given = find_duplicate(self.nums["5º mock"])
        expected = 7
        assert given == expected

    def test_when_an_input_has_a_duplicate_element_with_output_8(self):
        given = find_duplicate(self.nums["6º mock"])
        expected = -1
        assert given == expected
