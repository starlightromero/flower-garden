"""Import Turtle Graphics."""
import turtle as jerry


class Plant:
    """Class to make Plant."""

    def __init__(self, x, y, size, color):
        """Initialize Plant."""
        self._x = x
        self._y = y
        self._size = size
        self._color = color

    def _goto(self):
        jerry.penup()
        jerry.goto(self._x, self._y)
        jerry.pendown()
