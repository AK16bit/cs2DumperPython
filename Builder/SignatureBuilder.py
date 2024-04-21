from json import dumps
from os import mkdir
from os.path import exists, split, join
from typing import Sequence

from Signature.Container import ContainerModule


def signatureBuilder(modulesCtr: Sequence[ContainerModule]) -> None:
    outputLocation = "Output\\Signature"
    if not exists(split(outputLocation)[0]): mkdir(split(outputLocation)[0])
    if not exists(outputLocation): mkdir(outputLocation)

    for moduleCtr in modulesCtr:
        moduleName = moduleCtr.get("name")

        moduleDict = {
            signature.get("name"): signature.get("value")
            for signature in moduleCtr.get("signatures")
        }
        moduleJson = dumps(moduleDict, indent=4)

        with open(join(outputLocation, "%s.json" % moduleName), "w") as moduleFile:
            moduleFile.write(moduleJson)