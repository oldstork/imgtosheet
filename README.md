# imgtosheet

A lightweight python utility to convert Blender PNG output into a single large spritesheet.

## Usage

Suppose you exported a Blender animation as a series of PNGs to folder `~/output`. Assuming that imgtosheet is in your path, use the following commands to create a spritesheet:

`$ cd ~`

`$ imgtosheet ./output/ ./output_spritesheet.png`

This will produce a spritesheet from the PNGs at location `~/output_spritesheet.png`.
