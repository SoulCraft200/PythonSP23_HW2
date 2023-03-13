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
    total = 0
    count = 0
    x, mean, stdv = input("Please Enter x, mean and stdv: ").split()
    while not x == "q" and not mean == "q" and not stdv == "q":
        # if temp[0].isdigit() and temp[1].isdigit() and temp[2].isdigit():
        x = float(x)
        mean = float(mean)
        stdv = float(stdv)
        total,count = process(x, mean, stdv, total, count)
        x, mean, stdv = input("Please Enter x, mean and stdv: ").split()
    # else:
    #     print("Invalid input....")
    #     temp = input("Please Enter x, mean and stdv: ").split()
    print("The average prob density of values having normal distribution:",
          averageProbabilityDensityValue(total, count))
    print("Ther were", count, "values having normal distribution.")


def calculateProbabilityDensityValue(x):
    px = 1 / sqrt(2 * pi) - e ** ((-x ** 2) / 2)
    return px


def process(x, mean, stdv, total, count):
    if x < 0:
        x = abs(x)
    px = 0
    if mean == 0 and stdv == 1:
        px = calculateProbabilityDensityValue(x)
        total += px
        count += 1
    else:
        px = "***Not Normal Dist.***"

    printData(x, mean, stdv, px)
    return total, count


def averageProbabilityDensityValue(total, count):
    if total == 0 or count == 0:
        return 0
    else:
        return round(total / count, 4)


def printData(x, mean, stdv, px):
    print("%6s%9s%10s%20s" % ("x", "Mean", "standDev", "P(X) / MSG"))
    print("%6s%9s%10s%20s" % ("---", "---------", "---------", "---------"))
    px = str(px)
    if px == "***Not Normal Dist.***":
        print("%6.2f%9.2f%10.2f%20s" % (x, mean, stdv, px))
    else:
        px = float(px)
        px = round(px, 4)
        print("%6.2f%9.2f%10.2f%20s" % (x, mean, stdv, px))


main()
