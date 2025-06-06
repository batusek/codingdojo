from os import getcwd
import shutil


def adaptFile(filename: str):
    src:str = f"../../.samples/{filename}"
    target:str = f"../../{filename}"
    shutil.copy(src, target)

    with open(target, "r") as f:
        lines = f.readlines()

    with open(target, "w") as f:
        writeLine = True
        for i, line in enumerate(lines):
            if "After start" in line:
                writeLine = False

            if "After end" in line:
                writeLine = True
                continue

            if "Uncomment" in line:
                components = line.split(":")
                f.write(":".join(components[1:]))
                continue

            if writeLine:
                f.write(line)


def python():
    # no adaptation needed for baby steps yet
    adaptFile("python/blob/worldbank.py")
    adaptFile("python/blob/test_worldbank.py")
    adaptFile("python/external_dependencies/htmlformatter.py")
    adaptFile("python/external_dependencies/test_htmlformatter.py")
    adaptFile("python/global_state/globalstate.py")
    adaptFile("python/global_state/test_globalstate.py")
    # no adaptation needed for grow my code yet
    adaptFile("python/irritating_parameter/bankconnector.py")
    adaptFile("python/irritating_parameter/test_bankconnector.py")
    adaptFile("python/legacy_intro/legacyintro.py")
    adaptFile("python/legacy_intro/test_legacyintro.py")
    adaptFile("python/refactoring_alphabet/changemethodsignature.py")
    adaptFile("python/refactoring_alphabet/test_changemethodsignature.py")
    adaptFile("python/refactoring_alphabet/extractmethod.py")
    adaptFile("python/refactoring_alphabet/test_extractmethod.py")
    adaptFile("python/refactoring_alphabet/introduceobject.py")
    adaptFile("python/refactoring_alphabet/test_introduceobject.py")
    adaptFile("python/refactoring_alphabet/replaceconstructor.py")
    adaptFile("python/refactoring_alphabet/test_replaceconstructor.py")
    adaptFile("python/side_effect/invoiceitemmanager.py")
    adaptFile("python/side_effect/test_invoiceitemmanager.py")
    adaptFile("python/tooling/leapyear.py")
    adaptFile("python/tooling/test_leapyear.py")


def javaScript():
    adaptFile("./javascript/tooling/leapyear.ts")
    adaptFile("./javascript/tooling/leapyear.test.ts")
    adaptFile("./javascript/baby_steps/numbers.ts")
    adaptFile("./javascript/baby_steps/numbers.test.ts")
    adaptFile("./javascript/blob/worldbank.ts")
    adaptFile("./javascript/blob/worldbank.test.ts")
    adaptFile("./javascript/canonical_tdd/colors.ts")
    adaptFile("./javascript/canonical_tdd/colors.test.ts")
    adaptFile("./javascript/global_state/globalstate.ts")
    adaptFile("./javascript/global_state/globalstate.test.ts")
    adaptFile("./javascript/grow_my_code/ipv6validator.ts")
    adaptFile("./javascript/grow_my_code/ipv6validator.test.ts")
    adaptFile("./javascript/irritating_parameter/bankconnector.ts")
    adaptFile("./javascript/irritating_parameter/bankconnector.test.ts")
    adaptFile("./javascript/legacy_intro/legacyintro.ts")
    adaptFile("./javascript/legacy_intro/legacyintro.test.ts")
    adaptFile("./javascript/external_dependencies/pokemon.ts")
    adaptFile("./javascript/external_dependencies/pokemon.test.ts")
    shutil.copy("./javascript/external_dependencies/pokemon.ts", "./javascript/external_dependencies/pokemon2.ts")
    adaptFile("./javascript/external_dependencies/pokemon2.test.ts")
    shutil.copy("./javascript/external_dependencies/pokemon.ts", "./javascript/external_dependencies/pokemon3.ts")
    adaptFile("./javascript/external_dependencies/pokemon3.test.ts")
    shutil.copy("./javascript/external_dependencies/pokemon.ts", "./javascript/external_dependencies/pokemon4.ts")
    adaptFile("./javascript/external_dependencies/pokemon4.test.ts")
    adaptFile("./javascript/refactoring_alphabet/changemethodsignature.ts")
    adaptFile("./javascript/refactoring_alphabet/changemethodsignature.test.ts")
    adaptFile("./javascript/refactoring_alphabet/extractmethod.ts")
    adaptFile("./javascript/refactoring_alphabet/extractmethod.test.ts")
    adaptFile("./javascript/refactoring_alphabet/introduceobject.ts")
    adaptFile("./javascript/refactoring_alphabet/introduceobject.test.ts")
    adaptFile("./javascript/refactoring_alphabet/replaceconstructor.ts")
    adaptFile("./javascript/refactoring_alphabet/replaceconstructor.test.ts")
    adaptFile("./javascript/side_effect/invoiceitemmanager.ts")
    adaptFile("./javascript/side_effect/invoiceitemmanager.test.ts")

python()
# javaScript()
