import unittest
from command import CommandProcessor

class TestCommandProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = CommandProcessor()

    def test_place(self):
        result = self.processor.process("PLACE 0,0,NORTH")
        self.assertIsNone(result)
        self.assertEqual(self.processor.robot.report(), "0,0,NORTH")

    def test_move(self):
        self.processor.process("PLACE 0,0,NORTH")
        self.processor.process("MOVE")
        self.assertEqual(self.processor.robot.report(), "0,1,NORTH")

    def test_left(self):
        self.processor.process("PLACE 0,0,NORTH")
        self.processor.process("LEFT")
        self.assertEqual(self.processor.robot.report(), "0,0,WEST")

    def test_right(self):
        self.processor.process("PLACE 0,0,NORTH")
        self.processor.process("RIGHT")
        self.assertEqual(self.processor.robot.report(), "0,0,EAST")

    def test_report(self):
        self.processor.process("PLACE 0,0,NORTH")
        result = self.processor.process("REPORT")
        self.assertEqual(result, "0,0,NORTH")

    def test_invalid_place(self):
        with self.assertRaises(ValueError):
            self.processor.process("PLACE 5,5,NORTH")

    def test_invalid_command(self):
        with self.assertRaises(ValueError):
            self.processor.process("INVALID")

if __name__ == "__main__":
    unittest.main()
