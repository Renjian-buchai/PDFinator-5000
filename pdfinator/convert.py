import os
from pathlib import Path
import pymupdf as pdf


def convertFile(
    filePath: Path, inputFormat: str, outputPath: Path, outputFormat: str
) -> bool:
    if outputFormat == "pdf":
        pdfFile: bytes = None
        with pdf.open(filePath) as document:
            pdfFile = document.convert_to_pdf()

        with open(outputPath / (filePath.stem + ".pdf"), "wb") as file:
            file.write(pdfFile)

        print(f"Successfully converted {filePath} to .pdf file.")


def convert(inputPath: Path, inputFormat: str, outputPath: Path, outputFormat: str):
    """Converts files in inputPath to outputFormat, and dumps it in outputPath

    Args:
        inputPath (str): Input path. Can be a directory OR file. Must exist.
        inputFormat (str): Input format. Must be one of the accepted formats.
        outputPath (str): Output path. Must be a directory.
        outputFormat (str): Output format. Must be one of the accepted formats.
    """

    os.makedirs(outputPath, exist_ok=True)

    if Path.is_file(inputPath):
        inputFormat = (Path(inputPath).suffix)[1:]
        convertFile(inputPath, inputFormat, outputPath, outputFormat)
    else:
        files: list[Path] = []
        for file in Path.iterdir(inputPath):
            if file.suffix[1:].lower() == inputFormat:
                files.append(file)

        for file in files:
            convertFile(file, inputFormat, outputPath, outputFormat)
