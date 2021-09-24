import sys

H, V = map(float, sys.stdin.readline().strip().split())

# sina = cosb
# sinb = cosa
sina: float = H / ((V ** 2 + H ** 2) ** 0.5)
sinb: float = (1 - sina ** 2) ** 0.5
sinb_2: float = ((1 - sina) / 2) ** 0.5
sinab_2: float = sina * ((1 - sinb_2 ** 2) ** 0.5) + sinb * sinb_2

a: float = V / (1 + (1 / sina))
res_H: float = (1/2) * ((H ** 2 + a ** 2) ** 0.5)
res_V: float = (a / sina) * sinab_2

print(round(res_H, 2), round(res_V, 2))