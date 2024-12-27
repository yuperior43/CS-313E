'''File: maximum_profit.py
   Description: Outputs a single float number with 2 decimal points only which
   is the maximum possible profit by purchasing a subset of listed houses and selling
   them in the next year. Takes as input the amount of investment in million USD, the 
   number of houses listed for sale, a list of house prices in million USD, and a list
   of the forecasted increase in percent.

   Student Name: Primo M. Marquez
   Student UT EID: pmm2734

   Course Name: CS 313E
   Unique Number: 52590
   Date Created: November 12, 2023
   Date Last Modified: November 12, 2023'''

import sys

def main():
    '''This is the main function.'''

    # The first line is the amount of investment in million USD which is an integer number.
    line = sys.stdin.readline()
    line = line.strip()
    money = int(line)

    # The second line includes an integer number which is the number of houses listed for sale.
    line = sys.stdin.readline()
    line = line.strip()
    _ = int(line)

    # The third line is a list of house prices in million dollar which is a list of integers
    line = sys.stdin.readline()
    line = line.strip()
    prices = line.split(",")
    for i, _ in enumerate(prices):
        prices[i] = int(prices[i])

    # read the number of vertices
    line = sys.stdin.readline()
    line = line.strip()
    increase = line.split(",")
    for i, _ in enumerate(increase):
        increase[i] = float(increase[i])

    # getting the maximum profit given money, list of prices, and forecasted increase
    result = max_profit(prices, increase, money)

    # Add your functions and call them to generate the result.
    print(result)

def max_profit(prices, increase, money):
    '''Calculates the maximum profit given prices of a list of houses, forecasted value increase, 
    and the amount of investment.'''

    # this is a modified Knapsack problem
    n = len(prices)
    dp = [[0 for _ in range(money + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(money + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif prices[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], increase[i - 1] * prices[i - 1]
                               / 100.0 + dp[i - 1][j - prices[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]

    return round(dp[n][money], 2)

main()
