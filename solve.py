from function import f, judge
from sympy import symbols, solve, nsolve, re, im
import numpy as np

def solve_ps(u1, p1, rho1, u2, p2, rho2, methodl=None, methodr=None, med='nsolve', td=1.0):
    u1_u2 = u1 - u2
    ps = symbols('ps')
    fps = f(ps, p1, rho1, methodl) + f(ps, p2, rho2, methodr)
    if med == 'solve':
        ps_solutions = solve(fps-u1_u2, ps)
        valid_ps = []
        for sol in ps_solutions:
            if im(sol) == 0:
                real_sol = re(sol)  # 取实部
                if real_sol > 0:    # 检查是否大于0
                    valid_ps.append(real_sol)
        us_list = []
        for i in valid_ps:
            us_list.append(0.5 * (u1 + u2 -f(i, p1, rho1) + f(i, p2, rho2)))
        return [valid_ps, us_list]
    else:
        # print(fps-u1_u2)
        ps_solution = re(nsolve(fps-u1_u2, ps, td))
        return [ps_solution, 0.5 * (u1 + u2 - f(ps_solution, p1, rho1) + f(ps_solution, p2, rho2))]


#左激波情况下计算激波运行速度与中间区域左侧密度
def calcshock_l(p1, u1, rho1, ps, us):
    z1 = u1 - (ps - p1) / (rho1 * (u1 - us))
    rho1s = rho1 * (u1 - z1) / (us - z1)
    return [z1, rho1s]

# 左膨胀波计算波头波尾速度和左侧密度
def calcexpan_l(p1, u1, rho1, ps, us, gamma, idxcase):
    c1 = (gamma * p1 / rho1)**0.5
    z1head = u1 - c1
    if (idxcase != '5'):
        rho1s = rho1 * (ps / p1) ** (1/gamma)
        c1s = (gamma * ps / rho1s)**0.5
        z1tail = us - c1s
        return [rho1s, z1head, z1tail]
    elif (idxcase == '5'):
        rho1s = 0
        z1tail = u1 - 2*c1/(gamma-1)
        return [rho1s, z1head, z1tail]

# 右激波计算激波速度与中间右侧密度
def calcshock_r(p2, u2, rho2, ps, us):
    z2 = u2 - (ps-p2)/(rho2*(u2-us))
    rho2s = rho2 * (u2-z2) / (us-z2)
    return [z2, rho2s]

# 右膨胀波计算波头波尾速度和右侧密度
def calcexpan_r(p2, u2, rho2, ps, us, gamma, idxcase):
    c2 = (gamma * p2 / rho2)**0.5
    z2head = u2 + c2
    if (idxcase != '5'):
        rho2s = rho2 * (ps/p2)**(1/gamma)
        c2s = (gamma * ps / rho2s)**0.5
        z2tail = us + c2s
        return [rho2s, z2head, z2tail]
    elif (idxcase == '5'):
        rho2s = 0
        z2tail = u2 - 2*c2/(gamma-1)
        return [rho2s, z2head, z2tail]

# 左膨胀波内部速度压力密度
def calclft_l(z1head, z1tail, tnow, gamma, u1, c1, p1):
    xdwn = z1head * tnow
    xup = z1tail * tnow
    xspnlftexp = np.linspace(xdwn, xup, 100)
    c_spnlftexp = (gamma - 1) / (gamma + 1) * (u1 - xspnlftexp/tnow) + 2 * c1 / (gamma + 1)
    u_spnlftexp = xspnlftexp/tnow + c_spnlftexp
    p_spnlftexp = p1 * (c_spnlftexp/c1)**(2 * gamma / (gamma - 1))
    rho_spnlftexp = gamma * p_spnlftexp / c_spnlftexp**2
    return [xspnlftexp, u_spnlftexp, p_spnlftexp, rho_spnlftexp]

# 右膨胀波内部速度压力密度
def calclft_r(z2head, z2tail, tnow, gamma, u2, c2, p2):
    xdwn = z2tail * tnow
    xup = z2head * tnow
    xspnlftexp = np.linspace(xdwn, xup, 100)
    c_spnlftexp = -(gamma-1)/(gamma+1) * (u2-xspnlftexp/tnow) + 2*c2/(gamma+1)
    u_spnlftexp = xspnlftexp/tnow-c_spnlftexp
    p_spnlftexp = p2 * (c_spnlftexp/c2)**(2*gamma/(gamma-1))
    rho_spnlftexp = gamma * p_spnlftexp / c_spnlftexp**2
    return [xspnlftexp, u_spnlftexp, p_spnlftexp, rho_spnlftexp]

def calclft(z1, p1, u1, rho1, tnow):
    lftshockx = z1 * tnow
    x_spnlftwavl = [min(-1, int(lftshockx*2)), lftshockx]
    return x_spnlftwavl

def calclfm(z1, ps, us, rhosl, tnow):
    lftshockx = z1*tnow
    middisconx = us*tnow
    xspnmidl = [lftshockx, middisconx]
    return xspnmidl

def calclrm(z2, ps, us, rhosr, tnow):
    rgtshockx = z2*tnow
    middisconx = us * tnow
    xspnmidr = [middisconx, rgtshockx]
    return xspnmidr

def calclrt(z2, p2, u2, rho2, tnow):
    rgtshockx = z2*tnow
    x_spnrgtwavr = [rgtshockx, max(1, int(rgtshockx * 2))+1]
    return x_spnrgtwavr
