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

def insertLines(filename: str, start: int, excerpt: list[str]):
    with open(filename, "r") as f:
        lines = f.readlines()

    with open(filename, "w") as f:
        for i, line in enumerate(lines):
            if i == start:
                for l in excerpt:
                    f.write(l)

            f.write(line)


def python():
    # adaptFile("../python/blob/worldbank.py")
    # adaptFile("../python/blob/test_worldbank.py")
    # adaptFile("../python/external_dependencies/test_htmlformatter.py")
    adaptFile("../python/global_state/globalstate.py")
    adaptFile("../python/global_state/test_globalstate.py")


python()
#javaScript()

