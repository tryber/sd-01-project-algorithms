def study_schedule(start_time, target_time, end_time):
    if target_time == 0:
        return f"target_time não pode ser {target_time}"

    best_time = 0
    for index in range(len(start_time)):
        if start_time[index] <= target_time <= end_time[index]:
            best_time += 1

    return best_time


start_time = [3, 2, 4, 2, 5, 5]
end_time = [3, 3, 3, 5, 5, 5]
target_time = 2
print(study_schedule(start_time, target_time, end_time))
