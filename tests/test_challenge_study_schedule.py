from challenges.challenge_study_schedule import study_schedule


class Test_Fisrt_Use_Case:

    start_time = [2, 1, 2, 1, 4, 4]
    end_time = [2, 2, 3, 5, 5, 5]

    def test_when_target_time_is_5_the_output_must_be_3(self):
        given = study_schedule(self.start_time, self.end_time, 5)
        expected = 3
        assert given == expected

    def test_when_target_time_is_4_the_output_must_be_3(self):
        given = study_schedule(self.start_time, self.end_time, 4)
        expected = 3
        assert given == expected

    def test_when_target_time_is_3_the_output_must_be_2(self):
        given = study_schedule(self.start_time, self.end_time, 3)
        expected = 2
        assert given == expected

    def test_when_target_time_is_2_the_output_must_be_4(self):
        given = study_schedule(self.start_time, self.end_time, 2)
        expected = 4
        assert given == expected

    def test_when_target_time_is_1_the_output_must_be_2(self):
        given = study_schedule(self.start_time, self.end_time, 1)
        expected = 2
        assert given == expected


class Test_Second_Use_Case:

    start_time = [4, 1, 3, 2]
    end_time = [4, 3, 4, 5]

    def test_when_target_time_is_5_the_output_must_be_1(self):
        given = study_schedule(self.start_time, self.end_time, 5)
        expected = 1
        assert given == expected

    def test_when_target_time_is_4_the_output_must_be_3(self):
        given = study_schedule(self.start_time, self.end_time, 4)
        expected = 3
        assert given == expected

    def test_when_target_time_is_3_the_output_must_be_3(self):
        given = study_schedule(self.start_time, self.end_time, 3)
        expected = 3
        assert given == expected

    def test_when_target_time_is_2_the_output_must_be_2(self):
        given = study_schedule(self.start_time, self.end_time, 2)
        expected = 2
        assert given == expected

    def test_when_target_time_is_1_the_output_must_be_1(self):
        given = study_schedule(self.start_time, self.end_time, 1)
        expected = 1
        assert given == expected
