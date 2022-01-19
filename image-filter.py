from PIL import Image
from ast import literal_eval
import os.path

'''Simple function that adds pixels from an image and an
RGBA tuple or pixels from two images, then returns the modified image.'''
def add(filter, image, rgb=False):
    img = image.load() #Third image instance thing for writing
    width, height = image.size

    #Detects if filter is 'red', 'green', 'blue', or a tuple. 
    #If not, assumes another image is being added.
    if filter in color_list or isinstance(filter, tuple):
        if rgb == True:
            print(filter)
            filter = list(filter)
            filter.pop(3)
            filter = tuple(filter)
            print("Adding using RGB tuple...")
        else:
            print("Adding using RGBA tuple...")
        #Using a generator, adds two tuples together then assigns the result to the pixel.
        for i in range(width):
            for j in range(height):
                try:
                    img[i, j] = tuple(l + r for l, r in zip(img[i, j], filter))
                except IndexError:
                    continue
    else:
        print("Adding using pixels from another image...")
        with Image.open(filter) as f: 
            i2 = f.load()
            if rgb == True:
                i2 = i2.convert('RGB')
            #Using a generator, adds two pixels from both images together then assigns the result to a new pixel.
            for i in range(width):
                for j in range(height):
                    try:
                        img[i, j] = tuple(l + r for l, r in zip(img[i, j], i2[i, j]))
                    except IndexError:
                        continue
    return image 

'''Simple function that subtracts pixels from an image and an
RGBA tuple or pixels from two image, then returns the modified images.'''
def subtract(filter, image, rgb=False):
    img = image.load() #Third image instance thing for writing
    width, height = image.size

    #Detects if filter is 'red', 'green', 'blue', or a tuple. 
    #If not, assumes another image is being added.
    if filter in color_list or isinstance(filter, tuple):
        print("Subtracting using RGBA tuple...")

        #Removes the transparency value to avoid making the image transparent.
        filter = list(filter)
        filter.pop(3)
        filter = tuple(filter)

        #Using a generator, subtracts two tuples together then assigns the result to the pixel.
        for i in range(width):
            for j in range(height):
                try:
                    img[i, j] = tuple(l - r for l, r in zip(img[i, j], filter))
                except IndexError:
                    continue
    else:
        print("Subtracting using pixels from another image...")
        with Image.open(filter) as f:
            i2 = f.load()

            if rgb == True:
                i2 = i2.convert('RGB')

            #Using a generator, adds subtracts two tuples together then assigns the result to the pixel.
            for i in range(width):
                for j in range(height):
                    try:
                        img[i, j] = tuple(l - r for l, r in zip(img[i, j], i2[i, j]))
                    except IndexError:
                        continue
    return image  

'''Multiplies the RGBA values from an image and an RGBA tuple or pixels from two images 
by obtaining the ratio of the tuple/pixel to 255 then multiplying the image by the ratio, then returns the modified image.'''
def multiply(filter, image, rgb=False):
    img = image.load() #Third image instance thing for writing
    width, height = image.size

    #Detects if filter is 'red', 'green', 'blue', or a tuple. 
    #If not, assumes another image is being added.
    if filter in color_list or isinstance(filter, tuple):
        if rgb == True:
            print(filter)
            filter = list(filter)
            filter.pop(3)
            filter = tuple(filter)
            print("Multiplying using RGB tuple...")
        else:
            print("Multiplying using RGBA tuple...")
        for i in range(width):
            for j in range(height):
                try:
                    #Obtains the "coefficient" by dividing the RGBA tuple by 255.
                    coefficient = tuple(l / r for l, r in zip(filter, (255, 255, 255, 255)))

                    #Using a generator, multiplies each pixel by the coefficient then rounds the result.
                    img[i, j] = tuple(
                        round(rf) for rf in (
                            l * r for l, r in zip(img[i, j], coefficient)))
                except IndexError:
                    continue
                except ZeroDivisionError:
                    continue
    else:
        print("Multiplying using pixels from another image...")
        with Image.open(filter) as f:
            i2 = f.load()
            if rgb == True:
                i2 = i2.convert('RGB')
            for i in range(width):
                for j in range(height):
                    try:
                        #Obtains the "coefficient" by dividing the RGBA tuple by 255.
                        coefficient = tuple(l / r for l, r in zip(i2[i, j], (255, 255, 255, 255)))

                        #Using a generator, multiplies each pixel by the coefficient then rounds the result.
                        img[i, j] = tuple(
                            round(rf) for rf in (
                                l * r for l, r in zip(img[i, j], coefficient)))
                    except IndexError:
                        continue
                    except ZeroDivisionError:
                        continue
    return image

'''Divides the RGBA values from an image and an RGBA tuple or pixels from two images 
by obtaining the ratio of the tuple/pixel to 255 then dividing the image by the ratio, then returns the modified image.'''
def divide(filter, image, rgb=False):
    img = image.load() #Third image instance thing for writing
    width, height = image.size

    #Detects if filter is 'red', 'green', 'blue', or a tuple. 
    #If not, assumes another image is being added.
    if filter in color_list or isinstance(filter, tuple):
        if rgb == True:
            print(filter)
            filter = list(filter)
            filter.pop(3)
            filter = tuple(filter)
            print("Dividing using RGB tuple...")
        else:
            print("Dividing using RGBA tuple...")
        for i in range(width):
            for j in range(height):
                try:
                    #Obtains the "coefficient" by dividing the RGBA tuple by 255.
                    coefficient = tuple(l / r for l, r in zip(filter, (255, 255, 255, 255)))

                    #Using a generator, divides each pixel by the coefficient then rounds the result.
                    img[i, j] = tuple(
                        round(rf) for rf in (
                            l / r for l, r in zip(img[i, j], coefficient)))
                except IndexError:
                    continue
                except ZeroDivisionError:
                    continue
    else:
        print("Dividing using pixels from another image...")
        with Image.open(filter) as f:
            i2 = f.load()
            if rgb == True:
                i2 = i2.convert('RGB')
            for i in range(width):
                for j in range(height):
                    try:
                        #Obtains the "coefficient" by dividing the RGBA tuple by 255.
                        coefficient = tuple(l / r for l, r in zip(i2[i, j], (255, 255, 255, 255)))

                        #Using a generator, divides each pixel by the coefficient then rounds the result.
                        img[i, j] = tuple(
                            round(rf) for rf in (
                                l / r for l, r in zip(img[i, j], coefficient)))
                    except IndexError:
                        continue
                    except ZeroDivisionError:
                        continue
    return image

'''Function that allows for a secure way to call the functions above. Returns the return values of the functions called.'''
def func_sel(filter, func, image, rgb=False):
    rgb_bool = rgb
    if func == 'add':
        result = add(filter, image, rgb=rgb_bool)
    elif func == 'subtract':
        result = subtract(filter, image, rgb=rgb_bool)
    elif func == 'divide':
        result = divide(filter, image, rgb=rgb_bool)
    elif func == 'multiply':
        result = multiply(filter, image, rgb=rgb_bool)
    return result


if __name__ == '__main__':
    red = (255, 0, 0, 255)
    green = (0, 255, 0, 255)
    blue = (0, 0, 255, 255)

    color_list = [red, green, blue]

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

    color_strlist = ['red', 'green', 'blue']
    
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
        if blend_type not in blend_list:
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