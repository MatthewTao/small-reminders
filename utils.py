"""
Standard functions that benefit across areas
"""
import configparser


def minutes_to_milliseconds(time_in_minutes):
    return time_in_minutes * 60 * 1000


def hours_to_seconds(time_in_hours):
    return time_in_hours * 60 * 60


def seconds_to_hours(time_in_secs):
    return time_in_secs / 60 / 60


def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config
