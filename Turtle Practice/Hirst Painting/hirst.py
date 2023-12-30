import colorgram

color_list = []

colors = colorgram.extract(
    r'C:\Users\Owner\Documents\Projects\Python\python_projects\Simple Turtle\Hirst Painting\hirst.jpg', 360)

for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    rgbTuple = (r, g, b)
    color_list.append(rgbTuple)

print(color_list)
