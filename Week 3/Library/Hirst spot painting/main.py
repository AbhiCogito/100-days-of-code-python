import colorgram as cg

color_list = cg.extract('/Users/Money/Dropbox/Python/100-days-of-code-python/Week 3/Library/Hirst spot painting/dot.jpg', 100)
color_palette = []

for color in color_list:
    r,g,b = color.rgb
    color_palette.append((r,g,b))

print(color_palette)