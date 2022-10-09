import colorgram

""""" generating list iof colors form image
pallette = []
colors = colorgram.extract('GUI Module\hirst painting.jpg', 30)

for x in range(0,30):
    current_color = colors[x]
    rgb = current_color.rgb
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    final = (r, g, b)
    pallette.append(final)

print(pallette)
"""

final_colors = [(45, 31, 20), (22, 27, 36), (122, 91, 59), (53, 92, 149), (188, 164, 111), (37, 25, 30), (22, 32, 27), (230, 239, 234), (226, 225, 204), (237, 220, 72), (210, 160, 28), (223, 229, 233), (109, 169, 193), (45, 54, 113), (139, 24, 12), (75, 107, 95), (142, 170, 155), (13, 186, 217), (37, 112, 234), (87, 69, 28), (247, 207, 2), (100, 86, 94), (46, 
174, 162), (138, 20, 29), (164, 158, 161), (220, 215, 218), (210, 98, 54), (34, 82, 72), (19, 86, 95), (164, 207, 183)]



