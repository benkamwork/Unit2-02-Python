#!/usr/bin/env python3

# Created By: Ben Kamanda

# Date: February 28, 2025

# Calculates the circumference

import math
import constants


def main():
    # ask for radius
    radius = float(input("What is the radius: "))

    print("The circumference is: {}".format(constants.TAU * radius))


if __name__ == "__main__":
    main()
