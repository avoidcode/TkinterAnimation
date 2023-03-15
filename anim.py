import tkinter as tk
from shader import shader
from threading import Thread

def pyshader(w, h, t):
    scr = bytearray((0, 0, 0) * w * h)
    for y in range(h):
        wy = w * y
        for x in range(w):
            p = (wy + x) * 3
            scr[p:p + 3] = [min(abs(int(c * 255)), 255) for c in shader(x / w, y / h, t)]
    return bytes(f'P6\n{w} {h}\n255\n', 'ascii') + scr

label = tk.Label()
label.pack()
img = tk.PhotoImage()
label.configure(image=img)

def render():
    global img
    time = 0
    while True:
        img.configure(data=pyshader(256, 256, time))
        time += 1

if __name__ == "__main__":
    render_thread = Thread(target=render)
    render_thread.daemon = True
    render_thread.start()

    tk.mainloop()