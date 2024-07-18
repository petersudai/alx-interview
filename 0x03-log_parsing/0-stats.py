#!/usr/bin/python3
import sys


def print_stats(total_size, status_counts):
    """
    Print the accumulated metrics
    """
    print(f"File size: {total_size}")
    for status in sorted(status_counts.keys()):
        if status_counts[status] > 0:
            print(f"{status}: {status_counts[status]}")

total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        
        if len(parts) > 6:
            try:
                status_code = int(parts[-2])
                file_size = int(parts[-1])

                total_size += file_size

                if status_code in status_counts:
                    status_counts[status_code] += 1

                line_count += 1

                if line_count % 10 == 0:
                    print_stats(total_size, status_counts)

            except (ValueError, IndexError):
                continue

except KeyboardInterrupt:
    pass
finally:
    print_stats(total_size, status_counts)
