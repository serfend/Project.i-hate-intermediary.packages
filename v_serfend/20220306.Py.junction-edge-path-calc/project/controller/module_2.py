
from asyncio import constants
from configuration.Constances import Constances
constances = Constances()


def main(x8, items):
    result = [handle_single(x, x8) for x in items]
    return result

# result:当key=1时返回Ti(d)，否则返回None
def handle_single(item, x8):
    y4 = 0  # η4
    y5 = 0  # η5
    y6 = 0  # η6
    li = item.max_edge_length  # 取周围边的最大长度
    lamata_i = item.Li
    key = item.key
    if key == 0:
        return None
    if x8 <= constances.r2:
        if li <= 200:
            y4 = lamata_i
        else:
            y4 = lamata_i * (0.0013*li+0.73)
        y5 = 1
        y6 = 1
    else:
        if li <= 200:
            y4 = lamata_i
        else:
            y4 = lamata_i * (0.0013*li+0.73)
        di = item.Di
        if di <= 1:
            y5 = 1
        elif di == 2:
            y5 = 0.9
        elif di >= 3:
            y5 = 0.8
        land_use = item.land_use
        if land_use == 1:
            y6 = 1.2
        elif land_use == 2:
            y6 = 0.9

    xi = y4 * y5 * y6 * x8
    tid = 0
    Ti = item.Ti
    Ci = item.Ci
    if xi <= constances.r2:
        state_A1 = (Ti*pow((1-lamata_i), 2))
        state_A2 = 2 * (1-lamata_i*xi)
        state_B1 = pow(xi, 2)
        state_B2 = 2 * Ci * xi * (1-xi)
        tid = 0.9 * (state_A1/state_A2 + state_B1 / state_B2)
    else:
        state_A1 = (Ti*pow((1-lamata_i), 2))
        state_A2 = 2 * (1-lamata_i*xi)
        state_B1 = 1.5 * (xi-constances.r2)
        state_B2 = 1 - xi
        tid = state_A1/state_A2 + state_B1 / state_B2
    item.result = tid
    return tid
        
