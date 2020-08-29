"""Import Turtle Graphics and Plant."""
import turtle as jerry
from Plant import Plant


class Tree(Plant):
    """Class to make a flower which inherits from Plant."""

    def __init__(self, x, y, size, color):
        """Initialize Tree and parent Plant."""
        super().__init__(x, y, size, color)
        self._num_branches = size
        self._branch_length = size * 6
        self._trunk_color = "brown"

    def _move(self):
        return self._size * 2

    def draw(self):
        """Draw Tree."""
        self._goto()
        jerry.pencolor(self._trunk_color)
        jerry.pensize(self._size)

        jerry.left(90)
        jerry.forward(self._move() * 3)
        jerry.pencolor(self._color)

        for _ in range(self._num_branches):
            jerry.forward(self._move())
            jerry.left(135)
            jerry.forward(self._branch_length)
            jerry.backward(self._branch_length)
            jerry.left(90)
            jerry.forward(self._branch_length)
            jerry.backward(self._branch_length)
            jerry.left(135)

        jerry.right(90)
