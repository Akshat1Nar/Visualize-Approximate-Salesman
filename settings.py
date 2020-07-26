from collections import namedtuple


colours = [(0,1.,0,1.),(1.,0,0,1.),(1.,1.,0,1.),(0,0,1.,1.)]
colorIndex=0

Edge = namedtuple('Edge',['u','v','weight'])
pixel = namedtuple("pixel",['x','y','d'])
d=12
Subst = []
InputGraph = []

graphicsLine = []
graphicsLineInd = 0