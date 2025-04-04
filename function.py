import numpy as np
import bisect

gamma =1.4

def f(ps, pi, rhoi, method=1):
    ci = (gamma * pi / rhoi)**0.5
    if method == 2:
        return (ps - pi) / (
            (rhoi*ci)*(((gamma + 1) / (2 * gamma) * (ps / pi) + (gamma - 1) / (2 * gamma))**0.5)
        )
    elif method == 3 :
        return 2 * ci / (gamma - 1) * ((ps / pi) ** ((gamma - 1) / (2 * gamma)) - 1)
    if ps > pi:
        return (ps - pi) / (
            (rhoi*ci)*(((gamma + 1) / (2 * gamma) * (ps / pi) + (gamma - 1) / (2 * gamma))**0.5)
        )
    elif ps < pi:
        return 2 * ci / (gamma - 1) * ((ps / pi) ** ((gamma - 1) / (2 * gamma)) - 1)
    else:
        return 0
    
def judge(f0, fp1, fp2, u1, u2, p1, p2):
    u1_u2 = u1 - u2
    if p2 >= p1:
        breakpoints = [f0, fp1, fp2]
        situation = ['5', '4', '3', '1']
        return situation[bisect.bisect_right(breakpoints, u1_u2)]
    else:
        breakpoints = [f0, fp2, fp1]
        situation = ['5', '4', '2', '1']
        return situation[bisect.bisect_right(breakpoints, u1_u2)]
