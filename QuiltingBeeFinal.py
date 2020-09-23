import sys
from PIL import Image, ImageDraw

"""
@author William Wallace
@date 26/04/2020

QuiltingBeeFinal takes input from stdin and draws an image containing
squares of various sizes and colours.
"""

# Display window dimensions
x = 400
y = 400

# Creates viewing window with specified dimensions and background image colour 
im = Image.new('RGB', (x, y), (200, 178, 220))
draw = ImageDraw.Draw(im)

# Variables for creating ratios between squares
index = 0
length = 0
max_scale = 0.0
scale_map = {}

# Draws each of the panels in the quilt to their specifications
def drawSquares(step, x, y):

    # Breaks when index is 0
    if step == 0:
        return

        # Spaces and scales the squares 
    scale, r, g, b = scale_map[index - step]
    area = int(length * scale)
    half = int(area/2)
    
    # Draws over the preexisting image, with squares of specified dimensions and colours
    draw.rectangle((x-area/2, y-area/2, (x-area/2)+area, (y-area/2)+area), fill = (r, g, b), outline = None)
    
    # Recursively draws the squares image at each corner
    # of the four panels, and the panels Themselves
    drawSquares(step-1, x - half, y - half)        # Top left
    drawSquares(step-1, x - half, y + half)        # Bottom left
    drawSquares(step-1, x + half, y - half)        # Top right
    drawSquares(step-1, x + half, y + half)        # Bottom right 

    # Reads the input file and assigns the floats to colours and sizes of the squares
for line in sys.stdin:
    if line == "\s" or line == None or line.rstrip() == "":
        break

    # Splits based on whitespace
    val = line.split(" ")

    # Assigns colours and sizes
    scale = float(val[0])
    r = int(val[1])
    g = int(val[2])
    b = int(val[3])

    # Increments maximum scale and index to accomodate new panels
    max_scale += scale/2
    scale_map.update({index: (scale, r, g, b)})
    index += 1

    #Sets the scale of the entire quilt in relation to display window size    
length = int((x/2)/max_scale)

# Aligns the image to the centre of the display window
drawSquares(index, x/2, y/2)

# Saves the image in current directory
im.save("08.png")