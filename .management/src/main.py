import shutil


def adaptFile(filename: str):
    with open(filename, "r") as f:
        lines = f.readlines()

    with open(filename, "w") as f:
        writeLine = True
        for i, line in enumerate(lines):
            if "After start" in line:
                writeLine = False

            if "After end" in line:
                writeLine = True
                continue

            if "Uncomment" in line:
                components = line.split(":")
                f.write(components[1])

            if writeLine:
                f.write(line)


def python():
    # no adaptation needed for baby steps yet
    adaptFile("../python/blob/worldbank.py")
    adaptFile("../python/blob/test_worldbank.py")
    adaptFile("../python/external_dependencies/test_htmlformatter.py")
    adaptFile("../python/global_state/globalstate.py")
    adaptFile("../python/global_state/test_globalstate.py")
    # no adaptation needed for grow my code yet
    adaptFile("../python/irritating_parameter/bankconnector.py")
    adaptFile("../python/irritating_parameter/test_bankconnector.py")
    adaptFile("../python/legacy_intro/legacyintro.py")
    adaptFile("../python/legacy_intro/test_legacyintro.py")
    adaptFile("../python/refactoring_alphabet/changemethodsignature.py")
    adaptFile("../python/refactoring_alphabet/test_changemethodsignature.py")
    adaptFile("../python/refactoring_alphabet/extractmethod.py")
    adaptFile("../python/refactoring_alphabet/test_extractmethod.py")
    adaptFile("../python/refactoring_alphabet/introduceobject.py")
    adaptFile("../python/refactoring_alphabet/test_introduceobject.py")
    adaptFile("../python/refactoring_alphabet/replaceconstructor.py")
    adaptFile("../python/refactoring_alphabet/test_replaceconstructor.py")
    adaptFile("../python/side_effect/invoiceitemmanager.py")
    adaptFile("../python/side_effect/test_invoiceitemmanager.py")
    adaptFile("../python/tooling/leapyear.py")
    adaptFile("../python/tooling/test_leapyear.py")


python()
