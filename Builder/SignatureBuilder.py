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

        moduleSignatureDict = {
            signature.get("name"): signature.get("value")
            for signature in moduleCtr.get("signatures")
        }
        moduleSignatureJson = dumps(moduleSignatureDict, indent=4)

        with open(join(outputLocation, "%s.json" % moduleName.replace(".", "_")), "w") as moduleSignatureFile:
            moduleSignatureFile.write(moduleSignatureJson)

    configDict = dict()
    for moduleCtr in modulesCtr:
        moduleName = moduleCtr.get("name")

        moduleConfigDict = [
            signatureConfig
            for signature in moduleCtr.get("signatures")
            if (signatureConfig := signature.get("config")) is not None
        ]
        configDict.update({
            moduleName: moduleConfigDict
        })
    configJson = dumps(configDict, indent=4)
    with open(join(outputLocation, "%s.json" % "config"), "w") as configFile:
        configFile.write(configJson)