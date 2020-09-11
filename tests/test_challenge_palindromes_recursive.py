from challenges.challenge_palindromes_recursive import is_palindrome_recursive


class Test_Recursive:
    word_T = "SOCOS"
    word_F = "SOCOSS"
    word_A = "ANA"
    word_AS = "ANAS"

    def test_when_word_is_palindrome_returns_True_1(self):
        given = is_palindrome_recursive(self.word_T)
        expected = True
        assert given == expected

    def test_when_word_is_palindrome_returns_False_2(self):
        given = is_palindrome_recursive(self.word_F)
        expected = False
        assert given == expected

    def test_when__word_is_empty_returns_False_3(self):
        given = is_palindrome_recursive("")
        expected = False
        assert given == expected

    def test_when_word_is_palindrome_returns_False_4(self):
        given = is_palindrome_recursive(self.word_A)
        expected = True
        assert given == expected

    def test_when_word_is_palindrome_returns_False_5(self):
        given = is_palindrome_recursive(self.word_AS)
        expected = False
        assert given == expected
