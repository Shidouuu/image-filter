from PIL import Image
from ast import literal_eval
import os.path
import operator
import argparse

#Predefine colors incase you're too lazy to type up a tuple.
red = (255, 0, 0, 255)
green = (0, 255, 0, 255)
blue = (0, 0, 255, 255)

color_list = [red, green, blue]

'''Computes two numbers using a given operator.'''
def ops_func(op_char, a, b):
    ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "x": operator.mul,
    "/": operator.truediv
    }  
    func = ops[op_char]
    return func(a, b)

'''Adds, subtracts, multiplies, or divides the pixels of an image and a tuple or the pixels of two images, then returns the result.'''
def blend(filter, image, op, rgb=False):
    img = image.load() #Third image instance thing for writing
    width, height = image.size
    if rgb == True:
        cmode = "RGB"
    else:
        cmode = "RGBA"

    #Dict for identifying which operation to use.
    op_dict = {"+": 'Adding', "-": 'Subtracting', "*": 'Multiplying', "x": 'Multiplying', "/": 'Dividing'}
    for i in op_dict:
        if op == i:
            op_mode = op_dict[i]

    #Detects if filter is 'red', 'green', 'blue', or a tuple. 
    #If not, assumes another image is being added.
    if filter in color_list or isinstance(filter, tuple):
        if rgb == True or op == '-':
            filter = list(filter)
            filter.pop(3)
            filter = tuple(filter)

        print(op_mode + " using " + cmode + " tuple...")

        #Using a generator, adds two tuples together then assigns the result to the pixel.
        if op != '+' or op != '-':
            #"Coefficient" which is the ratio of the filter to 255
            coefficient = tuple(l / r for l, r in zip(filter, (255, 255, 255, 255))) 
        for i in range(width):
            for j in range(height):
                try:
                    if op == '+' or op == '-':
                        img[i, j] = tuple(ops_func(op, l, r) for l, r in zip(img[i, j], filter))
                    else: #rounds when multiplying or dividing
                            img[i, j] = tuple(round(ops_func(op, l, r)) for l, r in zip(img[i, j], coefficient))
                except IndexError:
                    continue
                except ZeroDivisionError:
                    continue
    else:
        print(op_mode + " using pixels from another image...")
        with Image.open(filter) as f: 
            i2 = f.load()
            if rgb == True:
                i2 = i2.convert('RGB')
            #Using a generator, adds two pixels from both images together then assigns the result to a new pixel.
            for i in range(width):
                for j in range(height):
                    try:
                        if op == '+' or op == '-':
                            img[i, j] = tuple(ops_func(op, l, r) for l, r in zip(img[i, j], i2[i, j]))
                        else: #rounds when multiplying or dividing
                            #"Coefficient" which is the ratio of the filter to 255
                            coefficient = tuple(l / r for l, r in zip(i2[i, j], (255, 255, 255, 255)))
                            img[i, j] = tuple(round(ops_func(op, l, r)) for l, r in zip(img[i, j], coefficient))
                    except IndexError:
                        continue
                    except ZeroDivisionError:
                        continue
    return image 


'''Function that allows for a secure way to call the functions above. Returns the return values of the functions called.'''
def func_sel(filter, func, image, cmode=False):
    blend_dict = {'add': '+', 'subtract': '-', 'multiply': 'x', 'divide': '/'}
    return blend(filter, image, blend_dict[func], rgb=cmode)


#Defines args to be used in terminal.
parser = argparse.ArgumentParser(description='Image Filter')
parser.add_argument('-i', '--image', help='Image to be modified.', required=False, default='dermott')
parser.add_argument('-f', '--filter', help='Either a second image or an RGBA tuple.', required=False)
parser.add_argument('-o', '--output', help='Output file name.', required=False, default= 'result')
parser.add_argument('-fo', '--format', help='Output file format.', required=False, default= 'png')
parser.add_argument('-m', '--mode', help='Color mode.', required=False, default='RGBA', choices=['RGBA', 'RGB'])
parser.add_argument('-b', '--blend', help='Blend mode.', required=False, choices=['add', 'subtract', 'multiply', 'mul', 'divide', 'div'])
args = parser.parse_args()
arg_list = vars(args).values()
default_args = ['dermott', 'result', 'png', 'RGBA']

#Parses args then calls func_sel()
for i in arg_list:
    if i != None and i not in default_args:
        if args.image == 'dermott':
            im = Image.open('mcdermott.png')
        elif os.path.isfile(args.image):
            im = Image.open(args.image)
        else:
            raise FileNotFoundError('File not found.')
        result = func_sel(args.filter, args.blend, im, args.mode)
        result.save(args.output + '.' + args.format)
        exit()

#If no arguments are given, defaults to dumb mode and prompts user for inputs
if __name__ == '__main__':
    img_sel = None
    while img_sel == None:
        img_sel = input('Select an image from the current directory, or press enter to use a picture of Mr.McDermott: ')
        if img_sel == '':
            im = Image.open('mcdermott.png')
        elif os.path.isfile(img_sel):
            im = Image.open(img_sel)
        else:
            print("File not found! Make sure you include the full file name (file extensions) and that the characters are the same case! Try again.")
            img_sel = None
            continue

    color_strlist = ['red', 'green', 'blue'] #For checking if user input is red, green, or blue
    
    img2 = None
    while img2 == None:
        img2 = (input("Select a filter from the list, create an RGBA filter (#, #, #, #), or type in an image from the directory: \nRed, Green, Blue\n")).lower()
        if img2 == '':
            print("Please enter something.")
            img2 = None
    
    blend_list = ['add', 'subtract', 'multiply', 'divide']
    blend_type = None
    while blend_type == None:
        blend_type = (input("Select a blend mode: Add | Subtract | Multiply | Divide\n")).lower()
        if blend_type not in blend_list: #Check if blend mode is valid
            print("Not a blend mode. Try again.")
            blend_type = None
    
    name = input("Select a name for the image or press enter to use the default name 'result': ")
    if name == '':
        name = 'result'
    format = (input("Select a format for the image or press enter to export as png. You can also type in a format not on the list and see if that works!\nbmp | gif | jpg/jpeg | png\n")).lower()
    format_list = ['bmp', 'gif', 'png']
    if format == '':
        format = '.png'
    elif format == 'jpg' or format == 'jpeg':
        im = im.convert('RGB')
        format = '.' + format
    elif format in format_list:
        format = "." + format
    else:
        print("Exporting to wildcard format...")
        format = '.' + format


    #Determines proper variables to call func_sel() with
    if img2 in color_strlist:
        color_index = color_strlist.index(img2)
        result = func_sel(color_list[color_index], blend_type, im)
    elif os.path.isfile(img2):
        result = func_sel(img2, blend_type, im)
    else:
        eval = literal_eval(img2)
        if isinstance(eval, tuple):
            if format == '.jpg':
                result = func_sel(eval, blend_type, im, rgb=True)
            elif len(eval) == 3:
                result = func_sel(eval + (255,), blend_type, im)
            elif len(eval) == 4:
                result = func_sel(eval, blend_type, im)
            else:
                print("Tuple must be a value of 4 integers.")
        else:
            print("Invalid image format.")
    print("Saving...")
    result.save(name + format)
    print("Done!")
    


