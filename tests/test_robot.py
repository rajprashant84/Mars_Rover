import unittest
from robot import Robot

class TestRobot(unittest.TestCase):
    def setUp(self):
        self.robot = Robot()

    def test_place_valid(self):
        self.robot.place(0, 0, "NORTH")
        self.assertEqual(self.robot.report(), "0,0,NORTH")

    def test_place_invalid(self):
        with self.assertRaises(ValueError):
            self.robot.place(5, 5, "NORTH")
        with self.assertRaises(ValueError):
            self.robot.place(0, 0, "INVALID_DIRECTION")

    def test_move(self):
        self.robot.place(0, 0, "NORTH")
        self.robot.move()
        self.assertEqual(self.robot.report(), "0,1,NORTH")

    def test_left(self):
        self.robot.place(0, 0, "NORTH")
        self.robot.left()
        self.assertEqual(self.robot.report(), "0,0,WEST")

    def test_right(self):
        self.robot.place(0, 0, "NORTH")
        self.robot.right()
        self.assertEqual(self.robot.report(), "0,0,EAST")

if __name__ == "__main__":
    unittest.main()
