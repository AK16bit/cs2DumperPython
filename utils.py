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
        except Exception as error:
            logger.error(error)
            system("pause.")
            exit()
    return wrapper



# Three Point
ASCII_BASAGANNIDARR_SMALL = r"""|~) _  _ _   /~_ _  _  _ .__|~\ _  _ _
|_)(_|_\(_|  \_/(_|| || ||  |_/(_|| | """
ASCII_AK32767_SMALL = r"""|\/| _  _| _   |_      /\ |/ '~)'~)~/ / ~/
|  |(_|(_|(/_  |_)\/  /~~\|\ ._) /_/ (_)/  
                  /"""
# Small Shadow
ASCII_BASAGANNIDARR_MEDIUM = r"""__ )                            ___|                      _)         __ \                     
__ \    _` |   __|   _` |      |       _` |  __ \   __ \   |         |   |   _` |   __|   __| 
|   |  (   | \__ \  (   |      |   |  (   |  |   |  |   |  | _____|  |   |  (   |  |     |    
___/  \__,_| ____/ \__,_|     \____| \__,_| _|  _| _|  _| _|        ____/  \__,_| _|    _|     """
ASCII_MYAAMINOX_MEDIUM = r"""  \  |                            _)            \ \  /
 |\/ |  |  |   _` |   _` |   ` \   |    \    _ \ >  < 
_|  _| \_, | \__,_| \__,_| _|_|_| _| _| _| \___/ _/\_\
       ___/"""