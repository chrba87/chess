import tkinter as tk

root = tk.Tk()

height = 800
width = 800
eightW = width / 8
eightH = height / 8

canvas = tk.Canvas(root, height=height, width=width)

fill = True
for i in range(8):
    fill = not fill
    for j in range(8):
        if fill:                
            rec = canvas.create_rectangle(eightW * j, eightH *i, eightW * (j+1), eightH * (i+1), fill="black") 
        else:
            rec = canvas.create_rectangle(eightW * j, eightH *i, eightW * (j+1), eightH * (i+1))
        fill = not fill

canvas.create_oval(width / 32, height / 32 * 29, width / 32 * 3, height / 32 * 31, fill="blue")

canvas.pack()
root.mainloop()