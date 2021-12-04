import os
from typing import Tuple

os.chdir('04')
with open("input.txt", "r") as f:
    input = [line.rstrip() for line in f.readlines()]


class BingoNode:
    def __init__(self, value: int):
        self.value = value
        self.found = False

    def __str__(self):
        return str(self.value) + " " + str(self.found)


class BingoRow:
    def __init__(self, nodes: list[BingoNode]):
        self.nodes = nodes

    def markNumber(self, number: int):
        for node in self.nodes:
            if node.value == number:
                node.found = True

    def sumOfNotFoundNumbers(self):
        return sum(node.value for node in self.nodes if not node.found)

    def __str__(self):
        return " ".join(map(str, self.nodes))


class BingoBoard:
    def __init__(self, rows: list[BingoRow]):
        self.rows = rows
        self.won = False

    def markNumber(self, number: int):
        for row in self.rows:
            row.markNumber(number)

    def checkForWin(self):
        if self.checkRowsForWin() or self.checkColumnsForWin():
            self.won = True
            return True
        return False

    def checkRowsForWin(self):
        for row in self.rows:
            if all(node.found for node in row.nodes):
                return True
        return False

    def checkColumnsForWin(self):
        for i in range(len(self.rows[0].nodes)):
            column = [row.nodes[i] for row in self.rows]
            if all(node.found for node in column):
                return True
        return False

    def sumOfNotFoundNumbers(self):
        return sum(row.sumOfNotFoundNumbers() for row in self.rows)

    def __str__(self):
        return "\n".join(map(str, self.rows))


def createBingoBoards(input: list[str]):
    boards: list[BingoBoard] = []
    boardRows: list[BingoRow] = []

    for line in input:
        if line == "":
            if boardRows == []:
                continue
            else:
                boards.append(BingoBoard(boardRows))
                boardRows = []
                continue

        nodes = list(map(BingoNode, map(int, line.split())))
        boardRow = BingoRow(nodes)
        boardRows.append(boardRow)

    boards.append(BingoBoard(boardRows))
    return boards


def playBingo(boards: list[BingoBoard], bingoNumbers: list[int]):
    firstWinner: Tuple[BingoBoard, int] = None
    mostRecentWinner: Tuple[BingoBoard, int] = None

    for number in bingoNumbers:
        for board in boards:
            if board.won:
                continue

            board.markNumber(number)
            if board.checkForWin():
                mostRecentWinner = (board, number)

                if firstWinner is None:
                    firstWinner = mostRecentWinner

    return firstWinner, mostRecentWinner


bingoNumbers = list(map(int, input.pop(0).split(',')))
boards = createBingoBoards(input)

firstWinner, lastWinner = playBingo(boards, bingoNumbers)
print("Result 1", firstWinner[0].sumOfNotFoundNumbers() * firstWinner[1])
print("Result 2", lastWinner[0].sumOfNotFoundNumbers() * lastWinner[1])
