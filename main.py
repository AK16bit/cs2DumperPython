from time import sleep, perf_counter

from CS2 import CS2Process, isCS2ProcessExist, isCS2ProcessReady
from utils import logger

if __name__ == '__main__':
    while not isCS2ProcessExist(): sleep(0.1)
    while not isCS2ProcessReady(): sleep(0.5)

    cs2 = CS2Process()
    timeUseCounter = perf_counter()

    from Dumper.SignatureDump import dumpSignature
    from Dumper.SchemaDump import dumpSchema
    from Dumper.ConvarDump import dumpConvar
    dumpSignature()
    dumpSchema()
    dumpConvar()

    timeUse = (perf_counter() - timeUseCounter) * 1000
    logger.info("All Dump Finished in %s ms" % timeUse)