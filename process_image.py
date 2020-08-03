import os
from PIL import Image

filename = "gon.gif"
new_form = ".ppm"

def convert_to_any(infile, new_format):
    f, e = os.path.splitext(infile)
    outfile = f + new_format

    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.save(outfile)
        except OSError:
            print("cannot convert", infile)

convert_to_any(filename, new_form)
