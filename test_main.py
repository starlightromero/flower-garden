"""Import unittest, main, and Flower."""
import unittest
from Flower import Flower


class TestMain(unittest.TestCase):
    """Unit tests for flower garden."""

    def test_flower(self):
        """Test _get_turn_degrees method in the Flower class."""
        flower = Flower(0, 0, 20, "blue")
        self.assertEqual(flower._get_turn_degrees(), 18)


unittest.main()
