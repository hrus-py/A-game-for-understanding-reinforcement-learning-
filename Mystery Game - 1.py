from tkinter import *
import matplotlib
matplotlib.use('Agg')

global pos
global capture 
global circle
pos = 2
capture = 0

def clicked_zero(event):
    global pos, capture
    if capture == 0:
        if pos == 2 or pos == 7 or pos == 5 or pos == 10 or pos == 15 or pos == 20 or pos == 25 or pos == 16 or pos == 18 or pos == 21 or pos == 23:
            pos
        else:
            pos = pos + 1
            C.move(square, right[0], right[1])
    else:
        if pos == 2 or pos == 7 or pos == 5 or pos == 10 or pos == 15 or pos == 20 or pos == 25 or pos == 16 or pos == 18 or pos == 21 or pos == 23:
            pos
        else:
            pos = pos + 1
            C.move(square, right[0], right[1])
            C.move(circle, right[0], right[1])


def clicked_four(event):
    global pos, capture
    if capture == 0:
        if pos == 21 or pos == 22 or pos == 23 or pos == 24 or pos == 25:
            pos
        else:
            pos = pos + 5
            C.move(square, down[0], down[1])
    else:
        if pos == 21 or pos == 22 or pos == 23 or pos == 24 or pos == 25:
            pos
        else:
            pos = pos + 5
            C.move(square, down[0], down[1])
            C.move(circle, down[0], down[1])

def clicked_two(event):
    global pos, capture
    if capture == 0:
        if pos == 1 or pos == 2 or pos == 3 or pos == 4 or pos == 5:
            pos
        else:
            pos = pos - 5
            C.move(square, up[0], up[1])
    else:
        if pos == 1 or pos == 2 or pos == 3 or pos == 4 or pos == 5:
            pos
        else:
            pos = pos - 5
            C.move(square, up[0], up[1])
            C.move(circle, up[0], up[1])

def clicked_five(event):
    global pos, capture
    if capture == 0:
        if pos == 1 or pos == 6 or pos == 11 or pos == 16 or pos == 21 or pos == 3 or pos == 8 or pos == 17 or pos == 22 or pos == 19 or pos == 24:
            pos
        else:
            pos = pos - 1
            C.move(square, left[0], left[1])
    else:
        if pos == 1 or pos == 6 or pos == 11 or pos == 16 or pos == 21 or pos == 3 or pos == 8 or pos == 17 or pos == 22 or pos == 19 or pos == 24:
            pos
        else:
            pos = pos - 1
            C.move(square, left[0], left[1])
            C.move(circle, left[0], left[1])

def clicked_three(event):
    global pos, capture, circle
    if pos == 1:
        C.delete(circle)
        capture = 1
        circle = C.create_oval(30, 30, 60, 60, fill = "green")

def clicked_one(event):
    global pos
    if pos == 5:
        #circle = C.create_oval(300, 20, 350, 70, outline = "green", fill = "green")
        C.delete(circle)

root = Tk()
root.title("Mystery Game - 1")
C = Canvas(root, bg="white", relief = FLAT, height=600, width=900)

for i in range(5):
    for j in range(5):
        coord = (10+(i*70)), (10+(j*70)), (80+(i*70)), (80+(j*70))
        if (i+j == 0):
            C.create_rectangle(coord, fill = "red")
        elif (i== 0 and j == 4):
            C.create_rectangle(coord, fill = "blue")
        elif (i== 4 and j == 0):
            C.create_rectangle(coord, fill = "green")
        elif (i== 4  and j == 4):
            C.create_rectangle(coord, fill = "orange")
        else:
            C.create_rectangle(coord)
            
line1 = C.create_line(150,10,150,150, width = 4)
line1 = C.create_line(80,220,80,360, width = 4)
line1 = C.create_line(220,220,220,360, width = 4)

rect = 90, 20, 140, 70
square= C.create_rectangle(rect, fill = "yellow")

circle = C.create_oval(20, 20, 70, 70, fill = "green")
                   
right = 70,0
down = 0,70
up = 0,-70
left = -70,0

text1 = C.create_text(620, 20, text="CLICK ON ANY NUMBER FROM 0 TO 5 TO PLAY THE GAME", font = 14)
zero = C.create_text(600, 80, text="0", font = 24)
one = C.create_text(600, 160, text="1", font = 24)
two = C.create_text(600, 240, text="2", font = 24)
three = C.create_text(600, 320, text="3", font = 24)
four = C.create_text(600, 400, text="4", font = 24)
five = C.create_text(600, 480, text="5", font = 24)
C.pack()

C.tag_bind(zero, "<Button-1>", clicked_zero) 
C.tag_bind(one, "<Button-1>", clicked_one)
C.tag_bind(two, "<Button-1>", clicked_two)
C.tag_bind(three, "<Button-1>", clicked_three)
C.tag_bind(four, "<Button-1>", clicked_four)
C.tag_bind(five, "<Button-1>", clicked_five)

root.mainloop()
    

