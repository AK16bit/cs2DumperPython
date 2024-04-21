from time import perf_counter
from typing import List

from Builder.SignatureBuilder import signatureBuilder
from CS2 import cs2
from Dumper.ButtonDump import buttonSignature
from Signature.Container import ContainerSignature, ContainerModule
from Signature.Signature.SignatureClient import clientSignatures
from Signature.Signature.SignatureEngine import engineSignatures
from Signature.Signature.SignatureInputsystem import inputsystemSignatures
from Signature.Signature.SignatureMatchmaking import matchmakingSignatures
from utils import logger, int2hex, timeUseInfo, errorButDontCloseWindow


@errorButDontCloseWindow
@timeUseInfo
def dumpSignature() -> None:
    client = clientSignature()
    engine = engineSignature()
    inputsystem = inputsystemSignature()
    matchmaking = matchmakingSignature()

    signatureBuilder((client, engine, inputsystem, matchmaking))




def clientSignature() -> ContainerModule:
    patterns = clientSignatures()
    timeUseCounter = perf_counter()

    logger.debug("Module: %s (Count: %s)" % (
        cs2.client.name,
        len(patterns)
    ))

    signaturesCtr: List[ContainerSignature] = list()
    for pattern in patterns:
        signatureName = pattern.__name__
        signature = pattern()

        signatureCtr = ContainerSignature(name=signatureName, value=signature.offset)
        signaturesCtr.append(signatureCtr)

        logger.debug(" · %s -> Signature: %s (Address: %s) (Offset: %s)" % (
            signature.pattern,
            signatureName,
            int2hex(signature.address),
            int2hex(signature.offset),
        ))

    buttonSignaturesCtr = buttonSignature().get("signatures")
    signaturesCtr = [*signaturesCtr, *buttonSignaturesCtr]

    timeUse = (perf_counter() - timeUseCounter) * 1000
    logger.debug("Module: %s Dump Finished in %s ms" % ("client.dll", timeUse))

    return ContainerModule(name=cs2.client.name.replace(".", "_"), signatures=signaturesCtr)


def engineSignature() -> ContainerModule:
    patterns = engineSignatures()
    timeUseCounter = perf_counter()

    logger.debug("Module: %s (base: %s) (size: %s)" % (
        cs2.engine.name,
        int2hex(cs2.engine.base),
        int2hex(cs2.engine.size)
    ))

    signaturesCtr: List[ContainerSignature] = list()
    for pattern in patterns:
        signatureName = pattern.__name__
        signature = pattern()

        signatureCtr = ContainerSignature(name=signatureName, value=signature.offset)
        signaturesCtr.append(signatureCtr)

        logger.debug(" · %s -> Signature: %s (Address: %s) (Offset: %s)" % (
            signature.pattern,
            signatureName,
            int2hex(signature.address),
            int2hex(signature.offset),
        ))

    timeUse = (perf_counter() - timeUseCounter) * 1000
    logger.debug("Module: %s Dump Finished in %s ms" % ("engine2.dll", timeUse))

    return ContainerModule(name=cs2.engine.name.replace(".", "_"), signatures=signaturesCtr)

def inputsystemSignature() -> ContainerModule:
    patterns = inputsystemSignatures()
    timeUseCounter = perf_counter()

    logger.debug("Module: %s (base: %s) (size: %s)" % (
        cs2.inputSystem.name,
        int2hex(cs2.inputSystem.base),
        int2hex(cs2.inputSystem.size)
    ))

    signaturesCtr: List[ContainerSignature] = list()
    for pattern in patterns:
        signatureName = pattern.__name__
        signature = pattern()

        signatureCtr = ContainerSignature(name=signatureName, value=signature.offset)
        signaturesCtr.append(signatureCtr)

        logger.debug(" · %s -> Signature: %s (Address: %s) (Offset: %s)" % (
            signature.pattern,
            signatureName,
            int2hex(signature.address),
            int2hex(signature.offset),
        ))

    timeUse = (perf_counter() - timeUseCounter) * 1000
    logger.debug("Module: %s Dump Finished in %s ms" % ("inputSystem.dll", timeUse))

    return ContainerModule(name=cs2.inputSystem.name.replace(".", "_"), signatures=signaturesCtr)

def matchmakingSignature() -> ContainerModule:
    patterns = matchmakingSignatures()
    timeUseCounter = perf_counter()

    logger.debug("Module: %s (base: %s) (size: %s)" % (
        cs2.matchmaking.name,
        int2hex(cs2.matchmaking.base),
        int2hex(cs2.matchmaking.size)
    ))

    signaturesCtr: List[ContainerSignature] = list()
    for pattern in patterns:
        signatureName = pattern.__name__
        signature = pattern()

        signatureCtr = ContainerSignature(name=signatureName, value=signature.offset)
        signaturesCtr.append(signatureCtr)

        logger.debug(" · %s -> Signature: %s (Address: %s) (Offset: %s)" % (
            signature.pattern,
            signatureName,
            int2hex(signature.address),
            int2hex(signature.offset),
        ))

    timeUse = (perf_counter() - timeUseCounter) * 1000
    logger.debug("Module: %s Dump Finished in %s ms" % ("matchmaking.dll", timeUse))

    return ContainerModule(name=cs2.matchmaking.name.replace(".", "_"), signatures=signaturesCtr)





# def a2xSignatureConverter(patternA2x: str):
#     patternA2x = (
#         patternA2x
#         .replace(" ", "")
#         .replace("'", "")
#         .replace("?", "??")
#     )
#
#     patternA2x = patternA2x.format(
#         *("?" * 8 for _ in range(patternA2x.count("$")))
#     )
#     pattern = patternA2x.replace("$", "")
#
#
#     return pattern
#
#
# def a2xAnalyzer() -> Dict[str, str]:
#     regexPattern = compile(r"""\"(.+?)\" => pattern!\(\"(.+?)\"\)""")
#
#     with open("../Signature/offsets.rs", "r") as a2xSignatureCode:
#         patternsUnconverted = [result for codeLine in a2xSignatureCode if (result := regexPattern.findall(codeLine))]
#         patterns = {patternUnconverted[0]: a2xSignatureConverter(patternUnconverted[1]) for patternUnconverted in [itemgetter(0)(patternUnconverted) for patternUnconverted in patternsUnconverted]}
#
#     return patterns
#
#
#
#
# if __name__ == "__main__":
#     dwSensitivityPattern = a2xSignatureConverter("488b05${'} 488b40? f3410f59f4")
#     print(dwSensitivityPattern)
#
#     dwBuildNumberPattern = a2xSignatureConverter("8905${'} 488d0d${} ff15${} e9")
#     print(dwBuildNumberPattern)
#
#     dwSensitivity_sensitivityPattern = a2xSignatureConverter("ff50u1 4c8bc6 488d55? 488bcf e8${} 84c0 0f85${} 4c8d45? 8bd3 488bcf e8${} e9${} f30f1006")
#     print(dwSensitivity_sensitivityPattern)
