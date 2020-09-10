from challenges.challenge_study_schedule import study_schedule


class Fisrt_Use_Case:

    start_time_1 = [2, 1, 2, 1, 4, 4]
    end_time_1 = [2, 2, 3, 5, 5, 5]

    def when_target_time_is_5_the_output_must_be_3(self):
        expectation = study_schedule(self.start_time_1, self.end_time_1, 5)
        reality = 3
        assert expectation == reality

    def when_target_time_is_4_the_output_must_be_3(self):
        expectation = study_schedule(self.start_time_1, self.end_time_1, 4)
        reality = 3
        assert expectation == reality

    def when_target_time_is_3_the_output_must_be_2(self):
        expectation = study_schedule(self.start_time_1, self.end_time_1, 3)
        reality = 2
        assert expectation == reality

    def when_target_time_is_2_the_output_must_be_4(self):
        expectation = study_schedule(self.start_time_1, self.end_time_1, 2)
        reality = 4
        assert expectation == reality

    def when_target_time_is_1_the_output_must_be_2(self):
        expectation = study_schedule(self.start_time_1, self.end_time_1, 1)
        reality = 2
        assert expectation == reality


class Second_Use_Case:

    start_time_2 = [4, 1, 3, 2]
    end_time_2 = [4, 3, 4, 5]

    def secund_case_when_target_time_is_5_the_output_must_be_2(self):
        expectation = study_schedule(self.start_time_2, self.end_time_2, 5)
        reality = 0
        assert expectation == reality

    def secund_case_when_target_time_is_4_the_output_must_be_2(self):
        expectation = study_schedule(self.start_time_2, self.end_time_2, 4)
        reality = 3
        assert expectation == reality

    def secund_case_when_target_time_is_3_the_output_must_be_2(self):
        expectation = study_schedule(self.start_time_2, self.end_time_2, 3)
        reality = 3
        assert expectation == reality

    def secund_case_when_target_time_is_2_the_output_must_be_2(self):
        expectation = study_schedule(self.start_time_2, self.end_time_2, 2)
        reality = 2
        assert expectation == reality

    def secund_case_when_target_time_is_1_the_output_must_be_2(self):
        expectation = study_schedule(self.start_time_2, self.end_time_2, 1)
        reality = 1
        assert expectation == reality
