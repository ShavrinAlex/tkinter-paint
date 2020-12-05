from tkinter import *


def draw(event):
    x1 = event.x - scale.get()
    y1 = event.y - scale.get()
    x2 = event.x + scale.get()
    y2 = event.y + scale.get()
    canvas.create_oval(x1, y1, x2, y2, fill=color.get(), outline=color.get())


# Create window.
root = Tk()
root['bg'] = '#838181'

# Settings canvas.
canvas_width = 500
canvas_height = 500
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.grid(row=2, column=0, columnspan=10)

# Create button clear.
btn_canvas_clear = Button(root, bg='#39c3f9', text='Clear', command=lambda: canvas.delete('all'))
btn_canvas_clear.grid(row=0, column=0, stick='nswe')

# Create brush size.
scale = Scale(root, from_=2, to=32, orient=HORIZONTAL)
scale.grid(row=0, column=1, stick='nswe')

# Create frame colors.
frame_colors = Frame(root)
frame_colors.grid(row=0, column=2, stick='nsw')

# Create colors.
color = StringVar()
color.set('#000000')

btn_red = Radiobutton(frame_colors, value='#ff0000', variable=color, bg='#ff0000')
btn_red.grid(row=0, column=0)

btn_black = Radiobutton(frame_colors, value='#000000', variable=color, bg='#000000')
btn_black.grid(row=1, column=0)

btn_green = Radiobutton(frame_colors, value='#11f20d', variable=color, bg='#11f20d')
btn_green.grid(row=1, column=1)

btn_white = Radiobutton(frame_colors, value='#ffffff', variable=color, bg='#ffffff')
btn_white.grid(row=0, column=1)

btn_yellow = Radiobutton(frame_colors, value='#f8ee35', variable=color, bg='#f8ee35')
btn_yellow.grid(row=0, column=2)

btn_pink = Radiobutton(frame_colors, value='#d54cfa', variable=color, bg='#d54cfa')
btn_pink.grid(row=1, column=2)

# Create brush.
canvas.bind('<B1-Motion>', draw)


root.mainloop()