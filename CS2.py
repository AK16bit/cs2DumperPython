import pyMeow as meow
from pyMeow import Process


class CS2Process(meow.Process):
    processName = "cs2.exe"
    windowName = "Counter-Strike 2"

    def __init__(self):
        super().__init__(self.processName)

        modules = {module.name: module for module in self.modules()}
        self.client = modules.get("client.dll")
        self.engine = modules.get("engine2.dll")
        self.inputSystem = modules.get("inputsystem.dll")
        self.matchmaking = modules.get("matchmaking.dll")
        self.schemaSystem = modules.get("schemasystem.dll")
        self.tier0 = modules.get("tier0.dll")

        global cs2
        cs2 = self


def isCS2ProcessExist() -> bool:
    return meow.pyMeow.process_exists(CS2Process.processName)

def isCS2ProcessReady() -> bool:
    cs2 = meow.Process(CS2Process.processName)
    return False not in [
        meow.pyMeow.module_exists(cs2.process, moduleName)
        for moduleName in (
            "client.dll",
            "engine2.dll",
            "inputsystem.dll",
            "matchmaking.dll",
            "schemasystem.dll",
            "tier0.dll"
        )
    ]



cs2: CS2Process
