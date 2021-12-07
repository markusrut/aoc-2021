import os
from statistics import median, mean


def steps_to_average(positions):
    average = round(mean(positions))
    steps_list = []
    steps_list.append(steps_to_pos(positions, average))
    steps_list.append(steps_to_pos(positions, average+1))
    steps_list.append(steps_to_pos(positions, average-1))
    return min(steps_list)


def steps_to_pos(positions, average):
    steps = 0
    for pos in positions:
        diff = abs(pos - average)
        inner_steps = 0
        for i in range(diff):
            inner_steps += i+1
        steps += inner_steps
    return steps


def steps_to_median(positions):
    med = median(positions)
    steps = 0
    for pos in positions:
        steps += abs(pos - med)
    return steps

os.chdir('07')
with open("input.txt", "r") as f:
    input = f.readline().rstrip()

positions = list(map(int, input.split(',')))

print(f"Part 1 : {steps_to_median(positions)}")
print(f"Part 2 : {steps_to_average(positions)}")
