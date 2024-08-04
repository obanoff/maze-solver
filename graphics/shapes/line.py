from graphics.shapes.point import Point
from tkinter import Canvas


class Line:
    def __init__(self, point_one: Point, point_two: Point):
        self.__point_one = point_one
        self.__point_two = point_two

    def draw(self, canvas: Canvas, fill_color: str):
        id = canvas.create_line(
            self.__point_one.x,
            self.__point_one.y,
            self.__point_two.x,
            self.__point_two.y,
            fill=fill_color,
            width=2,
        )

        return id
