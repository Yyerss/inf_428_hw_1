import math

def time_to_cyclic_features(hour):
    if not (0 <= hour < 24):
        raise ValueError("Hour must be в диапазоне [0, 24)")
    radians = (hour / 24) * 2 * math.pi
    return round(math.sin(radians), 4), round(math.cos(radians), 4)
