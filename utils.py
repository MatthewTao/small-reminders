"""
Standard functions that benefit across areas
"""
import configparser
import ctypes


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


def lock_screen():
    ctypes.windll.user32.LockWorkStation()


def str_to_bool(bool_str):
    valid = {'true': True, 't': True, '1': True,
             'false': False, 'f': False, '0': False,
             }   

    if isinstance(bool_str, bool):
        return bool_str

    if not isinstance(bool_str, str):
        raise ValueError('invalid literal for boolean. Not a string.')

    lower_value = bool_str.lower()
    if lower_value in valid:
        return valid[lower_value]
    else:
        raise ValueError(f'invalid literal for boolean: "{bool_str}"')
