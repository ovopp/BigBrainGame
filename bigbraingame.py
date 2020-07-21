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

def move():
    global game_arr
    game_arr[0].insert(0,game_arr[0][4])
    game_arr[0].pop(5)

printGameBoard(game_arr)



print("after")
move()
printGameBoard(game_arr)


