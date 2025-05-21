from misaligned import calc_index, print_color_map, get_colors

major_colors, minor_colors = get_colors()
result = print_color_map(major_colors, minor_colors)
assert(major_colors == ["White", "Red", "Black", "Yellow", "Violet"])
assert(minor_colors == ["Blue", "Orange", "Green", "Brown", "Slate"])
assert(calc_index(1, 2, 3) == 5)
assert(result == 25)
print("All is well (maybe!)")