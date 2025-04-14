from sys import argv
from os import path

import pdfinator


def main():
    # rm first element
    argv.pop(0)
    argvIter: iter = iter(argv)

    outputFormat: str = None
    inputFormat: str = None
    outputPath: str = None
    inputPath: str = None
    errored: bool = False

    formats = ["pdf", "cbz", "cbr"]

    def advance(iterator: iter[str]) -> str:
        try:
            return next(iterator)
        except StopIteration:
            return None

    while True:
        # next() is a better way to run this because it lets me peek and consume quickly
        arg: str = advance(argvIter)

        if arg.lower() == "--help":
            # If we realise that it's a --help call, terminate early.
            pdfinator.help()
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
            outputPath = advance(argvIter)
            if outputPath == None:
                print("Malformed input. Expected output path following -o.")
                errored = True
                break

        else:
            if inputPath != None:
                print(f"Overwriting previous input: {inputPath}")

            inputPath = advance(argvIter)

            if inputPath == None:
                print("Missing input path.")
                errored = True
                break

    if outputFormat not in formats:
        print(f"Invalid output format. Accepted values: {formats}")

    if inputFormat not in formats:
        print(f"Invalid input format. Accepted values: {formats}")

    if not path.exists(inputPath):
        print(f"Path {inputPath} does not exist.")

    pdfinator.convert(inputPath, inputFormat, outputPath, outputFormat)


if __name__ == "__main__":
    main()
