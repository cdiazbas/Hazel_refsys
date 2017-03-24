# -*- coding: utf-8 -*-
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
# from itertools import product, combinations
fig = plt.figure()
ax = fig.gca(projection='3d')
# ax.set_aspect("equal")

from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        FancyArrowPatch.draw(self, renderer)

##################################################################################
##################################################################################
# INICIALIZACION: #theta nunca 90.0 justo
theta = 21.7
chi = 0.
gamma = 58.0
# hscan = 0.
azul = 'navy'
rojo = 'tomato'
verde = 'lime'
negro = 'black'
gris = 'gray'

##################################################################################
##################################################################################
# AZUL = PLANO DEL CIELO
chi += 180. #fix problem
#draw a point
#ax.scatter([0],[0],[0],color="g", s=100)

#draw a vector
a = Arrow3D([0,1.2*np.cos(chi*np.pi/180.)],[0,0],[0,0], mutation_scale=20, lw=1, arrowstyle="-|>", color=azul)
b = Arrow3D([0,0],[0,1.2*np.cos(chi*np.pi/180.)],[0,0], mutation_scale=20, lw=1, arrowstyle="-|>", color=azul)
c = Arrow3D([0,0],[0,0],[0,1.2], mutation_scale=20, lw=1, arrowstyle="-|>", color=azul)
ax.add_artist(a)
ax.add_artist(b)
ax.add_artist(c)

# draw a plane
xx, yy = np.meshgrid(np.arange(-1,2), np.arange(-1,2))
zz = xx*0.
ax.plot_surface(xx, yy, zz, alpha = 0.4, color=azul)

##################################################################################
##################################################################################
# ROJO = VERTICAL LOCAL

#draw a vector
posix = []
posiz = []
xv = Arrow3D([0,+1*np.cos(theta*np.pi/180.)*np.cos(chi*np.pi/180.)],[0,0],[0,-1*np.sin(theta*np.pi/180.)*np.cos(chi*np.pi/180.)], mutation_scale=20, lw=1, arrowstyle="-|>", color=rojo)
yv = Arrow3D([0,0],[0,1.*np.cos(chi*np.pi/180.)],[0,0], mutation_scale=20, lw=1, arrowstyle="-|>", color=rojo)
zv = Arrow3D([0,1*np.sin(theta*np.pi/180.)],[0,0],[0,1*np.cos(theta*np.pi/180.)], mutation_scale=20, lw=1, arrowstyle="-|>", color=rojo)
ax.add_artist(xv)
ax.add_artist(yv)
ax.add_artist(zv)


# Plane of the sky
xx, yy = np.meshgrid(np.arange(-1,2,1), np.arange(-1,2,1))
zz = -xx*np.tan(theta*np.pi/180.)
ax.plot_surface(xx, yy, zz, alpha = 0.4, color=rojo)
plt.plot([0,1*np.cos(chi*np.pi/180.)],[0,0],ls='--', color=rojo, lw=2)


##################################################################################
##################################################################################
# GAMMA:
gv = Arrow3D([0,0.8*np.cos(gamma*np.pi/180.)*np.cos(chi*np.pi/180.)],[0,0.8*np.sin(gamma*np.pi/180.)*np.cos(chi*np.pi/180.)],[0,0], mutation_scale=20, lw=1, arrowstyle="-|>", color=verde)
ax.add_artist(gv)
ax.text(0.8*np.cos(gamma*np.pi/180.)*np.cos(chi*np.pi/180.), 0.8*np.sin(gamma*np.pi/180.)*np.cos(chi*np.pi/180.), 0., r'$e_1$', zdir=None)


##################################################################################
##################################################################################
# hscan: horizontal del scan
# gv = Arrow3D([0,1*np.cos(hscan*np.pi/180.)],[0,1*np.sin(hscan*np.pi/180.)],[0,0], mutation_scale=20, lw=1, arrowstyle="-|>", color=gris)
# ax.add_artist(gv)
# ax.text(1*np.cos(hscan*np.pi/180.), 1*np.sin(hscan*np.pi/180.), 0., r'$H$', zdir=None)


##################################################################################
##################################################################################
# Texto dentro:
ax.text(0, 0, 1.4, r'$\Omega$', zdir=None)
ax.text(0, 1.2*np.cos(chi*np.pi/180.), 0, 'Y', zdir=None)
ax.text(1.2*np.sin(theta*np.pi/180.), 0, 1.2*np.cos(theta*np.pi/180.), 'Z', zdir=None)
ax.text(1.2*np.cos(theta*np.pi/180.)*np.cos(chi*np.pi/180.), 0, -1.2*np.sin(theta*np.pi/180.)*np.cos(chi*np.pi/180.), 'X', zdir=None)




#ax.plot([.5],[.5],marker=r'$\circlearrowleft$',ms=100)





ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1,1)

ax.view_init(elev=31, azim=52)

#ax.set_xlabel('X axis')
#ax.set_ylabel('Y axis')
#ax.set_zlabel('Z axis')


plt.show()
#plt.savefig('reference.pdf')