import solve
from function import f, judge
import draw
import numpy as np
import video

def main(tnow, u1, u2, rho1, rho2, p1, p2, video = False):
    # tnow = 0.14
    gamma = 1.4
    # u1 = 0
    # u2 = 2
    # rho1 = 1
    # rho2 = 0.125
    # p1 = 1
    # p2 = 0.1

    c1 = (gamma*p1/rho1)**0.5
    c2 = (gamma*p2/rho2)**0.5

    fp0 = f(0, p1, rho1) + f(0, p2, rho2)
    fp1 = f(p1, p1, rho1) + f(p1, p2, rho2)
    fp2 = f(p2, p1, rho1) + f(p2, p2, rho2)

    idxcase = judge(fp0, fp1, fp2, u1, u2, p1, p2)
    method_dic = {'1' : [2, 2], '2' : [3, 2], '3' : [2, 3], '4' : [3, 3], '5' : [3, 3]}

    if video == False:
        draw.setpic()

    try:
        [ps, us] = solve.solve_ps(u1, p1, rho1, u2, p2, rho2, method_dic[idxcase][0], method_dic[idxcase][1])
    except:
        [ps, us] = solve.solve_ps(u1, p1, rho1, u2, p2, rho2, method_dic[idxcase][0], method_dic[idxcase][1], td=0)

    if (idxcase == '1') or (idxcase == '3'):
        [z1, rho1s] = solve.calcshock_l(p1, u1, rho1, ps, us)

    if (idxcase == '2') or (idxcase == '4') or (idxcase == '5'):
        [rho1s, z1head, z1tail] = solve.calcexpan_l(p1, u1, rho1, ps, us, gamma, idxcase)
        [xspnlftexp1, u_spnlftexp1, p_spnlftexp1, rho_spnlftexp1] = solve.calclft_l(z1head, z1tail, tnow, gamma, u1, c1, p1)

    if (idxcase == '1') or (idxcase == '2'):
        [z2, rho2s] = solve.calcshock_r(p2, u2, rho2, ps, us)
    if (idxcase == '3') or (idxcase == '4') or (idxcase == '5'):
        [rho2s, z2head, z2tail] = solve.calcexpan_r(p2, u2, rho2, ps, us, gamma, idxcase)
        [xspnlftexp2, u_spnlftexp2, p_spnlftexp2, rho_spnlftexp2] = solve.calclft_r(z2head, z2tail, tnow, gamma, u2, c2, p2)

    def match_draw(value):
        match value:
            case '1':
                limitl = draw.shock(z1, u1, rho1, p1, us, ps, rho1s, tnow,)
                limitr = draw.shock(z2, u2, rho2, p2, us, ps, rho2s, tnow, 'r')
                draw.middle(us, ps, tnow, rho1s, rho2s, z1, z2)
            case '2':
                limitl = draw.expan(z1head, z1tail, u1, rho1, p1, xspnlftexp1, u_spnlftexp1, p_spnlftexp1, rho_spnlftexp1, us, ps, rho1s, tnow)
                limitr = draw.shock(z2, u2, rho2, p2, us, ps, rho2s, tnow, 'r')
                draw.middle(us, ps, tnow, rho1s, rho2s, z1tail, z2)
            case '3':
                limitl = draw.shock(z1, u1, rho1, p1, us, ps, rho1s, tnow)
                limitr = draw.expan(z2head, z2tail, u2, rho2, p2, xspnlftexp2, u_spnlftexp2, p_spnlftexp2, rho_spnlftexp2, us, ps, rho2s, tnow, 'r')
                draw.middle(us, ps, tnow, rho1s,rho2s, z1, z2tail)
            case '4':
                limitl = draw.expan(z1head, z1tail, u1, rho1, p1, xspnlftexp1, u_spnlftexp1, p_spnlftexp1, rho_spnlftexp1, us, ps, rho1s, tnow)
                limitr = draw.expan(z2head, z2tail, u2, rho2, p2, xspnlftexp2, u_spnlftexp2, p_spnlftexp2, rho_spnlftexp2, us, ps, rho2s, tnow, 'r')
                draw.middle(us, ps, tnow, rho1s, rho2s, z1tail, z2tail)
        return limitl, limitr

    limitl, limitr = match_draw(idxcase)
    if video == True:
        draw.save(j, video)
    else: 
        draw.save()
    return limitl, limitr

def make_video(u1, u2, rho1, rho2, p1, p2, t1, t2):
    global j
    j = 1
    draw.setpic()
    limitl, limitr = main(t2, u1, u2, rho1, rho2, p1, p2, True)
    for i in np.linspace(t1, t2, int(30*(t2-t1))):
        draw.setpic(int(limitl)-0.2, int(limitr)+0.2)
        main(i, u1, u2, rho1, rho2, p1, p2, True)
        j = j + 1
    video.make_video(j-1)

if __name__ == '__main__':
    j = 1
    draw.setpic()
    limitl, limitr = main(1.1, 3, 0, 1, 0.125, 1, 0.1, True)
    for i in np.linspace(0.1, 1.1, 30):
        draw.setpic(int(limitl)-0.2, int(limitr)+0.2)
        main(i, 3, 0, 1, 0.125, 1, 0.1, True)
        j = j + 1
    main(0.14, 3, 0, 1, 0.125, 1, 0.1, 1)
