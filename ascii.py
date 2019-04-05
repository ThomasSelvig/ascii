from PIL import Image, ImageOps, ImageColor
from sys import argv
from math import floor

scale = " .'`^\",:;Il!i><~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

if len(argv) < 3:
	print("Usage: ascii [-max <maxPixels>] <imageFile.png> <outputFile.txt>")
	input()
	exit()

# handling command line arguments
passArgs = 0
for i in range(len(argv)):
	if argv[i] == "-max":
		passArgs += 2
		scaleMax = int(argv[i + 1])

sourceFile = argv[1 + passArgs]
outputFile = argv[2 + passArgs]

# open the image
img = Image.open(sourceFile)

# scale the image before processing it (if specified in argv)
if "scaleMax" in globals():
	img.thumbnail((scaleMax, scaleMax), Image.ANTIALIAS)

# clear output file
with open(outputFile, "w") as tmp:
	tmp.write("")

# function for preventing list over-indexing
max = lambda integ, mx: integ if integ < mx else mx-1
# grayscale image
grayImage = ImageOps.grayscale(img)
# pixels loaded as a 2d list
px = grayImage.load() # px[x, y] holds a grayscale value range: 0-255 (black-white)

with open(outputFile, "a") as output:
	relativeScaling = len(scale) / 255
	for y in range(grayImage.size[1]):
		outputString = ""
		for x in range(grayImage.size[0]):
			scaleIndex = max(floor(int(px[x, y]) * relativeScaling), len(scale))
			outputString += scale[scaleIndex]
		output.write(outputString + "\n")
