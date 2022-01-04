#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0 and len(tuple_b) == 0:
        return (0, 0)
    elif len(tuple_a) == 1 and len(tuple_b) == 1:
        rtupla = (tuple_a[0] + tuple_b[0], 0 + 0)
    elif len(tuple_a) == 0:
        return tuple_b
    elif len(tuple_b) == 0:
        return tuple_a
    elif len(tuple_a) == 1 and len(tuple_b) == 2:
        rtupla = (tuple_a[0] + tuple_b[0], 0 + tuple_b[1])
    elif len(tuple_a) == 2 and len(tuple_b) == 1:
        rtupla = (tuple_a[0] + tuple_b[0], tuple_a[1] + 0)
    else:
        rtupla = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return rtupla
