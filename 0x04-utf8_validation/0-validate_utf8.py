#!/usr/bin/python3
"""
method that determines if a given data set represents a valid UTF-8 encoding
"""
def validUTF8(data):
    def get_num_of_bytes(num):
        if num & 0x80 == 0x00:
            return 1
        elif num & 0xE0 == 0xC0:
            return 2
        elif num & 0xF0 == 0xE0:
            return 3
        elif num & 0xF8 == 0xF0:
            return 4
        return -1

    num_bytes = 0

    for num in data:
        if num_bytes == 0:
            num_bytes = get_num_of_bytes(num)
            if num_bytes == -1:
                return False
            if num_bytes > 1:
                num_bytes -= 1
        else:
            if num & 0xC0 != 0x80:
                return False
            num_bytes -= 1

    return num_bytes == 0
