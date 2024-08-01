from graphics.window import Window
from graphics.shapes.point import Point
from graphics.shapes.line import Line
from graphics.shapes.cell import Cell


def main():
    win = Window(800, 600)

    cell_1 = Cell(Point(10, 10), Point(110, 110), win)
    cell_2 = Cell(Point(150, 10), Point(250, 110), win, has_top=False)
    cell_3 = Cell(
        Point(300, 10), Point(400, 110), win, has_right=False, has_bottom=False
    )
    cell_4 = Cell(Point(450, 10), Point(550, 110), win, has_right=False, has_left=False)

    cell_1.draw("green")
    cell_2.draw("blue")
    cell_3.draw("orange")
    cell_4.draw("red")

    win.wait_for_close()


main()
