"""
Name:Sulaiman Khalifa Khalfan Al Yousfi
ID:s133607
HW:2
Purpose:    Write a program that continuously prompt the user for number,mean,stdv then calculates the probability, when
            the stops in calculate the average of all the probabilities and the number of them.
Algorithm:
    Main():
        1)Prompt the user for input.
        2)If the input is less or more than 3 values keep asking.
        3)Assign the values of x, mean, stdv.
        4)While the user didn't enter q q q keep asking.
            1) if x, mean, stdv are all digit.
                1)call process
                2)Ask user again.
            2) else Show error msg and ask again.
        5)Print the average and count.
    Process():
        1)If x is negative turns it to positive.
        2)If the mean = 0 and stdv = 1
            1)Calculate Prob using its function
            2)Add prob to total
            3)Increment count.
        3)else Prob isn't normal
        4)Print the data in a table using PrintData function.
        5)return total and count.


Test:
    Case 1:
        Inputs:
            input1: a a
            input2: -4 0 1
            input2: -2 1 1
            input3: 0 0 1
            input4: 5 0 1
            input5: 2 1 1
            input6: q q q
        Outputs:
            Please Enter x, mean and stdv: a a
            Please input 3 values!!!
            Please Enter x, mean and stdv: -4 0 1
                 x     Mean  standDev          P(X) / MSG
               ------------ ---------           ---------
              4.00     0.00      1.00              0.3986
            Please Enter x, mean and stdv: -2 1 1
                 x     Mean  standDev          P(X) / MSG
               ------------ ---------           ---------
              2.00     1.00      1.00***Not Normal Dist.***
            Please Enter x, mean and stdv: 0 0 1
                 x     Mean  standDev          P(X) / MSG
               ------------ ---------           ---------
              0.00     0.00      1.00             -0.6011
            Please Enter x, mean and stdv: 5 0 1
                 x     Mean  standDev          P(X) / MSG
               ------------ ---------           ---------
              5.00     0.00      1.00              0.3989
            Please Enter x, mean and stdv: 2 1 1
                 x     Mean  standDev          P(X) / MSG
               ------------ ---------           ---------
              2.00     1.00      1.00***Not Normal Dist.***
            Please Enter x, mean and stdv: q q q
            The average prob density of values having normal distribution: 0.0655
            There were 3 values having normal distribution.

"""
# Importing functions and variables.
from math import pi, sqrt, e


def main():
    total = 0
    count = 0
    inpt = input("Please Enter x, mean and stdv: ").split()
    while len(inpt) != 3:
        print("Please input 3 values!!!")
        inpt = input("Please Enter x, mean and stdv: ").split()
    x, mean, stdv = inpt
    while not x == "q" and not mean == "q" and not stdv == "q":
        if ((x[0] == '-' and x[1:].isdigit()) or x.isdigit()) and mean.isdigit() and stdv.isdigit():
            x = float(x)
            mean = float(mean)
            stdv = float(stdv)
            total, count = process(x, mean, stdv, total, count)
            inpt = input("Please Enter x, mean and stdv: ").split()
            while len(inpt) != 3:
                print("Please input 3 values!!!")
                inpt = input("Please Enter x, mean and stdv: ").split()
            x, mean, stdv = inpt
        else:
            print("Invalid input....")
            inpt = input("Please Enter x, mean and stdv: ").split()
            while len(inpt) != 3:
                print("Please input 3 values!!!")
                inpt = input("Please Enter x, mean and stdv: ").split()
            x, mean, stdv = inpt

    print("The average prob density of values having normal distribution:",
          averageProbabilityDensityValue(total, count))
    print("There were", count, "values having normal distribution.")


def calculateProbabilityDensityValue(x):
    px = 1 / sqrt(2 * pi) - e ** ((-x ** 2) / 2)
    return px


def process(x, mean, stdv, total, count):
    if x < 0:
        x = abs(x)
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
