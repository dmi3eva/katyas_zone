from tkinter import *
from tkinter import Label


def flea_a(step):
  pass


def flea_b(step):
  return 0, step, "Катя"


def flea_c(step):
  return step, step, "Ира"


def flea_d(step):
  return 6-step, step, "Маша"


def flea_e(step):
  return 2, 2, "Анастасия"


def flea_f(step):
  return 6-step, 0, "Виссарион"


def flea_g(step):
  return 6-step, 0, "Александр"


def flea_h(step):
  return 6-step, 0, "Михаил"


def flea_i(step):
  return 6-step, 0, "Димас"


def flea_j(step):
  return 6-step, 0, "Гераклида"


def flea_k(step):
  return 6-step, 0, "Афанасий"


def flea_l(step):
  return 6-step, 0, "Лиссабон"


fleas_functions = [flea_a, flea_b, flea_c, flea_d, flea_e, flea_f, flea_g, flea_h, flea_i, flea_j, flea_k, flea_l]


def clear_all():
  for i in range(TABLE_SIZE):
    for j in range(TABLE_SIZE):
      color = 'white' if (i + j) % 2 else 'gray'
      label = f"({i}, {j})"
      if table[i][j]:
        label = f"({i}, {j})\n Пыль"
      cells[i][j].configure(width=12, height=6, bd=2, bg=color, text=label)
      positions[i][j] = []


def change_scores_label():
  label = ""
  index = 0
  for _name, _score in scores.items():
    current_score = round(_score, 2)
    label += f"{_name}: {current_score}\n"
    index += 1
    if index == len(scores) or index % 4 == 0:
      score_labels[(index - 1) // 4].configure(text=label, justify=LEFT)
      label = ""


def recalculate_scores():
  for i in range(TABLE_SIZE):
    for j in range(TABLE_SIZE):
      for _name in positions[i][j]:
        if table[i][j]:
          scores[_name] = scores.get(_name, 0) + 1. / len(positions[i][j])
      if len(positions[i][j]) > 0:
        table[i][j] = False
  change_scores_label()


def change_labels():
  for i in range(TABLE_SIZE):
    for j in range(TABLE_SIZE):
      label = f""
      if table[i][j]:
        label = f"({i}, {j})\n Пыль"
      else:
        label += ', '.join(positions[i][j])
      cells[i][j].configure(text=label)


def make_one_step():
  for _flea in fleas_functions:
    try:
      x, y, name = _flea(step)
      cells[x][y].configure(background='#ffdfc4')
      positions[x][y].append(name)
    except:
      print("Error")


def make_all_steps():
  global step
  step += 1
  step_label.configure(text=f"Шаг №{step}")
  clear_all()
  make_one_step()
  recalculate_scores()
  change_labels()


root = Tk()
root.geometry("540x600")
TABLE_SIZE = 6
table = [[True for _ in range(TABLE_SIZE)] for _ in range(TABLE_SIZE)]
cells = [[] for _ in range(TABLE_SIZE)]
scores = {}
positions = [[[] for _ in range(TABLE_SIZE)] for _ in range(TABLE_SIZE)]
step = 0


for i in range(TABLE_SIZE):
  for j in range(TABLE_SIZE):
    color = 'white' if (i + j) % 2 else 'gray'
    label = f"({i}, {j})\n Пыль"
    current_label = Label(root, width=12, height=6, bd=2, bg=color, text=label, wraplength="100")
    current_label.grid(row=i, column=j)
    cells[i].append(current_label)


step_button = Button(root, text="Сделать шаг", width=12, command=make_all_steps)
step_button.grid(row=TABLE_SIZE+1, column=0)

step_label = Label(root, text=f"Шаг №{step}")
step_label.grid(row=TABLE_SIZE+3, column=0)

score_labels = []
for i in range(3):
  current_label = Label(root, text="", justify=LEFT, padx=2)
  current_label.grid(row=i, column=TABLE_SIZE+2)
  score_labels.append(current_label)
mainloop()