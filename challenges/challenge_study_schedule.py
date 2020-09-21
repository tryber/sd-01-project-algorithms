def study_schedule(start_time, end_time, target_time):
    best_time = 0
    if target_time == 0:
        return f"O valor do target_time não pode ser {target_time}"

    for index in range(len(start_time)):
        if start_time[index] <= target_time <= end_time[index]:
            best_time += 1

    return f"A quantidade de estudantes que se adaptam a este horário é: {best_time}"


start_time = [2, 1, 2, 1, 4, 4]
end_time = [2, 2, 3, 5, 5, 5]
target_time = 2
print(study_schedule(start_time, end_time, target_time))
