from graphics.window import Window
from graphics.shapes.point import Point
from graphics.shapes.line import Line
from graphics.shapes.cell import Cell
from graphics.maze import Maze


def main():
    win = Window(800, 600)

    maze = Maze(50, 50, 10, 14, 50, 50, win)

    win.wait_for_close()


main()
