from tkinter import Canvas

from graphics.window import Window
from graphics.shapes.point import Point
from graphics.shapes.line import Line


class Cell:
    def __init__(
        self,
        point1: Point,
        point2: Point,
        win: Window,
        has_left=True,
        has_right=True,
        has_top=True,
        has_bottom=True,
    ):
        self.has_left = has_left
        self.has_right = has_right
        self.has_top = has_top
        self.has_bottom = has_bottom
        self.__point1 = point1
        self.__point2 = point2
        self.__win = win

    def draw(self, fill_color: str):
        walls = []

        if self.has_top:
            line = Line(
                Point(self.__point1.x, self.__point1.y),
                Point(self.__point2.x, self.__point1.y),
            )
            walls.append(line)

        if self.has_right:
            line = Line(
                Point(self.__point2.x, self.__point1.y),
                Point(self.__point2.x, self.__point2.y),
            )
            walls.append(line)

        if self.has_bottom:
            line = Line(
                Point(self.__point1.x, self.__point2.y),
                Point(self.__point2.x, self.__point2.y),
            )
            walls.append(line)

        if self.has_left:
            line = Line(
                Point(self.__point1.x, self.__point1.y),
                Point(self.__point1.x, self.__point2.y),
            )
            walls.append(line)

        for wall in walls:
            self.__win.draw_line(wall, fill_color)

    def draw_move(self, to_cell: "Cell", undo=False):
        center1_x = (self.__point2.x - self.__point1.x) / 2 + self.__point1.x
        center1_y = (self.__point2.y - self.__point1.y) / 2 + self.__point1.y

        center2_x = (to_cell.__point2.x - to_cell.__point1.x) / 2 + to_cell.__point1.x
        center2_y = (to_cell.__point2.y - to_cell.__point1.y) / 2 + to_cell.__point1.y
        line = Line(Point(center1_x, center1_y), Point(center2_x, center2_y))

        if undo:
            self.__win.draw_line(line, "gray")
        else:
            self.__win.draw_line(line, "red")
