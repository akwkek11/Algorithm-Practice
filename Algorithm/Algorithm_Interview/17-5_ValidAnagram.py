def solution(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

print(f'{solution("anagram", "nagaram")}')