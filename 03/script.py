import os

os.chdir('03')
with open("input.txt", "r") as f:
    input = [line.rstrip() for line in f.readlines()]


def splitToNumbers(word: str):
    return [int(i) for i in word]


def binaryToDecimal(binary: str):
    return int(binary, 2)


def countBitsInList(list: list):
    bitCounter = [0] * len(list[0])

    for line in list:
        bitsList = splitToNumbers(line)
        for i in range(len(bitsList)):
            if bitsList[i] == 1:
                bitCounter[i] += 1

    return bitCounter


def filterListByAverage(input: list[str], keepAboveAverage: bool):
    binaryLength = len(input[0])
    filteredList = input
    while len(filteredList) > 1:
        for i in range(binaryLength):
            bitCountForIndex = countBitsInList(filteredList)[i]
            average = len(filteredList) / 2
            if bitCountForIndex >= average:
                filteredList = [
                    line for line in filteredList
                    if int(line[i]) == (1 if keepAboveAverage else 0)
                ]
            if bitCountForIndex < average:
                filteredList = [
                    line for line in filteredList
                    if int(line[i]) == (0 if keepAboveAverage else 1)
                ]
            if len(filteredList) == 1:
                break

    return filteredList[0]


def calculatePart1(input: list[str]):
    bitCounter = countBitsInList(input)

    gammaRateBinary = [0] * len(bitCounter)
    epsilonRateBinary = [0] * len(bitCounter)

    average = len(input) / 2
    for i in range(len(bitCounter)):
        bit = bitCounter[i]
        if bit > average:
            gammaRateBinary[i] = 1
        else:
            epsilonRateBinary[i] = 1

    gammaRate = binaryToDecimal(''.join(map(str, gammaRateBinary)))
    epsilonRate = binaryToDecimal(''.join(map(str, epsilonRateBinary)))

    return gammaRate * epsilonRate


def calculatePart2(input: list[str]):
    oxygenRatingBinary = filterListByAverage(input, True)
    oxygenRating = binaryToDecimal(oxygenRatingBinary)
    co2RatingBinary = filterListByAverage(input, False)
    co2Rating = binaryToDecimal(co2RatingBinary)
    return oxygenRating * co2Rating


print("Part 1: ", calculatePart1(input))
print("Part 2: ", calculatePart2(input))
