import math

def format_time_value(value = 0):
    format = str(value)
    
    if len(format) == 1:
        return "0" + format
    else:
        return format

def what_time_is_it(angle = 0):
    hour = 0
    minutes = (angle / 360) * 12

    if angle < 30:
        hour += 12
    else:
        hour += math.floor((angle / 360) * 12)

    if minutes.is_integer():
        minutes = "00"
    else:
        intValue = math.floor(minutes)
        deci = abs(minutes - intValue) * 60

        top = math.ceil(deci)

        if abs(top - deci) < 0.001:
            minutes = math.ceil(deci)
        else:
            minutes = math.floor(deci)

    return format_time_value(hour) + ":" + format_time_value(minutes)