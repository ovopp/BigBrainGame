import random
import tkinter as tk

window = tk.Tk()

game_arr = []
array = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]
random.shuffle(array)

for i in range(5):
    tmp_arr = []
    for j in range(5):
        tmp_arr.append(array[5 * i + j])
    game_arr.append(tmp_arr)


def printGameBoard(array):
    for item in array:
        print(item)


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


image_list = [
    tk.PhotoImage(file='colors/red.png'),
    tk.PhotoImage(file='colors/green.png'),
    tk.PhotoImage(file='colors/blue.png'),
    tk.PhotoImage(file='colors/yellow.png'),
    tk.PhotoImage(file='colors/orange.png'),
]

printGameBoard(game_arr)

print("after")
move("1U")
move("2U")
printGameBoard(game_arr)
window.geometry("1000x1000")

canvas = tk.Canvas(window, width=800, height=800, bg='white')
canvas.pack()


def drawGrid():
    global game_arr
    for i in range(5):
        for j in range(5):
            image = image_list[game_arr[i][j] - 1]
            canvas.create_image(80 + j * 160, 80 + i * 160, image=image)


drawGrid()


def moveDown2D():
    move("2D")
    drawGrid()


b = tk.Button(window, text="OK", command=moveDown2D)
b.pack()
window.mainloop()
