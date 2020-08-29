"""Import Turtle Graphics and Plant."""
import turtle as jerry
from Plant import Plant


class Flower(Plant):
    """Class to make a flower which inherits from Plant."""

    def __init__(self, x, y, size, color):
        """Initialize Flower and parent Plant."""
        super().__init__(x, y, size, color)
        self._num_petals = size
        self._petal_length = size * 4

    def _get_turn_degrees(self):
        return 360 / self._num_petals

    def draw(self):
        """Draw Flower."""
        self._goto()
        jerry.pencolor(self._color)
        jerry.pensize(self._size)

        for _ in range(self._num_petals):
            jerry.forward(self._petal_length)
            jerry.backward(self._petal_length)
            jerry.right(self._get_turn_degrees())

        jerry.pencolor("orange")
        jerry.dot(self._size * 2)
