
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_map = []

    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            pair_number = i * len(minor_colors) + j + 1
            line = f'{pair_number} | {major} | {minor}'
            print(line)
            color_map.append(line)
    
    return color_map



def test_total_pairs():
    color_map = print_color_map()
    assert len(color_map) == 25

def test_first_and_last_pair():
    color_map = print_color_map()
    assert color_map[0] == '1 | White | Blue'
    assert color_map[-1] == '25 | Violet | Slate'

def test_format():
    color_map = print_color_map()
    for line in color_map:
        assert '|' in line
        parts = line.split('|')
        assert len(parts) == 3
        assert parts[0].strip().isdigit()
        assert parts[1].strip().isalpha()
        assert parts[2].strip().isalpha()

if __name__ == '__main__':
    test_total_pairs()
    test_first_and_last_pair()
    test_format()
    print("All is well (maybe!)")

