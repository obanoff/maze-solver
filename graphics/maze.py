from typing import List
from time import sleep
import random

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
        win: Window | None = None,
        seed: int | None = None,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

        random.seed(seed)

        self.__cells: List[List[Cell]] = []

        self.__create_cells()

        self.__break_walls_r(0, 0)

        self.__reset_cells_visited()

    def __create_cells(self):
        # for testing purposes
        if type(self.__win) == Window:
            if self.__cell_size_x * self.__num_cols + self.__x1 > self.__win.width:
                raise Exception("window cannot contain the number of columns")

            if self.__cell_size_y * self.__num_rows + self.__y1 > self.__win.height:
                raise Exception("window cannot contain the number of rows")

        for i in range(self.__num_cols):
            column = [self.__draw_cell(i, j) for j in range(self.__num_rows)]
            self.__cells.append(column)

        self.__break_entrance_and_exit()

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

        cell.draw("black")

        self.__animate(0.00001)

        return cell

    def __animate(self, sec: float):
        # for testing purposes
        if type(self.__win) != Window:
            return

        self.__win.redraw()
        sleep(sec)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top = False
        self.__cells[-1][-1].has_bottom = False

        if type(self.__win) == Window:
            id1 = self.__cells[0][0]._line_ids["top"]
            id2 = self.__cells[-1][-1]._line_ids["bottom"]
            self.__win._canvas.delete(id1)
            self.__win._canvas.delete(id2)

            del self.__cells[0][0]._line_ids["top"]
            del self.__cells[-1][-1]._line_ids["bottom"]

    def __break_walls_r(self, i, j):
        current: Cell = self.__cells[i][j]
        current._visited = True

        while True:
            directions = self.__get_directions(i, j)

            if len(directions) == 0:
                current.draw("black")
                return

            move_to = random.choice(directions)
            move_to_cell: Cell = self.__cells[move_to[0]][move_to[1]]

            # same column
            if move_to[0] == i:
                # above
                if move_to[1] > j:
                    current.has_bottom = False
                    move_to_cell.has_top = False
                # beneath
                else:
                    current.has_top = False
                    move_to_cell.has_bottom = False

            # same row
            if move_to[1] == j:
                # left
                if move_to[0] > i:
                    current.has_right = False
                    move_to_cell.has_left = False
                # right
                else:
                    current.has_left = False
                    move_to_cell.has_right = False

            current.draw("black")
            move_to_cell.draw("black")

            self.__animate(0.01)

            self.__break_walls_r(*move_to)

    def __reset_cells_visited(self):
        for column in self.__cells:
            for cell in column:
                cell._visited = False

    def solve(self):
        return self.__solve_r()

    def __solve_r(self, i=0, j=0):
        self.__animate(0.06)

        current = self.__cells[i][j]

        current._visited = True

        if i == len(self.__cells) - 1 and j == len(self.__cells[i]) - 1:
            return True

        directions = self.__get_directions(i, j)

        for d in directions:
            move_to_cell = self.__cells[d[0]][d[1]]

            if move_to_cell._visited:
                continue

            # same column
            if i == d[0]:
                # beneath
                if j < d[1]:
                    if current.has_bottom == False and move_to_cell.has_top == False:
                        current.draw_move(move_to_cell)

                        if self.__solve_r(*d):
                            return True
                        else:
                            current.draw_move(move_to_cell, undo=True)
                # above
                else:
                    if current.has_top == False and move_to_cell.has_bottom == False:
                        current.draw_move(move_to_cell)

                        if self.__solve_r(*d):
                            return True
                        else:
                            current.draw_move(move_to_cell, undo=True)

            # same row
            if j == d[1]:
                # right
                if i < d[0]:
                    if current.has_right == False and move_to_cell.has_left == False:
                        current.draw_move(move_to_cell)

                        if self.__solve_r(*d):
                            return True
                        else:
                            current.draw_move(move_to_cell, undo=True)

                # left
                else:
                    if current.has_left == False and move_to_cell.has_right == False:
                        current.draw_move(move_to_cell)

                        if self.__solve_r(*d):
                            return True
                        else:
                            current.draw_move(move_to_cell, undo=True)

        return False

    def __get_directions(self, i: int, j: int):
        directions = []

        if i + 1 < len(self.__cells) and not self.__cells[i + 1][j]._visited:
            directions.append((i + 1, j))

        if j + 1 < len(self.__cells[0]) and not self.__cells[i][j + 1]._visited:
            directions.append((i, j + 1))

        if i - 1 >= 0 and not self.__cells[i - 1][j]._visited:
            directions.append((i - 1, j))

        if j - 1 >= 0 and not self.__cells[i][j - 1]._visited:
            directions.append((i, j - 1))

        return directions

    # for testing purposes
    @property
    def cells(self):
        return self.__cells
