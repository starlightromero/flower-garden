"""Import Turtle Graphics and Plant."""
import turtle as jerry
from Plant import Plant


class Bush(Plant):
    """Class to make a bush which inherits from Plant."""

    def draw(self):
        """Draw Bush."""
        self._goto()
        jerry.pencolor(self._color)
        jerry.pensize(self._size)

        for _ in range(10):
            jerry.forward(self._size * 4)
            jerry.backward(self._size * 4)
            jerry.left(20)

        jerry.left(160)
