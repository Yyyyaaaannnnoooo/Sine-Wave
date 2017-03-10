def map(val, iL, iH, oL, oH):
   return (val-iL)* (oH-oL)/(iH-iL) + oL;
def timestamp():
   import time
   timestr = time.strftime("%Y%m%d-%H%M%S")
   return timestr
def circle(posX, posY, w, h):
    loop = 30
    count = 0
    for a in range(loop):
        angle = map(a, 0, loop, 0, 2 * pi)
        x = cos(angle) * (w / 2)
        y = sin(angle) * (h / 2)
        oval(posX + x, posY + y, 3, 3) # circle size
    
w = 500
h = 500
r = 10
loop = 50
sineOff = 0.1
nW = 25
nD = loop
PI = 20 * pi # here you define the number of waves
print w / (loop * 0.7)
for i in range(loop):
    newPage(w, h)
    fill(0)
    rect(0, 0, w, h)
    fill(None)
    #strokeWidth(1)
    x = w / 2
    y = h / 2
    for k in range(nD):
        rad = r + k * (w / loop)
        #x = w / 2 - rad * 0.5
        #y = h / 2 - rad * 0.3
        factor = k
        begin = 0 
        to = PI 
        angle = map(i + k, 0, loop + nD, begin, to)
        cosOff = sin(angle)
        height =  3 * cosOff # define the height of the wave
        c = map(i + k, 0, loop + nD, begin, to / 2)
        col = abs(sin(c))
        fill(1, col, 0)# color?
        circle(x, y + height, rad, rad * 0.6)
saveImage("wave" + timestamp() + ".gif")