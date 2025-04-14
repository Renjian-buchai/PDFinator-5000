# PDFInator-5000

Finally, an inator that doesn't end with -3000!

```ps
usage: python main.py [options] <path/to/input> -of <output_format>
       python main.py --help

  options:
    -if <input_format>  Input format. If not provided, input will be inferred
                        by *extension*. When a directory is the input, the
                        program will ignore all files that do not have that
                        format.
    -of <output_format> Output format. Must be one of the accepted formats
                        listed below.
    -o <path/to/output> Output path. In the absence of this option, the files
                        will be dumped in the current working directory.
    --help              Shows help menu; i.e., this menu.


  accepted formats:
  - pdf
  - cbz
  - cbr
```
