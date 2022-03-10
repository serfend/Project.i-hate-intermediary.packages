from asyncio import constants
from configuration.Constances import Constances
constances = Constances()


def main(x8, items):
    result = [handle_single(x, x8) for x in items]
    return result


def handle_single(item, x8):
    y1 = 0  # η1
    y2 = 0  # η2
    h = item.highway
    k = item.key
    if x8 >= constances.a1 and x8 <= constances.a2:
        y1 = 1
        y2 = 1
    elif x8 > constances.a2 and x8 <= constances.a3:
        dict_highway = {1: 1.375,  2: 1.0,  3: 0.75,  4: 0.75}
        dict_key = {1: 1.2,  0: 0.9}
        y1 = dict_highway[h]
        y2 = dict_key[k]
    elif x8 > constances.a3:
        dict_highway = {1: 1.5,  2: 1.125,  3: 0.9,  4: 0.9}
        dict_key = {1: 1.3,  0: 1.1}
        y1 = dict_highway[h]
        y2 = dict_key[k]

    xj = y1 * y2 * x8
    vj = 0
    if xj <= constances.r1:
        vj = constances.a1 - constances.b1 * xj
    else:
        vj = constances.vf / (1+constances.a2*(pow(xj, constances.b2)))

    result = item.length / vj
    item.result = result
    return result
