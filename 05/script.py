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
        if i.start.x == i.end.x:
            for y in range(min(i.start.y, i.end.y), max(i.start.y, i.end.y) + 1):
                grid[y][i.start.x] += 1
        elif i.start.y == i.end.y:
            for x in range(min(i.start.x, i.end.x), max(i.start.x, i.end.x) + 1):
                grid[i.start.y][x] += 1
        elif include_diagonals:
            print(f'Diagonal: {i}')
            top_to_bottom = i.start.x < i.end.x
            if not top_to_bottom:
                old_start = i.start
                i.start = i.end
                i.end = old_start
                
            left_to_right = i.start.y < i.end.y
            x = i.start.x
            y = i.start.y
            
            while x <= i.end.x and (left_to_right and y <= i.end.y or not left_to_right and y >= i.end.y):
                print(f"draw node {x},{y}")
                grid[x][y] += 1
                x += 1
                y += 1 if left_to_right else -1
    return grid


def count_overlapping(grid):
    overlapping = 0
    for row in grid:
        for col in row:
            if col > 1:
                overlapping += 1
    return overlapping

os.chdir('05')
with open("sample.txt", "r") as f:
    input = [line.rstrip() for line in f.readlines()]
    parsed_input = list(map(InputRow, input))

def part1():
    grid = create_grid(parsed_input)
    grid = draw_lines(parsed_input, grid, False)
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