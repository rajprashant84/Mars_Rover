from robot import Robot
from table_dimensions import TableDimensions

class CommandProcessor:
    def __init__(self):
        self.robot = Robot()
        self.table = TableDimensions()

    def process(self, command):
        """Process a single command and return the result if applicable."""
        try:
            if command.startswith("PLACE"):
                parts = command.split()
                if len(parts) != 2:
                    raise ValueError("Invalid PLACE command format.")
                params = parts[1].split(",")
                if len(params) != 3:
                    raise ValueError("Invalid PLACE command parameters.")
                x, y, facing = params
                x, y = int(x), int(y)
                if self.table.is_on_table(x, y):
                    self.robot.place(x, y, facing)
                else:
                    raise ValueError(f"PLACE command parameters out of dimesnsion bounds.")
            elif command == "MOVE":
                if self.robot.x is None or self.robot.y is None:
                    raise ValueError("MOVE command cannot be executed before PLACE command.")
                self.robot.move()
            elif command == "LEFT":
                if self.robot.x is None or self.robot.y is None:
                    raise ValueError("LEFT command cannot be executed before PLACE command.")
                self.robot.left()
            elif command == "RIGHT":
                if self.robot.x is None or self.robot.y is None:
                    raise ValueError("RIGHT command cannot be executed before PLACE command.")
                self.robot.right()
            elif command == "REPORT":
                if self.robot.x is None or self.robot.y is None:
                    raise ValueError("REPORT command cannot be executed before PLACE command.")
                return self.robot.report()
            else:
                raise ValueError("Invalid command.")
        except (ValueError, IndexError) as e:
            print(f"Error processing command '{command}': {e}")
        return None
