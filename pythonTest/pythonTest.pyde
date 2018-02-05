dia = 150
p = dia/2


class Ellipse:

    def __init__(self, d, tx, ty):
        self.d = d
        self.tx = tx
        self.ty = ty

    def draw(self):
        pushMatrix()
        translate(self.tx, self.ty)
        strokeWeight(2)
        stroke(0)
        noFill()
        ellipse(0, 0, self.d, self.d)
        popMatrix()


class Line:

    def __init__(self, speed, p, tx, ty):
        self.p = p
        self.speed = speed
        self.tx = tx
        self.ty = ty

    def drawX(self):
        self.ang = frameCount * self.speed
        pushMatrix()
        translate(self.tx, self.ty)
        strokeWeight(1)
        self.v = PVector(cos(self.ang)*self.p, height)
        line(self.v.x, self.v.y, self.v.x, -self.v.y)
        self.v = PVector()
        popMatrix()

    def drawY(self):
        self.ang = frameCount * self.speed
        pushMatrix()
        translate(self.tx, self.ty)
        strokeWeight(1)
        self.v = PVector(width, sin(self.ang)*self.p)
        line(self.v.x, self.v.y, -self.v.x, self.v.y)
        popMatrix()


class Point:

    def __init__(self, speed, p, tx, ty):
        self.tx = tx
        self.ty = ty
        self.speed = speed
        self.p = p

    def draw(self):
        self.ang = (frameCount) * self.speed
        pushMatrix()
        translate(self.tx, self.ty)
        strokeWeight(15)
        stroke(155)
        point(cos(self.ang)*self.p, sin(self.ang)*self.p)
        popMatrix()

class intersect:
    pLineX = 0
    pLineY = 0
    def __init__(self, ln1, ln2):
        self.ln1 = ln1
        self.ln2 = ln2
        """self.pLineX = (cos(frameCount*0.025)*ln1.p)+ln1.tx
        self.pLineY = self.ln2.v.y + self.ln2.ty"""
    
    def lissajous(self):
        pushMatrix()
        strokeWeight(5)
        line((cos(frameCount*0.025)*self.ln1.p)+self.ln1.tx, self.ln2.v.y + self.ln2.ty, self.pLineX, self.pLineY)
        popMatrix()
        self.pLineX = (cos(frameCount*0.025)*self.ln1.p) + self.ln1.tx
        self.pLineY = self.ln2.v.y + self.ln2.ty

def setup():
    size(900, 600)
    # frameRate(1)

def draw():
    background(255)
    elx = Ellipse(dia, width/2, 100)
    lx = Line(0.025, p, width/2, 100)
    px = Point(0.025, p, width/2, 100)
    elx.draw()
    lx.drawX()
    px.draw()

    ely = Ellipse(dia, 100, height/2)
    ly = Line(0.025*2, p, 100, height/2)
    py = Point(0.025*2, p, 100, height/2)
    ely.draw()
    ly.drawY()
    py.draw()

    lis1 = intersect(lx, ly)
    lis1.lissajous()