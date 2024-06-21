#!/usr/bin/python3
"""
This module provides a function to determine the fewest number of coins needed
to meet a given amount total using given coin denominations.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): A list of the values of the coins in your possession.
        total (int): The amount to be made with the coins.

    Returns:
        int: The fewest number of coins needed to meet the total. If the total
        cannot be met by any number of coins you have, return -1.
    """
    if total <= 0:
        return 0

    # Initialize dp array with infinity
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins to make amount 0

    # Dynamic programming to fill dp array
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    # Check if we have a solution for the total
    return dp[total] if dp[total] != float('inf') else -1
