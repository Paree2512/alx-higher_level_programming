#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    args = len(sys.argv)

    if args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")