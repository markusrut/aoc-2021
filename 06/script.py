import os
from typing import List


def parse_input(input: str):
    fish_input = list(map(int, input.split(',')))
    fish_count = [0] * 9
    for fish in fish_input:
        fish_count[fish] += 1
    return fish_count


def iterate_days(fish_count: List[int], days: int):
    reset_fish_index = 6
    new_fish_index = 8

    for _ in range(days):
        spawn_count = 0
        for i in range(len(fish_count)):
            if i == 0:
                spawn_count = fish_count[i]
            elif i > 0:
                fish_count[i-1] = fish_count[i]

        fish_count[new_fish_index] = spawn_count
        fish_count[reset_fish_index] += spawn_count
        # print(f"Day: {d+1}, Fish count: {fish_count}, Sum: {sum(fish_count)}")


def part1(input: str):
    fish_count = parse_input(input)
    iterate_days(fish_count, 80)
    print(sum(fish_count))
    
def part2(input: str):
    fish_count = parse_input(input)
    iterate_days(fish_count, 256)
    print(sum(fish_count))

os.chdir('06')
with open("input.txt", "r") as f:
    input = f.readline().rstrip()
    # input = [line.rstrip() for line in f.readlines()]

part1(input)
part2(input)