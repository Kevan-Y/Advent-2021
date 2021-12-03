import os
import sys

# Loop through the columns
# if countOf1 > countOf0 add 1 to gamma else 0
# if countOf1 > countOf0 add 0 to epsilon else 1
# return the product of gamma and epsilon
def challenge1(data: list[list[int]]) -> int:
    gamma = ""
    epsilon = ""
    for i in range(len(data[0])):
        countOf1 = [j[i] for j in data].count(1)
        countOf0 = [j[i] for j in data].count(0)
        gamma += str(1 if countOf1 > countOf0 else 0)
        epsilon += str(0 if countOf1 > countOf0 else 1)

    return int(gamma, 2) * int(epsilon, 2)


# Loop through the columns
# if dataTemp only have 1 element return the bytes as a string
# if countOf1 >= countOf0 get all element at columns index start with 1 and set the new list to dataTemp
# else get all element at columns index start with 0 and set the new list to dataTemp
def getOxygenGeneratorRating(data: list[list[int]]) -> str:
    dataTemp = data
    for i in range(len(data[0])):
        countOf1 = [j[i] for j in dataTemp].count(1)
        countOf0 = [j[i] for j in dataTemp].count(0)
        if len(dataTemp) > 1:
            if countOf1 >= countOf0:
                dataTemp = [idx for idx in dataTemp if idx[i] == 1]
            else:
                dataTemp = [idx for idx in dataTemp if idx[i] == 0]
        else:
            break
    return "".join([str(item) for sublist in dataTemp for item in sublist])


# Loop through the columns
# if dataTemp only have 1 element return the bytes as a string
# if countOf0 <= countOf1 get all element at columns index start with 0 and set the new list to dataTemp
# else get all element at columns index start with 1 and set the new list to dataTemp
def getOxygenScrubberRating(data: list[list[int]]) -> str:
    dataTemp = data
    for i in range(len(data[0])):
        countOf1 = [j[i] for j in dataTemp].count(1)
        countOf0 = [j[i] for j in dataTemp].count(0)
        if len(dataTemp) > 1:
            if countOf0 <= countOf1:
                dataTemp = [idx for idx in dataTemp if idx[i] == 0]
            else:
                dataTemp = [idx for idx in dataTemp if idx[i] == 1]
        else:
            break
    return "".join([str(item) for sublist in dataTemp for item in sublist])


# return the product of oxygenGeneratorRating and oxygenScrubberRating
def challenge2(data: list[list[int]]) -> int:
    return int(getOxygenGeneratorRating(data), 2) * int(
        getOxygenScrubberRating(data), 2
    )


def main() -> None:
    f = open(os.path.join(sys.path[0], "data/day_3_input.txt"), "r")
    lines = f.readlines()
    data_list: list[list[int]] = []
    for line in lines:
        line = line.strip("\n")
        data_list.append([int(x) for x in list(line)])

    print(challenge1(data_list))
    print(challenge2(data_list))


if __name__ == "__main__":
    main()
