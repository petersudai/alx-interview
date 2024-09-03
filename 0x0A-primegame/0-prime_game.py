#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    Determine winner after playing x rounds of the Prime Game
    """
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(max_n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, max_n + 1, i):
                sieve[j] = False

    primes_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        primes_count[i] = primes_count[i - 1] + (1 if sieve[i] else 0)

    maria_wins = 0
    for n in nums:
        if primes_count[n] % 2 != 0:
            maria_wins += 1

    if maria_wins > x / 2:
        return "Maria"
    elif maria_wins < x/ 2:
        return "Ben"
    else:
        return None
