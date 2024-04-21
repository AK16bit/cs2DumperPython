from os import mkdir
from os.path import exists
from time import sleep, perf_counter

from CS2 import CS2Process, isCS2ProcessExist, isCS2ProcessReady
from utils import logger, ASCII_BASAGANNIDARR_MEDIUM, ASCII_AK32767_SMALL


def main(signature: bool = True, schema: bool = True, convar: bool = True) -> None:
    while not isCS2ProcessExist(): sleep(0.1)
    while not isCS2ProcessReady(): sleep(0.5)

    cs2 = CS2Process()
    timeUseCounter = perf_counter()

    if signature:
        from Dumper.SignatureDump import dumpSignature
        dumpSignature()
    if schema:
        from Dumper.SchemaDump import dumpSchema
        dumpSchema()
    if convar:
        from Dumper.ConvarDump import dumpConvar
        dumpConvar()

    timeUse = (perf_counter() - timeUseCounter) * 1000
    logger.info("All Dump Finished in %s ms" % timeUse)


if __name__ == '__main__':
    [logger.info(strLine) for strLine in ASCII_BASAGANNIDARR_MEDIUM.split("\n")]
    # [logger.info(strLine) for strLine in ASCII_AK32767_SMALL.split("\n")]

    main(True, True, False)
    