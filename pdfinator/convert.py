from os import path, makedirs
import pymupdf as pdf


def convert(inputPath: str, inputFormat: str, outputPath: str, outputFormat: str):
    """Converts files in inputPath to outputFormat, and dumps it in outputPath

    Args:
        inputPath (str): Input path. Can be a directory OR file. Must exist.
        inputFormat (str): Input format. Must be one of the accepted formats.
        outputPath (str): Output path. Must be a directory.
        outputFormat (str): Output format. Must be one of the accepted formats.
    """
