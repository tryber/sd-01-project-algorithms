from typing import List


def study_schedule(start_time: List, end_time: List, target_time: int) -> int:
    answer: int = 0
    for pos in range(len(start_time)):
        if start_time[pos] <= target_time <= end_time[pos]:
            answer += 1
    return answer
