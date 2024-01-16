import colorgram

rgb_colors = []
# extracting 30 colors from an image
colors = colorgram.extract('butterfly.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)




