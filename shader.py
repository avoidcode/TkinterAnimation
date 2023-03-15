import math
from numba import njit

SIGMOID_COEFF = 0.5

@njit
def random(x, y):
    return (math.sin(x * 12.9898 + y * 78.233) * 43758.5453123) % 1

@njit
def sigmoid(x):
    return 1 / (1 + math.exp((SIGMOID_COEFF - x) / 0.2))

@njit
def mix(a, b, v):
    return a * (1 - v) + b * (v)

@njit
def noise(x, y, amplitude):
    fx = math.floor(x * amplitude)
    fy = math.floor(y * amplitude)

    frx = (x * amplitude) % 1
    fry = (y * amplitude) % 1

    a = random(fx, fy)
    b = random(fx + 1, fy)
    c = random(fx, fy + 1)
    d = random(fx + 1, fy + 1)

    ab = mix(a, b, sigmoid(frx))
    cd = mix(c, d, sigmoid(frx))
    n = mix(ab, cd, sigmoid(fry))

    return n

@njit
def sky(x, y):
    f = 0
    k = 0.5
    for i in range(1, 6):
        f += k * noise(x, y, i * 25)
        k /= 2
    return f

@njit
def shader(x, y, t):
    s = sky(x + t * 0.02, y + t * 0.02)
    return (1 - s * 0.5, 1 - s * 0.3, 1)


# @njit
# def shader(x, y, t):
#     n = noise(x * math.sin(t * 0.03), y * math.sin(t * 0.03), 50)
#     return (n, n, n)
