def study_schedule(start_time, end_time, target_time):
    if target_time == 0:
        return f"O valor do target_time não pode ser {target_time}"

    students_quantity = 0
    for index in range(len(start_time)):
        if start_time[index] <= target_time and target_time <= end_time[index]:
            students_quantity += 1

    return f"A quantidade de estudantes que se adaptam a este horário é: {students_quantity}"


start_time = [2, 1, 2, 1, 4, 4]
end_time = [2, 2, 3, 5, 5, 5]
target_time = 5
print(study_schedule(start_time, end_time, target_time))
