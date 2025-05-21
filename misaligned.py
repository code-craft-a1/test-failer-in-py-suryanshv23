def get_colors():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]

    return major_colors, minor_colors


def calc_index(i, j, size_of_minor):
    return i * size_of_minor + j


def print_color_map(major_colors, minor_colors):
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{calc_index(i, j, len(minor_colors))} | {major} | {minor}')
    return len(major_colors) * len(minor_colors)

