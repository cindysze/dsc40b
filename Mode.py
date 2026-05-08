def mode(numbers):
    counts = {}
    max_count = 0
    mode_value = None

    for num in numbers:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

        if counts[num] > max_count:
            max_count = counts[num]
            mode_value = num

    return mode_value
