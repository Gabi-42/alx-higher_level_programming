#!/usr/bin/python3
def add_tuple(tuplea=(), tupleb=()):
    if len(tuplea) > 2:
        tuplea = (tuplea[0], tuplea[1])
    if len(tuplea) == 1:
        tuplea = (tuplea[0], 0)
    if len(tuplea) = 0:
        tuplea = (0, 0)
    if len(tupleb) > 2:
        tupleb = (tupleb[0], tupleb[1])
    if len(tupleb) == 1:
        tupleb = (tupleb[0], 0)
    if len(tupleb) = 0:
        tupleb = (0, 0)
    sum_tup = (tuplea[0] + tupleb[0], tuplea[1] + tupleb[1])
    return sum_tup
