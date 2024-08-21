#!/usr/bin/python3
"""
This module provides solution to the "Change comes from within" problem
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to make the given total
    """
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    # Fill dp array using dynamic programming
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1
