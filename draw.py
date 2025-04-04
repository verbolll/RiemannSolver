import matplotlib.pylab as plt

def setpic():
    global fig, ax
    fig, ax = plt.subplots()
  
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

def middle(us, ps, tnow, rho1s, rho2s, z1, z2):
    ax.plot([z1*tnow, z2*tnow], [us, us], 'g')
    ax.plot([z1*tnow, z2*tnow], [ps, ps], 'b')
    ax.plot([z1*tnow, z2*tnow], [us, us], 'g')
    ax.plot([z1*tnow, us*tnow], [rho1s, rho1s], c='r')
    ax.plot([us*tnow, us*tnow], [rho1s, rho2s], c='r')
    ax.plot([us*tnow, z2*tnow], [rho2s, rho2s], c='r')

def show():
    plt.grid()
    plt.show()
    plt.close()
def save():
    plt.grid()
    plt.savefig('Riemann.png', dpi=300)
    plt.close()



