from tandom import *
from tkinter import *
size = 735
window = Tk()
window.title('Froggos')
c = Canvas(window, width=size, height=size)
c.pack()

def froggo(x,y):
    body = c.create_oval(x, y, x + 200, y + 100, fill='purple')
    eye = c.create_oval (x + 70, y - 80, x + 130, y - 20, fill='white')
    eyeball = c.create_oval (x + 90, y - 60, x + 110, y - 40, fill='black')
    mouth = c.create_oval (x + 50, y + 70, x + 150, y + 90, fill='red')
    neck = c.create_line(x + 100, y, x + 100, y - 20)

while True:
    x0 = randint(0, size)
    y0 = randint(0, size)
    d = randint(0, size/5)
    froggo(x0,y0)
    window.update()