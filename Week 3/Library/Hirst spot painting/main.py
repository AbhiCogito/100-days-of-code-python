import colorgram as cg

color_list = cg.extract('dot.jpg', 100)
color_palette = []

for color in color_list:
    r,g,b = color.rgb
    color_palette.append((r,g,b))

print(color_palette)