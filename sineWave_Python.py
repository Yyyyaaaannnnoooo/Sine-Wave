def map(val, iL, iH, oL, oH):
   return (val-iL)* (oH-oL)/(iH-iL) + oL;
def timestamp():
   import time
   timestr = time.strftime("%Y%m%d-%H%M%S")
   return timestr
def circle(posX, posY, w, h, count):
    loop = 6 #define the edges of your polygon
    pt = []
    save()
    translate(posX, posY)
    for a in range(loop):
        angle = map(a, 0, loop, 0 + count, 2 * pi + count)
        angles = (cos(angle) * (w / 2), sin(angle) * (h / 2))
        #oval(posX + x, posY + y, 3, 3) # circle size # turn on and off to switch between points and shapes
        pt.append(angles)
    polygon(*pt)
    restore()
    
w = 500
h = 500
r = 10
loop = 50
sineOff = 0.1
nW = 25
nD = loop
PI = 4 * pi # here you define the number of waves
print w / (loop * 0.7)
for i in range(loop):
    newPage(w, h)
    fill(0)
    rect(0, 0, w, h)
    fill(None)
    #strokeWidth(1)
    x = 0
    y = 0
    count = 0
    for k in range(nD):
        rad = r + k * (w / loop)
        #x = w / 2 - rad * 0.5
        #y = h / 2 - rad * 0.3
        factor = k
        begin = 0 
        to = PI 
        angle = map(i + k, 0, loop + nD, begin, to)
        cosOff = sin(angle)
        height =  15 * cosOff # define the height of the wave
        c = map(i + k, 0, loop + nD, begin, to / 2)
        col = abs(sin(c))
        stroke(col, 0, 1)# color? change between fill and stroke to match with the point visualization
        circle(w /2, (h / 2) + height, rad, rad * 0.6, count)
        count += 0.02
saveImage("wave" + timestamp() + ".gif")