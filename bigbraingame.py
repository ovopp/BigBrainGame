import random
import tkinter as tk
from functools import partial
import time

window = tk.Tk()

game_arr = []
array = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]
random.shuffle(array)
window.geometry("1000x1000")

canvas = tk.Canvas(window, width=900, height=900, bg='white')
canvas.pack()

image_list = [
    tk.PhotoImage(file='colors/red.png'),
    tk.PhotoImage(file='colors/green.png'),
    tk.PhotoImage(file='colors/blue.png'),
    tk.PhotoImage(file='colors/yellow.png'),
    tk.PhotoImage(file='colors/orange.png'),
]

for i in range(5):
    tmp_arr = []
    for j in range(5):
        tmp_arr.append(array[5 * i + j])
    game_arr.append(tmp_arr)


def drawGrid():
    global game_arr
    for i in range(5):
        for j in range(5):
            image = image_list[game_arr[i][j] - 1]
            canvas.create_image(50 + (j + 1) * 120, 50 + (i + 1) * 120, image=image)


drawGrid()
t0 = time.time()


def move(inp):
    global game_arr
    idx = int(inp[0])
    print(idx)
    if inp[1] is "R":
        game_arr[idx].insert(0, game_arr[idx][4])
        game_arr[idx].pop(5)
    elif inp[1] is "L":
        tmp_elem = game_arr[idx][0]
        game_arr[idx].pop(0)
        game_arr[idx].append(tmp_elem)
    elif inp[1] is "U":
        tmp = game_arr[0][idx]
        for val in range(4):
            game_arr[val][idx] = game_arr[val + 1][idx]
        game_arr[4][idx] = tmp
    else:
        tmp_elem = game_arr[4][idx]
        for var in reversed(range(4)):
            game_arr[var + 1][idx] = game_arr[var][idx]
        game_arr[0][idx] = tmp_elem
    drawGrid()


def checkGrid():
    global game_arr
    global t0
    for x in range(1, 6):
        for item in game_arr[x - 1]:
            if item is not x:
                return False
    t1 = time.time() - t0
    tk.Label(window, text=t1).pack()


# bottom direction
b2d = tk.Button(window, text="v", command=partial(move, "2D"))
canvas.create_window(50 + 3 * 120, 750, window=b2d)

b3d = tk.Button(window, text="v", command=partial(move, "3D"))
canvas.create_window(50 + 4 * 120, 750, window=b3d)

b4d = tk.Button(window, text="v", command=partial(move, "4D"))
canvas.create_window(50 + 5 * 120, 750, window=b4d)

b1d = tk.Button(window, text="v", command=partial(move, "1D"))
canvas.create_window(50 + 2 * 120, 750, window=b1d)

b0d = tk.Button(window, text="v", command=partial(move, "0D"))
canvas.create_window(50 + 1 * 120, 750, window=b0d)

# up direction

b0u = tk.Button(window, text="^", command=partial(move, "0U"))
canvas.create_window(50 + 1 * 120, 50, window=b0u)

b1u = tk.Button(window, text="^", command=partial(move, "1U"))
canvas.create_window(50 + 2 * 120, 50, window=b1u)

b2u = tk.Button(window, text="^", command=partial(move, "2U"))
canvas.create_window(50 + 3 * 120, 50, window=b2u)

b3u = tk.Button(window, text="^", command=partial(move, "3U"))
canvas.create_window(50 + 4 * 120, 50, window=b3u)

b4u = tk.Button(window, text="^", command=partial(move, "4U"))
canvas.create_window(50 + 5 * 120, 50, window=b4u)

# left direction

b0l = tk.Button(window, text="<", command=partial(move, "0L"))
canvas.create_window(50, 50 + 1 * 120, window=b0l)

b1l = tk.Button(window, text="<", command=partial(move, "1L"))
canvas.create_window(50, 50 + 2 * 120, window=b1l)

b2l = tk.Button(window, text="<", command=partial(move, "2L"))
canvas.create_window(50, 50 + 3 * 120, window=b2l)

b3l = tk.Button(window, text="<", command=partial(move, "3L"))
canvas.create_window(50, 50 + 4 * 120, window=b3l)

b4l = tk.Button(window, text="<", command=partial(move, "4L"))
canvas.create_window(50, 50 + 5 * 120, window=b4l)

# right direction

b0r = tk.Button(window, text=">", command=partial(move, "0R"))
canvas.create_window(750, 50 + 1 * 120, window=b0r)

b1r = tk.Button(window, text=">", command=partial(move, "1R"))
canvas.create_window(750, 50 + 2 * 120, window=b1r)

b2r = tk.Button(window, text=">", command=partial(move, "2R"))
canvas.create_window(750, 50 + 3 * 120, window=b2r)

b3r = tk.Button(window, text=">", command=partial(move, "3R"))
canvas.create_window(750, 50 + 4 * 120, window=b3r)

b4r = tk.Button(window, text=">", command=partial(move, "4R"))
canvas.create_window(750, 50 + 5 * 120, window=b4r)

bdone = tk.Button(window, text="Check", command=checkGrid)
window.mainloop()
