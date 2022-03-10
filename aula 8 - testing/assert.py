def square(x):
    return x + x

try:
    assert square(10) == 100
except AssertionError:
    print(f'square(10) is equal to {square(10)} not to 100')