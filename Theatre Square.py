import math
n, m, a = map(int, input().split())
tiles_length = math.ceil(n / a)
tiles_width = math.ceil(m / a)
print(tiles_length * tiles_width)