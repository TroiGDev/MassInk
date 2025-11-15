import shutil
import pathlib
import subprocess

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def moveFile(filePath, destinationPath):
    #convert string path to lib path
    filePath = pathlib.Path(filePath)
    destinationPath = pathlib.Path(destinationPath)

    #generate if doesnt exist
    destinationPath.mkdir(exist_ok=True)

    destination = destinationPath / filePath.name
    shutil.move(str(filePath), str(destination))

def exportSVGasPNG(inkscapePath, svgPath, pngPath):
    svg_path = pathlib.Path(svgPath)
    png_path = pathlib.Path(pngPath)
    inkscape_path = pathlib.Path(inkscapePath)


    command = f'"{inkscape_path}" "{svg_path}" ' \
          f'--export-type=png ' \
          f'--export-filename="{png_path}" ' \
          f'--export-id=text1 ' \
          f'--export-id-only ' \
          f'--export-dpi=300'

    subprocess.run(command, shell=True, check=True)

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#get style code
with open("Source/style.svg", "r", encoding="utf-8") as f:
    svg = f.read()

#replace placeholder with correct output text
svg = svg.replace("PLACEHOLDER", "Banana is good")

#generate a new svg with the right output text
with open("output.svg", "w", encoding="utf-8") as f:
    f.write(svg)

#export the new svg as png
exportSVGasPNG(r"C:\Program Files\Inkscape\bin\inkscape.exe", "output.svg", "Source/PNGs/output")

#move new svg to SVGs
moveFile("output.svg", "Source/SVGs")