import os
import sys

# Loop if previous value < current value then increase counter by 1
def challenge1(data: list[int]) -> int:
    counter = 0
    for i, item in enumerate(data):
        if i - 1 >= 0:
            if data[i - 1] < item:
                counter += 1
    return counter


# Check if data has more then 4 items
# if more than 4 items set old to be the sum of the current + next 2 value
# else return counter
# Loop if current + next 2 value > old sum then increase counter by 1
def challenge2(data: list[int]) -> int:
    counter = 0
    oldSum = 0

    if len(data) > 4:
        oldSum = data[0] + data[1] + data[2]
    else:
        return counter

    for i, item in enumerate(data, start=1):
        if i + 2 < len(data):
            if data[i] + data[i + 1] + data[i + 2] > oldSum:
                counter += 1
            oldSum = data[i] + data[i + 1] + data[i + 2]
    return counter


def main() -> None:
    f = open(os.path.join(sys.path[0], "data/day_1_input.txt"), "r")
    data = f.read()
    data_list = data.split("\n")
    data_list = [int(i) for i in data_list]
    print(challenge1(data_list))
    print(challenge2(data_list))


if __name__ == "__main__":
    main()
