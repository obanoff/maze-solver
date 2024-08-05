import unittest

from graphics.maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(
            0,
            0,
            num_rows,
            num_cols,
            10,
            10,
        )

        self.assertEqual(len(m1.cells), num_cols)
        self.assertEqual(len(m1.cells[0]), num_rows)

    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(
            0,
            0,
            num_rows,
            num_cols,
            10,
            10,
        )

        for column in m1.cells:
            for cell in column:
                self.assertEqual(False, cell._visited)


if __name__ == "__main__":
    unittest.main()
