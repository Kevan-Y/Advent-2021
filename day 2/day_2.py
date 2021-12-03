import os
import sys

# If forward X, horizontal is increased by X
# If down X, depth is increased by X
# If up X, depth is decreased by X
# return the product of horizontal and depth
def challenge1(data: list[list[str]]) -> int:
    horizontal:int = 0
    depth :int = 0
    for item in data:
        match item[0]:
            case "forward":
                horizontal += int(item[1])
            case "down":
                depth += int(item[1])
            case "up": 
                depth -= int(item[1])
    return horizontal*depth

# If forward X, horizontal is increased by X and depth increased by product aim and X
# If down X, aim is increased by X
# If up X, aim is decreased by X
# return the product of horizontal and depth
def challenge2(data: list[list[str]]) -> int:
    horizontal:int = 0
    depth :int = 0
    aim:int = 0
    for item in data:
        match item[0]:
            case "forward":
                horizontal += int(item[1])
                depth +=  int(item[1])*aim
            case "down":
                aim += int(item[1])
            case "up": 
                aim -= int(item[1])

    return horizontal*depth


def main() -> None:
    f = open(os.path.join(sys.path[0], "data/day_2_input.txt"), "r")
    lines = f.readlines()
    data_list: list[list[str]] = []
    for line in lines:
        line = line.strip("\n")
        data_list.append(line.split(" "))

    print(challenge1(data_list))
    print(challenge2(data_list))


if __name__ == "__main__":
    main()
