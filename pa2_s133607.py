"""
Name:Sulaiman Khalifa Khalfan Al Yousfi
ID:s133607
HW:2
Purpose:
Input:
Output:
Algorithm:
Test:
"""
from math import pi, sqrt, e


def main():
    x = 0
    mean = 0
    stdv = 0
    total = 0
    count = 0
    px = 0
    not_done = True



def calculateProbabilityDensityValue(x):
    px = 1 / sqrt(2 * pi) - e ** -x ** 2 / 2
    return px


def process(x, mean, stdv):
    while not_done:
        x, mean, stdv = input("Please Enter x, mean and stdv: ").split()
        if x.isdigit() and mean.isdigit() and stdv.isdigit():
            not_done = False
        elif x == "q" and mean == "q" and stdv == "q":
            print("The average prob density of the values having normal distribution:",
                  averageProbabilityDensityValue(total, count))
            print("There were", count, "values having normal distribution")

    if mean == 0 and stdv == 1:
        px = calculateProbabilityDensityValue(x)
    else:
        px = "***Not Normal Dist.***"

def averageProbabilityDensityValue(total, count):
    if total == 0 or count == 0:
        return 0
    else:
        return total / count


def printData():
    pass


main()
