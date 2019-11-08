"""
wl = [1, -1] rl = [100, 100] #Line
"""

from random import *

t = 0
mx0 = 800
MOVE = 0

wl = [-1, 2]
rl = [200, 300] 
l = len(wl)
out = []


def f(x, y, r, w, t):
    c = 255
    mx = x + r * cos(w*t)
    my = y - r * sin(w*t)
    trail = createShape(ELLIPSE, x, y , r / 10 , r / 10)
    trail.stroke(c)
    shape(trail)
    stroke(c)
    line(x, y, mx, my)
    node = createShape(ELLIPSE, mx, my , 5, 5)
    node.fill(c)
    shape(node)
    return mx, my
    
def setup():
    size(1600, 900)
    
def drawone(wl, rl, l, my, c = color(randint(0, 255), randint(0, 255), randint(0, 255)) ):
    global t, mx, out
    background(0)
    for i in range(l):
        mx, my = f(mx, my, rl[i], wl[i], t)
    if [mx, my] not in out: out.append([mx, my])
    for i in range(len(out)):
        try:
            stroke(c)
            line(out[i][0], out[i][1], out[i+1][0], out[i+1][1])
            out[i][0] += 30* (sum([abs(i) for i in wl]) / float(l)) if MOVE else 0
        except:
            pass
            if out[i][0] > width: out.remove(out[i])

    t += 0.05

def draw():
    global wl, rl, l, mx
    background(255)
    mx = mx0
    drawone(wl, rl, l, height//2)
    
