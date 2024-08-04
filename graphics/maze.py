from typing import List
from time import sleep

from graphics.window import Window
from graphics.shapes.cell import Cell
from graphics.shapes.point import Point


class Maze:
    def __init__(
        self,
        x1: float,
        y1: float,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

        self.__cells: List[List[Cell]] = []

        self.__create_cells()

    def __create_cells(self):
        if self.__cell_size_x * self.__num_cols + self.__x1 > self.__win.width:
            raise Exception("window cannot contain the number of columns")

        if self.__cell_size_y * self.__num_rows + self.__y1 > self.__win.height:
            raise Exception("window cannot contain the number of rows")

        for i in range(self.__num_cols):
            column = [self.__draw_cell(i, j) for j in range(self.__num_rows)]
            self.__cells.append(column)

    def __draw_cell(self, i, j):
        point1 = Point(
            self.__x1 + self.__cell_size_x * i,
            self.__y1 + self.__cell_size_y * j,
        )

        point2 = Point(
            point1.x + self.__cell_size_x,
            point1.y + self.__cell_size_y,
        )

        cell = Cell(point1, point2, self.__win)

        cell.draw("blue")

        self.__animate()

        return cell

    def __animate(self):
        self.__win.redraw()
        sleep(0.05)
