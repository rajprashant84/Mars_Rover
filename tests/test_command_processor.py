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
        result = self.processor.process("PLACE 5,5,NORTH")
        self.assertEqual(result, "Error processing command 'PLACE 5,5,NORTH': PLACE command parameters out of dimensions bounds.")

    def test_invalid_command(self):
        result = self.processor.process("INVALID")
        self.assertEqual(result, "Error processing command 'INVALID': Invalid command.")

if __name__ == "__main__":
    unittest.main()
