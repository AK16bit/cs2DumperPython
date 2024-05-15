from ctypes import windll
from logging import info, error, debug
from os import system
from platform import system as system_name
from time import sleep, perf_counter

from CS2 import CS2Process, isCS2ProcessExist, isCS2ProcessReady
from utils import ASCII_BASAGANNIDARR_MEDIUM, loggerSetup


def main(signature: bool = True, schema: bool = True, convar: bool = False) -> None:
    if not system_name() == "Windows":
        error("No Support For Non-Windows Systems.")
        system("pause")
        exit()

    if not windll.shell32.IsUserAnAdmin():
        error("Please Run As Administrator.")
        system("pause")
        exit()

    if not isCS2ProcessExist():
        info("Wait For Counter-Strike 2 Process...")
        while not isCS2ProcessExist(): sleep(0.1)
    if not isCS2ProcessReady():
        info("Wait For Counter-Strike 2 Initialization Complete...")
        while not isCS2ProcessReady(): sleep(0.5)

    cs2 = CS2Process()
    info("Counter-Strike 2 Found.")
    debug("Process ID: %s" % cs2.pid)
    debug("Process Handle: %s" % cs2.handle)
    timeUseCounter = perf_counter()

    if signature:
        from Dumper.SignatureDump import dumpSignature
        dumpSignature()
    if schema:
        from Dumper.SchemaDump import dumpSchema
        dumpSchema()
    if convar:
        # Actually, convarDump is meaningless, but I still coded it I dunno why :P
        from Dumper.ConvarDump import dumpConvar
        dumpConvar()

    timeUse = (perf_counter() - timeUseCounter) * 1000
    info("All Dump Finished in %s ms" % timeUse)

    system("pause.")


if __name__ == '__main__':
    loggerSetup()
    [info(strLine) for strLine in ASCII_BASAGANNIDARR_MEDIUM.split("\n")]
    # [logger.info(strLine) for strLine in ASCII_AK32767_SMALL.split("\n")]

    main(True, True)
    