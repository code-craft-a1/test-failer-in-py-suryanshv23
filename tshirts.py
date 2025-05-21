def size(cms):
    if not isinstance(cms, int) :
        return "Inalid entry"
    if cms <= 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    else:
        return 'L'
