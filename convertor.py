from math import trunc


def hours_to_degree(h):
    """Convert hours to degree
        2.225 (h) -> 33.375 (°)
    """
    return h*15


def degree_to_hours(d):
    """Convert degree to hours
       33.375 (°) -> 2.225 (h)
    """
    return d/15


def str_to_hours(s):
    """Convert str to hours
       '02h 13m 30s' -> 2.225 (h)
    """
    h = 0
    for pos in range(8, -1, -4):
        h /= 60
        h += int(s[pos:pos+2])
    return h


def hours_to_str(h):
    """Convert hours to str
       2.225 (h) ->  '02h 13m 30s'
    """
    n = trunc(h)
    h -= n
    h *= 60
    m = trunc(h)
    h -= m
    h *= 60
    s = trunc(h)

    return f'{n}h {m}m {s}s'


def str_to_degree(s):
    """Convert str to degree
       '+33° 22’ 30''' -> 33.375 (°)
    """
    d = 0
    for pos in range(9, 0, -4):
        d /= 60
        d += int(s[pos:pos+2])
    return -d if s[0]=='-' else d


def degree_to_str(d):
    """Convert degree to str
       33.375 (°) ->  '+33° 22’ 30"'
    """
    z = '-' if d < 0 else '+'
    if d < 0: d *= -1
    n = trunc(d)
    d -= n
    d *= 60
    m = trunc(d)
    d -= m
    d *= 60
    s = trunc(d)

    return f'{z}{n}° {m}’ {s}'''


def time_to_str(t):
    h = trunc(t)
    m = trunc((t-h)*60)
    return f'{h//10}{h%10}:{m//10}{m%10}'
