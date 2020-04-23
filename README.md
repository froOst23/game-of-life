# Conway's Game of Life

![](https://img.shields.io/github/languages/top/froOst23/game_of_life.svg)
![](https://img.shields.io/github/last-commit/froOst23/game_of_life.svg)
![](https://img.shields.io/github/repo-size/froOst23/game_of_life.svg)

### Description

The Game of Life, also known simply as Life, is a cellular automaton devised by the [British mathematician John Horton Conway](https://en.wikipedia.org/wiki/John_Horton_Conway) in 1970.

The graphical interface is implemented using the tkinter module.

### Classic game rules

In this version there is a slight deviation from the classic version of the game. Implemented the method of cell aging, which is described in this part:

```
def hex_color(color):
    color = int(color[1:7:1], 16)
    if color >= 20000:
        color = color - 2560
        color = hex(color)
        color = str(color[2:8:1])
        color = '#00' + color
        return color
    else:
        color = '#000000'
        return color
```

For classic rules, it’s enough to remove one condition in the fate() function:

```
hex_color(color_matrix[index]) == '#000000':
```
