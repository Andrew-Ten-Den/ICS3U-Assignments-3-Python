#!/usr/bin/env python3

# Created by: Andrew Ten-Den
# Created on: April 2022
# This program lets the user pick a number that corresponds with a day


def main():
    # this function lets the user pick a number that corresponds with a day

    # input
    day_number = int(input("Enter a number of the day (ex: 3 is Tuesday): "))

    # process & output
    if day_number == 1:
        print("Sunday")

    elif day_number == 2:
        print("Monday")

    elif day_number == 3:
        print("Tuesday")

    elif day_number == 4:
        print("Wednesday")

    elif day_number == 5:
        print("Thursday")

    elif day_number == 6:
        print("Friday")

    elif day_number == 7:
        print("Saturday")
    else:
        print("No idea!")

    print("")
    print("Done")


if __name__ == "__main__":
    main()
