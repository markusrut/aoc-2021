import os
from typing import List

class InputNode:
    def __init__(self, input: str):
        values = input.split(',')
        self.x = int(values[0])
        self.y = int(values[-1])
    
    def __str__(self) -> str:
        return f'{self.x},{self.y}'


class InputRow:
    def __init__(self, input_row: str):
        values = input_row.split()
        
        self.start = InputNode(values[0])
        self.end = InputNode(values[-1])

    def __str__(self):
        return f'{self.start} -> {self.end}'

def create_grid(input: List[InputRow]):
    largestX = max([max(i.start.x, i.end.x) for i in input])
    largestY = max([max(i.start.y, i.end.y) for i in input])
    grid = [[0 for x in range(largestX +1)] for y in range(largestY +1)]
    return grid


def print_grid(grid):
    for row in grid:
        print(row)


def draw_lines(inputs: List[InputRow], grid, include_diagonals=False):
    for i in inputs:
    
        if i.start.x != i.end.x and i.start.y != i.end.y and not include_diagonals:
            continue

        x = i.start.x
        y = i.start.y

        while True:            
            grid[y][x] += 1

            if x == i.end.x and y == i.end.y:
                break
            if not x == i.end.x:
                x += 1 if i.end.x > x else -1
            if not y == i.end.y:
                y += 1 if i.end.y > y else -1

    return grid


def count_overlapping(grid):
    overlapping = 0
    for row in grid:
        for col in row:
            if col > 1:
                overlapping += 1
    return overlapping

os.chdir('05')
with open("input.txt", "r") as f:
    input = [line.rstrip() for line in f.readlines()]
    parsed_input = list(map(InputRow, input))

def part1():
    grid = create_grid(parsed_input)
    grid = draw_lines(parsed_input, grid, False)
    # print_grid(grid)
    overlapping = count_overlapping(grid)
    print(overlapping)
    
def part2():
    grid = create_grid(parsed_input)
    grid = draw_lines(parsed_input, grid, True)
    # print_grid(grid)
    overlapping = count_overlapping(grid)
    print(overlapping)

part1()
part2()