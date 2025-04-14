from sys import argv
from pathlib import Path

from pdfinator.convert import convert
from pdfinator.help import help


def main():
    # rm first element
    argv.pop(0)
    argvIter: iter = iter(argv)

    outputFormat: str = None
    inputFormat: str = None
    outputPath: Path = None
    inputPath: Path = None
    errored: bool = False

    formats = ["pdf", "cbz", "cbr"]

    def advance(iterator: iter) -> str:
        try:
            return next(iterator)
        except StopIteration:
            return None

    while True:
        # next() is a better way to run this because it lets me peek and consume quickly
        arg: str = advance(argvIter)
        if arg == None:
            break

        if arg.lower() == "--help":
            # If we realise that it's a --help call, terminate early.
            help()
            return

        elif arg.lower() == "-of":
            outputFormat = advance(argvIter)
            if outputFormat == None:
                print("Malformed input. Expected output format following -of.")
                errored = True
                break

        elif arg.lower() == "-if":
            inputFormat = advance(argvIter)
            if inputFormat == None:
                print("Malformed input. Expected input format following -if.")
                errored = True
                break

        elif arg.lower() == "-o":
            outputPath = Path(advance(argvIter))
            if outputPath == None:
                print("Malformed input. Expected output path following -o.")
                errored = True
                break

        else:
            if inputPath != None:
                print(f"Overwriting previous input: {inputPath}")

            inputPath = Path(arg)

            if inputPath == None:
                print("Missing input path.")
                errored = True
                break

    if outputFormat not in formats:
        print(f"Invalid output format. Accepted values: {formats}")

    if inputFormat not in formats and inputFormat != None:
        print(f"Invalid input format. Accepted values: {formats}")

    if not Path.exists(inputPath):
        print(f"Path {inputPath} does not exist.")

    if outputPath == None:
        outputPath = Path(".")

    convert(
        inputPath,
        inputFormat.lower() if inputFormat != None else inputFormat,
        outputPath,
        outputFormat.lower(),
    )


if __name__ == "__main__":
    main()
