import math

def solution(w: int, h: int) -> int:
    gcd_result: int = math.gcd(w, h)
    answer = w // gcd_result + h // gcd_result - 1
    return w * h - answer * gcd_result

print(solution(8, 12))