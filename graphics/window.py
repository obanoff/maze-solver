from tkinter import Tk, BOTH, Canvas
from graphics.shapes.line import Line
from graphics.shapes.point import Point


class Window:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.__root_widget = Tk()
        self.__root_widget.title("Maze Solver")
        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(
            self.__root_widget, bg="white", height=height, width=width
        )
        self.__canvas.pack(fill=BOTH, expand=1)

        self.__running = False

    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.__canvas, fill_color)

    def redraw(self):
        self.__root_widget.update_idletasks()
        self.__root_widget.update()

    def wait_for_close(self):
        self.__running = True

        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False
