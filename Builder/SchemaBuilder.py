from json import dumps
from os import mkdir
from os.path import exists, join, split
from typing import Sequence

from Schema.Container import ContainerModule


def schemaBuilder(modulesCtr: Sequence[ContainerModule]) -> None:
    outputLocation = "Output\\Schema"
    if not exists(split(outputLocation)[0]): mkdir(split(outputLocation)[0])
    if not exists(outputLocation): mkdir(outputLocation)

    for moduleCtr in modulesCtr:
        moduleName = moduleCtr.get("name")
        # if not "client" in moduleDumpedCtr.get("name"): continue

        moduleDict = {
            classCtr.get("name"): {
                fieldCtr.get("name"): fieldCtr.get("value")
                for fieldCtr in classCtr.get("fields")
            }
            for classCtr in moduleCtr.get("classes")
        }
        moduleJson = dumps(moduleDict, indent=4)

        with open(join(outputLocation, "%s.json" % moduleName), "w") as moduleFile:
            moduleFile.write(moduleJson)
