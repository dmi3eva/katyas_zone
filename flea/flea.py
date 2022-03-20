from tkinter import *
from tkinter import Label


def flea_a(step):
  pass


def flea_b(step):
  return 0, step, "Катя"


def flea_c(step):
  pass


def flea_d(step):
  pass


def flea_e(step):
  pass


def flea_f(step):
  pass


def flea_g(step):
  pass


def flea_h(step):
  pass


def flea_i(step):
  pass


def flea_j(step):
  pass


def flea_k(step):
  pass


def flea_l(step):
  pass


def make_all_steps():
  step += 1
  fleas_functions = [flea_a, flea_b, flea_c, flea_d, flea_e, flea_f, flea_g, flea_h, flea_i, flea_j, flea_k, flea_l]
  for _flea in fleas_functions:
    step = 1
    try:
      x, y, name = _flea(step)
      cells[x][y].configure(background='black')
    except:
      print("Error")


root = Tk()
root.geometry("450x600")
TABLE_SIZE = 5
table = [[1 for _ in range(TABLE_SIZE)] for _ in range(TABLE_SIZE)]
cells = [[] for _ in range(TABLE_SIZE)]



for i in range(TABLE_SIZE):
  for j in range(TABLE_SIZE):
    color = 'white' if (i + j) % 2 else 'gray'
    label = f"({i}, {j})\n Пыль"
    current_label = Label(root, width=12, height=6, bd=2, bg=color, text=label)
    current_label.grid(row=i, column=j)
    cells[i].append(current_label)


step = 0
step_button = Button(root, text="Сделать шаг", width=12, command=make_all_steps)
step_button.grid(row=TABLE_SIZE+1, column=0)


mainloop()