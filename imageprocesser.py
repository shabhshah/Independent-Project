from PIL import Image

path = raw_input("Enter path to image (include .jpg): ")

photo = Image.open(path)
photo = photo.convert('RGB')

width, height = photo.size

values = []

for y in range(0, height):
    for x in range(0, width):
    	RGB = photo.getpixel((x,y))
    	print((x, y), RGB)
    	values.append(str(RGB))

z = str(values.count("(255, 119, 0)"))
a = str(float((float((float(int(z))/float(len(values)))))*100))
print "The amount of times #ff7700 appears is " + z +"."
print "The percentage of #ff7700 is " + a + "%."