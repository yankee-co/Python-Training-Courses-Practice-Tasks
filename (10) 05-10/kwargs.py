def wasd(*args):
    b = ''
    for i in args:
        b += str(i)
    return b

print(wasd(2, 6, 9, 7, 3, 1, 5, 0))
