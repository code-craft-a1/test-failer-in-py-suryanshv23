
def size(cms):
    if cms < 38:
        return 'S'
    elif 38 <= cms < 42:
        return 'M'
    else:
        return 'L'

assert(size(0) == 'S')
assert(size(37.9) == 'M')

assert(size(38) == 'S')

# Exact boundary values
assert(size(38) == 'M')  # previously failed
assert(size(41.9) == 'M')
assert(size(42) == 'L')

# Large values
assert(size(100) == 'L')

print("All tests passed!")
assert(size(37) == 'S')
assert(size(40) == 'M')
assert(size(43) == 'L')
print("All is well (maybe!)")
