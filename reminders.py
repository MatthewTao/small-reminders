"""
Contains class to set reminders
"""
import time


class Reminders:
    def __init__(self):
        """
        Init Reminders
        """
        self.last_drink = time.time()
        self.last_moved = time.time()

        self.drink_threshold = 3 * 60 * 60
        self.move_threshold = 2 * 60 * 60

    def take_drink(self):
        self.last_drink = time.time()

    def move_about(self):
        self.last_moved = time.time()

    def _drink_due(self, time_since):
        return time_since > self.drink_threshold

    def _move_due(self, time_since):
        return time_since > self.move_threshold

    def check_action_due(self):
        time_since_drink = time.time() - self.last_drink
        time_since_move = time.time() - self.last_moved
        return {
            "time_since_drink": str(round(time_since_drink/60/60,1)).rjust(4, ' '),
            "drink_due": self._drink_due(time_since_drink),
            "time_since_move": str(round(time_since_move/60/60,1)).rjust(4, ' '),
            "move_due": self._move_due(time_since_move)
        }


