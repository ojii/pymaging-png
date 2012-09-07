# -*- coding: utf-8 -*-
from pymaging.colors import RGBA
from pymaging_png.raw import Writer

def write(image, fileobj):
    writer = Writer(
        width=image.width,
        height=image.height,
        alpha=image.mode is RGBA,
        palette=image.palette,
    )
    writer.write_array(fileobj, image.pixels.data)
