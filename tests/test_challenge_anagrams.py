from challenges.challenge_anagrams import is_anagram


class Test_Anagrams:
    def test_when_the_anagram_receives_amor_and_roma_it_must_be_True(self):
        first_string = "amor"
        second_string = "roma"
        given = is_anagram(first_string, second_string)
        expected = True
        assert given is expected

    def test_when_the_anagram_receives_pedra_and_perda_it_must_be_True(self):
        first_string = "pedra"
        second_string = "perda"
        given = is_anagram(first_string, second_string)
        expected = True
        assert given is expected

    def test_when_the_anagram_receives_pato_and_tapo_it_must_be_True(self):
        first_string = "pato"
        second_string = "tapo"
        given = is_anagram(first_string, second_string)
        expected = True
        assert given is expected

    def test_when_the_anagram_receives_coxinha_and_romaempada_it_must_be_False(self):
        first_string = "coxinha"
        second_string = "empada"
        given = is_anagram(first_string, second_string)
        expected = False
        assert given is expected