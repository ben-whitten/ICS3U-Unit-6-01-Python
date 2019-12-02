#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: December 2019
# This is a program which generates 10 random numbers and finds the average.

import random


# This allows me to do things with the text.
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def main():
    # This is what runs the program.

    random_number = []
    total = 0
    current_number = 0

    for loop_counter in range(0, 9+1):
        number = random.randint(0, 100+1)
        random_number.append(number)
        total = random_number[loop_counter] + total
        print(color.YELLOW + "{0}".format(random_number[loop_counter]),
              end=" | " + color.END)

    average = total/10
    print("")
    print(color.GREEN + "Average = {0}".format(average) + color.END)


if __name__ == "__main__":
    main()
