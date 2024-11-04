def time_difference(hour1, hour2):
    diff = abs(hour2 - hour1)
    if diff > 12:
        diff = 24 - diff
    return diff