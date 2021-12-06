import os
from typing import List


def iterate_days(fishes: List[int], days: int):
    reset_fish = 6
    new_fish = 8

    for d in range(days):
        spawn_count = 0
        for i in range(len(fishes)):
            if fishes[i] > 0:
                fishes[i] -= 1
            else:
                spawn_count += 1
                fishes[i] = reset_fish

        new_fishes = [new_fish] * spawn_count
        fishes = fishes + new_fishes
    return fishes


os.chdir('06')
with open("input.txt", "r") as f:
    input = [line.rstrip() for line in f.readlines()]
    fish_input = list(map(int, input[0].split(',')))

def part1():
    fishes = iterate_days(fish_input, 80)
    print(len(fishes))
    
def part2():
    fishes = iterate_days(fish_input, 256)
    print(len(fishes))

part1()
# part2()