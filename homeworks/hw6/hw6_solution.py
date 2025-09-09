
def level_up(experience: int, threshold: int, reward: int) -> bool:
    return threshold <= experience + reward


def motor_time(n: int) -> int:
    hours = (n // 60) % 24
    minutes = n % 60
    hours1 = hours // 10
    hours2 = hours % 10
    minutes1 = minutes // 10
    minutes2 = minutes % 10
    return hours1 + hours2 + minutes1 + minutes2


def time_converter(time_str: str) -> str:
    time_conv = time_str.split(':')
    hours = int(time_conv[0])
    if hours > 12:
        hours -= 12
        time_conv[0] = str(hours)
        time = ':'.join(time_conv) + ' p.m.'
    elif hours == 0:
        time_conv[0] = '12'
        time = ':'.join(time_conv) + ' a.m.'
    elif hours < 12:
        time_conv[0] = str(hours)
        time = ':'.join(time_conv) + ' a.m.'
    else:
        time = time_str + ' p.m.'
    return time
