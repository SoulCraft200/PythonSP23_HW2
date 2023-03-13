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
    temp = input("Please Enter x, mean and stdv: ").split()
    while not temp[0] == "q" and not temp[1] == "q" and not temp[2] == "q":
        if temp[0].isdigit() and temp[1].isdigit() and temp[2].isdigit():
            temp[0] = float(temp[0])
            temp[1] = float(temp[1])
            temp[2] = float(temp[2])
            process(temp[0], temp[1], temp[2], total, count)
            temp = input("Please Enter x, mean and stdv: ").split()
        else:
            print("Invalid input....")
            temp = input("Please Enter x, mean and stdv: ").split()

    print("The average prob density of values having normal distribution:",
          averageProbabilityDensityValue(total, count))
    print("Ther were",count,"values having normal distribution.")


def calculateProbabilityDensityValue(x):
    px = 1 / sqrt(2 * pi) - e ** -x ** 2 / 2
    return px


def process(x, mean, stdv, total, count):
    px = 0
    if mean == 0 and stdv == 1:
        px = calculateProbabilityDensityValue(x)
        total += px
        count += 1
    else:
        px = "***Not Normal Dist.***"

    printData(x, mean, stdv, px)


def averageProbabilityDensityValue(total, count):
    if total == 0 or count == 0:
        return 0
    else:
        return total / count


def printData(x, mean, stdv, px):
    print("%10s%10s%20s%50s" % ("x", "Mean", "standDev", "P(X) / MSG"))
    print("%10s%10s%20s%50s" % ("---", "---------", "---------", "---------"))
    px = str(px)
    if px.isdigit():
        px = float(px)
        print("%10.2f%10.2f%20.2f%50.4f" % (x, mean, stdv, px))
    else:
        print("%10.2f%10.2f%20.2f%50s" % (x, mean, stdv, px))


main()
