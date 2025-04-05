import matplotlib.pylab as plt
import os

def setpic(limitl = None, limitr = None):
    global fig, ax
    fig, ax = plt.subplots()
    if limitl != None and limitr !=None:
        ax.set_xlim(limitl, limitr)
  
def shock(z, u, rho, p, us, ps, rhos, tnow, direction='l'):
    if direction == 'l':
        limit = min(-1, z*tnow-1)
    elif direction == 'r':
        limit = max(1, z*tnow+1)

    ax.plot([limit, z*tnow], [u, u] ,c='g')
    ax.plot([limit, z*tnow], [p, p] ,c='b')
    ax.plot([limit, z*tnow], [rho, rho] ,c='r')

    ax.plot([z*tnow, z*tnow], [u, us], c='g')
    ax.plot([z*tnow, z*tnow], [p, ps], c='b')
    ax.plot([z*tnow, z*tnow], [rho, rhos], c='r')

    return limit

    # ax.plot([0, z*tnow], [us, us], c='g')
    # ax.plot([0, z*tnow], [ps, ps], c='b')
    # ax.plot([z*tnow, us*tnow], [rhos, rhos], c='r')
    

def expan(zhead, ztail, u, rho, p, xspnlftexp, u_spnlftexp, p_spnlftexp, rho_spnlftexp, us, ps, rhos, tnow, direction='l'):
    if direction == 'l':
        limit = min(-1, zhead*tnow-1)
    elif direction == 'r':
        limit = max(1, zhead*tnow+1)
    ax.plot([limit, zhead*tnow], [u,u] ,c='g')
    ax.plot([limit, zhead*tnow], [p,p] ,c='b')
    ax.plot([limit, zhead*tnow], [rho, rho] ,c='r')

    ax.plot(xspnlftexp, u_spnlftexp, c='g')
    ax.plot(xspnlftexp, p_spnlftexp, c='b')
    ax.plot(xspnlftexp, rho_spnlftexp, c='r')

    # ax.plot([0, ztail*tnow], [us, us], c='g')
    # ax.plot([0, ztail*tnow], [ps, ps], c='b')
    # ax.plot([ztail*tnow, us*tnow], [rhos, rhos], c='r')

    return limit

def middle(us, ps, tnow, rho1s, rho2s, z1, z2):
    ax.plot([z1*tnow, z2*tnow], [us, us], 'g', label='u')
    ax.plot([z1*tnow, z2*tnow], [ps, ps], 'b', label='p')
    ax.plot([z1*tnow, z2*tnow], [us, us], 'g')
    ax.plot([z1*tnow, us*tnow], [rho1s, rho1s], c='r', label='rho')
    ax.plot([us*tnow, us*tnow], [rho1s, rho2s], c='r')
    ax.plot([us*tnow, z2*tnow], [rho2s, rho2s], c='r')

def show():
    plt.grid()
    plt.legend()
    plt.show()
    plt.close()
def save(tnow = None, video = False):
    plt.grid()
    plt.legend()
    if video == True:
        try:
            plt.savefig(rf'.\pic\{str(tnow).zfill(3)}.png', dpi=300)
        except:
            os.mkdir(r'.\pic')
            plt.savefig(rf'.\pic\{str(tnow).zfill(3)}.png', dpi=300)
        plt.close()
    plt.savefig('Riemann.png', dpi=300)
    plt.close()



