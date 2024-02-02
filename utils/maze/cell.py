from graphics import *

class Cell:
    Normal = 1
    Wall = 2
    Start = 3
    End = 4

    def __init__(self, pos):
        self.pos = pos
        
        self.x = pos[0]
        self.y = pos[1]

        self.type = self.Normal
        self.size = 30
        self.border = 1

    def draw(self, win, col=None):
        p1 = Point(self.pos[0]*self.size + (self.pos[0]+1)*self.border, self.pos[1]*self.size + (self.pos[1]+1)*self.border)
        p2 = Point(p1.x + self.size, p1.y + self.size)

        rect = Rectangle(p1, p2)
        text = None

        if col != None:
            rect.setFill(col)
        elif self.type == self.Normal:
            rect.setFill('black')
        elif self.type == self.Wall:
            rect.setFill('grey')
        elif self.type == self.Start:
            rect.setFill('lightgreen')
        elif self.type == self.End:
            rect.setFill('red')

        rect.draw(win)

    def drawWithCustomColor(self, win, col):
        self.draw(win, col)

    def drawText(self, win, text):
        p1 = Point(self.pos[0]*self.size + (self.pos[0]+1)*self.border, self.pos[1]*self.size + (self.pos[1]+1)*self.border)

        t = Text(Point(p1.x + self.size / 2, p1.y + self.size / 2), text)
        t.setTextColor('blue')
        t.setSize(6)

        t.draw(win)