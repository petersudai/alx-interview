#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened starting from the first box
    """

    # Check if boxes list is empty or None
    if not boxes:
        return False

    # Set to track which boxes have been unclocked
    unlocked_boxes = set()

    # Initially, the first box is unlocked
    unlocked_boxes.add(0)

    # Stack to manage the boxes to be explored
    stack = [0]

    # While there are boxes to explore
    while stack:
        # Pop a box from the stack
        current_box = stack.pop()
        # Iterate over each key in the current box
        for key in boxes[current_box]:
            # Check if the key unlocks a new box and the box index is valid
            if key not in unlocked_boxes and key < len(boxes):
                # Unlock the new box
                unlocked_boxes.add(key)
                # Add the new box to the stack for further exploration
                stack.append(key)

    # If all boxes are unlocked, return True; otherwise, reeturn False
    return len(unlocked_boxes) == len(boxes)
