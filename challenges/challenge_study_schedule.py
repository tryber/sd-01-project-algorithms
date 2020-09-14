def study_schedule(start_time, end_time, target_time):
    indice = 0
    end = len(start_time)
    print(end)
    while(indice < end):
        study_start = start_time[indice]
        study_end = end_time[indice]
        if study_start == study_end:
            pass
        while(study_start <= study_end):
            target[study_start-1] += 1
            study_start += 1
        indice += 1
    print(target)
    return target[target_time-1]


def study_schedule2(start_time, end_time, target_time):
    value = 0
    for i in range(len(start_time)):
        if start_time[i] <= target_time <= end_time[i]:
            value += 1
    return value


# start_time = []
# end_time = []

target_time = 1

start_time = [4, 1, 3, 2]
end_time   = [4, 3, 4, 5]

# start_time = [1, 2, 3]
# end_time = [2, 5, 5]

print(study_schedule2(start_time, end_time, target_time))
