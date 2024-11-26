import math

def cyclic_time_difference_trig(time1, time2):

    if not (0 <= time1 < 24) or not (0 <= time2 < 24):
        raise ValueError("Время должно быть в диапазоне [0, 24)")

    theta1 = (time1 / 24) * 2 * math.pi
    theta2 = (time2 / 24) * 2 * math.pi

    angle_diff = math.fabs(theta1 - theta2) % (2 * math.pi)

    min_angle = min(angle_diff, 2 * math.pi - angle_diff)
    hour_diff = (min_angle / (2 * math.pi)) * 24
    return round(hour_diff, 4)
