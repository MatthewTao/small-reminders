"""
Contains class to set reminders
"""
import time

from utils import read_config, hours_to_seconds, seconds_to_hours


class Reminders:
    def __init__(self):
        """
        Init Reminders
        """
        self.last_drink = time.time()
        self.last_moved = time.time()

        self.config = read_config()
        self.drink_threshold = hours_to_seconds(
            float(self.config['THRESHOLD']['drink']))
        self.move_threshold = hours_to_seconds(
            float(self.config['THRESHOLD']['move']))

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
        since_drink_str = str(
            round(
                seconds_to_hours(
                    time_since_drink
                )
            )
        ).rjust(4, ' ')

        time_since_move = time.time() - self.last_moved
        since_move_str = str(
            round(
                seconds_to_hours(
                    time_since_move
                )
            )
        ).rjust(4, ' ')

        return {
            "time_since_drink": since_drink_str,
            "drink_due": self._drink_due(time_since_drink),
            "time_since_move": since_move_str,
            "move_due": self._move_due(time_since_move)
        }


