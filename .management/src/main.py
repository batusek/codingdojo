import shutil


def removeLines(filename: str):
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
    removeLines("../python/blob/worldbank.py")

python()
#javaScript()

