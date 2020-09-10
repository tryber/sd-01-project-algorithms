from challenges.challenge_palindromes_recursive import is_palindrome_recursive


class Test_Recursive:
    word_T = "SOCOS"
    word_F = "SOCOSS"

    def test_when_word_is_palindrome_returns_True(self):
        given = is_palindrome_recursive(self.word_T)
        expected = True
        assert given is expected

    def test_when_word_is_palindrome_returns_False(self):
        given = is_palindrome_recursive(self.word_F)
        expected = False
        assert given is expected

    def test_when__word_is_empty_returns_False(self):
        given = is_palindrome_recursive("")
        expected = False
        assert given is expected
