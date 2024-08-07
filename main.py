from graphics.window import Window
from graphics.shapes.point import Point
from graphics.shapes.line import Line
from graphics.shapes.cell import Cell
from graphics.maze import Maze


def main():
    win = Window(800, 600)

    maze = Maze(50, 50, 20, 28, 25, 25, win=win)

    maze.solve()

    win.wait_for_close()


main()
