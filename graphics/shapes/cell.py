from graphics.window import Window
from graphics.shapes.point import Point
from graphics.shapes.line import Line


class Cell:
    def __init__(
        self,
        point1: Point,
        point2: Point,
        win: None | Window = None,  # default: None - for testing purposes
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
        self._visited = False

        self.__win = win

        self._line_ids = {}

    def draw(self, fill_color: str):
        walls = {}

        if self.has_top:
            line = Line(
                Point(self.__point1.x, self.__point1.y),
                Point(self.__point2.x, self.__point1.y),
            )
            walls["top"] = line

        if self.has_right:
            line = Line(
                Point(self.__point2.x, self.__point1.y),
                Point(self.__point2.x, self.__point2.y),
            )
            walls["right"] = line

        if self.has_bottom:
            line = Line(
                Point(self.__point1.x, self.__point2.y),
                Point(self.__point2.x, self.__point2.y),
            )
            walls["bottom"] = line

        if self.has_left:
            line = Line(
                Point(self.__point1.x, self.__point1.y),
                Point(self.__point1.x, self.__point2.y),
            )
            walls["left"] = line

        # for testing purposes
        if type(self.__win) == Window:
            for key in walls:
                self._line_ids[key] = self.__win.draw_line(walls[key], fill_color)

    def redraw(self, fill_color: str):
        # for testing purposes
        if self.__win is None:
            return

        if not self.has_top and self._line_ids["top"]:
            self.__win._canvas.delete(self._line_ids["top"])
            del self._line_ids["top"]

        if not self.has_right and self._line_ids["right"]:
            self.__win._canvas.delete(self._line_ids["right"])
            del self._line_ids["right"]

        if not self.has_bottom and self._line_ids["bottom"]:
            self.__win._canvas.delete(self._line_ids["bottom"])
            del self._line_ids["bottom"]

        if not self.has_left and self._line_ids["left"]:
            self.__win._canvas.delete(self._line_ids["left"])
            del self._line_ids["left"]

        self.draw(fill_color)

    def draw_move(self, to_cell: "Cell", undo=False):
        if type(self.__win) != Window:
            raise Exception("Window object not provided")

        center1_x = (self.__point2.x - self.__point1.x) / 2 + self.__point1.x
        center1_y = (self.__point2.y - self.__point1.y) / 2 + self.__point1.y

        center2_x = (to_cell.__point2.x - to_cell.__point1.x) / 2 + to_cell.__point1.x
        center2_y = (to_cell.__point2.y - to_cell.__point1.y) / 2 + to_cell.__point1.y
        line = Line(Point(center1_x, center1_y), Point(center2_x, center2_y))

        if undo:
            self.__win.draw_line(line, "gray")
        else:
            self.__win.draw_line(line, "red")
