from os import system
from time import perf_counter
from typing import Callable


def int2hex(value: int) -> str:
    return hex(value).upper().replace("X", "x")

def instantiation(cls):
    return cls()


def _loggerSetup():
    from logging import getLogger, StreamHandler, Formatter, INFO, WARNING, ERROR, DEBUG

    class ColoredFormatter(Formatter):
        def format(self, record):
            record.levelname = {
                DEBUG: f'\033[95m[{record.levelname}]\033[0m',
                INFO: f'\033[92m[{record.levelname}]\033[0m',
                WARNING: f'\033[93m[{record.levelname}]\033[0m',
                ERROR: f'\033[91m[{record.levelname}]\033[0m',
            }.get(record.levelno, record.levelname)

            return super().format(record)

    handler = StreamHandler()
    handler.setFormatter(ColoredFormatter(" ".join((
        "%(levelname)s",
        "\033[1;32m[%(asctime)s]\033[0m",
        # "\033[1;35m[%(filename)s:%(lineno)s]\033[0m",
        "\033[1;35m[%(filename)s]\033[0m",
        "\033[1;97m%(message)s\033[0m",
    ))))

    logger = getLogger(None)
    logger.addHandler(handler)
    logger.setLevel(DEBUG)
    return logger

logger = _loggerSetup()


def timeUseInfo(func: Callable):
    def wrapper(*args, **kwargs):
        funcName = "%s:%s" % (
            func.__code__.co_filename.split("\\")[-1],
            func.__name__,
        )
        logger.info("Dumper: %s Run" % funcName)

        timeUseCounter = perf_counter()
        result = func(*args, **kwargs)
        timeUse = (perf_counter() - timeUseCounter) * 1000

        logger.info("Dumper: %s Finished in %s ms" % (
            funcName,
            timeUse
        ))
        return result

    return wrapper

def errorButDontCloseWindow(func: Callable):
    def wrapper(*args, **kwargs):
        try: return func(*args, **kwargs)
        except Exception:
            system("pause.")
            exit()
    return wrapper
