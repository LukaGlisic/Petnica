import matplotlib 
from numpy import *
from pylab import *

x=linspace(-2, 2, 40)
y=linspace(-2, 2, 40)
x, y=meshgrid(x, y)

 
def E(q, a, x, y):
    return q*(x-a[0])/((x-a[0])**2+(y-a[1])**2), \
        q*(y-a[1])/((x-a[0])**2+(y-a[1])**2)
# racunjanje vektora
Ex1, Ey1=E(5, [-1, 0], x, y)
Ex2, Ey2=E(5, [1, 0], x, y)
Ex=Ex1+Ex2
Ey=Ey1+Ey2
quiver(x, y, Ex, Ey, pivot='middle', headwidth=4, headlength=6)
show()