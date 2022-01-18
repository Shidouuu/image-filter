######################################
# Image Filter Project Starter Code  #
#                                    #
#             UTeach CSP             #
#                                    #
######################################


# importing PIL.Image library and os library
from PIL import Image #from PIL import Image 
import os

# Deletes old created images if they exist
images = ["StudentWork/combinedFilters.jpg","StudentWork/filter1.jpg","StudentWork/filter2.jpg","StudentWork/filter3.jpg","StudentWork/gray.jpg"]
for i in images:
	if os.path.exists(i):
		os.remove(i)

# Adds two blank lines before any output
print("\n\n")

# Opens image - upload a Local File into repl.it
img = Image.open('StudentWork/image.jpg')

# Rescale image size down, if original is too large
width = img.width
height = img.height
mwidth = width // 1000
mheight = height // 1000
if mwidth > mheight:
	scale = mwidth
else:
	scale = mheight
if scale != 0:
	img = img.resize( (width // scale, height // scale) )

########################
#    Example Filter    #
########################
def gray():
	print("Code for grayscale")
	# Creates an ImageCore Object from original image
	pixels = img.getdata()
	# Creates empty array to hold new pixel values
	new_pixels = []
	# For every pixel from our original image, it saves
	# a copy of that pixel to our new_pixels array
	for p in pixels:
		new_pixels.append(p)
	# Starts at the first pixel in the image
	location = 0
	# Continues until it has looped through all pixels
	while location < len(new_pixels):
		# Gets the current color of the pixel at location
		p = new_pixels[location]
		# Splits color into red, green and blue components
		r = p[0]
		g = p[1]
		b = p[2]
		# Perform pixel manipulation and stores results
		# to a new red, green and blue components
		newr = (r + g + b) // 3
		newg = (r + g + b) // 3
		newb = (r + g + b) // 3
		# Assign new red, green and blue components to pixel
		# # at that specific location
		new_pixels[location] = (newr, newg, newb)
		# Changes the location to the next pixel in array
		location = location + 1
	# Creates a new image, the same size as the original 
	# using RGB value format
	newImage = Image.new("RGB", img.size)
	# Assigns the new pixel values to newImage
	newImage.putdata(new_pixels)
	# Sends the newImage back to the main portion of program
	return newImage


#####################
#    Your Filter    #
#####################

def filter1():
	print("Code for filter1")
	newImage = img
	return newImage

#####################################
#    Your Filters with User Input   #
#####################################

def filter2():
	print("Code for filter2")
	newImage = img
	return newImage

def filter3():
	print("Code for filter3")
	newImage = img
	return newImage

# Creates the four filter images and saves them to our files
a = gray()
a.save("StudentWork/gray.jpg")
b = filter1()
b.save("StudentWork/filter1.jpg")
c = filter2()
c.save("StudentWork/filter2.jpg")
d = filter3()
d.save("StudentWork/filter3.jpg")

# Image filter names for use below
f1 = "filter1"
f2 = "filter2"
f3 = "filter3"

# Apply multiple filters through prompts with the user
print("\nThe following prompt will ask you which filter to apply to the combined filter. It will keep asking until you answer 'none'.")
answer = input("\nWhich filter do you want me to apply?\n gray\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")
while answer != "gray" and answer != f1 and answer != f2 and answer != f3 and answer != "none":
	answer = input("\nIncorrect filter, please enter:\n gray\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")

while answer == "gray" or answer == f1 or answer == f2 or answer == f3:
	if answer == "gray":
		img = gray()
	elif answer == f1:
		img = filter1()
	elif answer == f2:
		img = filter2()
	elif answer == f3:
		img = filter3()
	else:
		break
	print("Filter \"" + answer + "\" applied...")
	answer = input("\nWhich filter do you want me to apply next?\n gray\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")
	while answer != "gray" and answer != f1 and answer != f2 and answer != f3 and answer != "none":
		answer = input("\nIncorrect filter, please enter:\n gray\n " +  f1 + "\n " + f2 + "\n " + f3 + "\n none\n\n")

print("Combined filter being created...Done")

# Create the combined filter image and saves it to our files
img.save("StudentWork/combinedFilters.jpg")