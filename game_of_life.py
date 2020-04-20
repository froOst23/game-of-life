from tkinter import *
from random import *
import time

# Параметр определяющий живую клетку
live_tag = ('live', '1')
# Задаем размер приложению
app_width = 600
app_height = 600
# Размер клетки
cell_size = 23
# Создаем список, в котором будут хранится клетки
cell_matrix = []
# Для дополнительных вычислений будем определять стороны поля
cube_width = 0
cube_height = 0
# Определяем цвет клеток
die_cell = '#000000'
new_cell = '#ADFF2F'
old_cell = '#2E8B57'


def draw_init_cell():
    # Рисуем клетки в случайном порядке
    for i in range(len(cell_matrix) // 4):
        square = randint(cell_matrix[0], cell_matrix[-2])
        canvas.itemconfig(square, fill=new_cell, tag=('live', '1'))


def check_neighbors():
    # Переменная для определения живой клетки
    live_tag = ('live', '1')
    square = 1
    # i начинает отсчет с 0
    for i in range(cube_height+1):
        if i == 0:
            pass
        else:
            # j начинает отсчет с 0
            for j in range(cube_height+1):
                if j == 0:
                    pass
                else:
                    count_neighbors = 0
                    # Проверяем статус соседних клеток по вертикале
                    square_number = (i - 1) * cube_height + j + 1
                    square = square_number
                    if cube_height >= j + 1 > 0 and canvas.gettags(square) == live_tag:
                        count_neighbors += 1
                    # Проверяем статус соседних клеток по вертикале
                    square_number = (i - 1) * cube_height + j - 1
                    square = square_number
                    if cube_height >= j - 1 > 0 and canvas.gettags(square) == live_tag:
                        count_neighbors += 1
                    # Проверяем статус соседних клеток по горизонтале
                    square_number = ((i - 1) - 1) * cube_height + j
                    square = square_number
                    if cube_height >= i - 1 > 0 and canvas.gettags(square) == live_tag:
                        count_neighbors += 1
                    # Проверяем статус соседних клеток по горизонтале
                    square_number = ((i - 1) + 1) * cube_height + j
                    square = square_number
                    if cube_height >= i + 1 > 0 and canvas.gettags(square) == live_tag:
                        count_neighbors += 1
                    # Проверяем статус соседних клеток по диагонале
                    square_number = ((i - 1) + 1) * cube_height + j + 1
                    square = square_number
                    if cube_height >= i + 1 > 0 and cube_height >= j + 1 > 0 and \
                            canvas.gettags(square) == live_tag:
                        count_neighbors += 1
                    # Проверяем статус соседних клеток по диагонале
                    square_number = ((i - 1) - 1) * cube_height + j - 1
                    square = square_number
                    if cube_height >= i - 1 > 0 and cube_height >= j - 1 > 0 and \
                            canvas.gettags(square) == live_tag:
                        count_neighbors += 1
                    # Проверяем статус соседних клеток по диагонале
                    square_number = ((i - 1) - 1) * cube_height + j + 1
                    square = square_number
                    if cube_height >= i - 1 > 0 and cube_height >= j + 1 > 0 and \
                            canvas.gettags(square) == live_tag:
                        count_neighbors += 1
                    # Проверяем статус соседних клеток по диагонале
                    square_number = ((i - 1) + 1) * cube_height + j - 1
                    square = square_number
                    if cube_height >= i + 1 > 0 and cube_height >= j - 1 > 0 and \
                            canvas.gettags(square) == live_tag:
                        count_neighbors += 1
                    # Определяем судьбу текущей клетки
                    square = (i - 1) * cube_height + j
                    if canvas.gettags(square) != live_tag:
                        if count_neighbors == 3:
                            canvas.itemconfig(square, fill=new_cell, tag=('live', '1'))
                    else:
                        if count_neighbors == 3 or count_neighbors == 2:
                            canvas.itemconfig(square, fill=old_cell, tag=('live', '1'))
                        if count_neighbors > 3 or count_neighbors < 2:
                            canvas.itemconfig(square, fill=die_cell, tag=('die', '0'))


def game():
    # Текущий жизненный цикл
    life_cycle = 0
    while TRUE:
        life_cycle += 1
        check_neighbors()
        root.update()
        time.sleep(0.08)
        root.title('Life cycle = ' + str(life_cycle))


root = Tk()
# Выводим на центр экрана
sys_width = root.winfo_screenwidth()
sys_height = root.winfo_screenheight()
sys_width = sys_width // 2
sys_height = sys_height // 2
sys_width = sys_width - (app_width / 2)
sys_height = sys_height - (app_height / 2)
root.resizable(False, False)
# Задаем конфигурацию root.geometry формата WxH+W+H
config_geometry = str(app_width) + 'x' + str(app_height) \
                  + '+' + str(int(sys_width)) \
                  + '+' + str(int(sys_height))
root.geometry(config_geometry)
# Создаем область прорисовки
field_width = app_width / cell_size
field_height = app_height / cell_size
canvas = Canvas(root, width=app_width, height=app_height)
canvas.pack(fill=BOTH)
# Заполняем поле клетками
state_cell = dict()
for i in range(int(field_height)):
    cube_height += 1
    for j in range(int(field_width)):
        cube_width += 1
        square = canvas.create_rectangle(cell_size * j,
                                         cell_size * i,
                                         cell_size + cell_size * j,
                                         cell_size + cell_size * i, )
        canvas.itemconfig(square, fill=die_cell, tag=('die', '0'))
        cell_matrix.append(square)
print(cell_matrix)
# Рисуем первоночальные клетки
draw_init_cell()
# Запускаем наш клеточный автомат
game()
root.mainloop()
