#!/usr/bin/python3
"""
Log parsing
"""

import sys

if __name__ == "__main__":
    total_size = 0
    count = 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}

    def print_stats(stats: dict, file_size: int) -> None:
        """
        Print the accumulated statistics.
        """
        print("File size: {:d}".format(file_size))
        for k in sorted(stats.keys()):
            if stats[k]:
                print("{}: {}".format(k, stats[k]))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()

            if len(data) < 7:
                continue

            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except IndexError:
                pass

            try:
                file_size = int(data[-1])
                total_size += file_size
            except (IndexError, ValueError):
                pass

            if count % 10 == 0:
                print_stats(stats, total_size)

        print_stats(stats, total_size)

    except KeyboardInterrupt:
        print_stats(stats, total_size)
        raise
