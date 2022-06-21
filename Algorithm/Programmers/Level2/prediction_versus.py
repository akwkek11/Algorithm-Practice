def solution(n: int, a: int, b :int) -> int:
    answer: int = 0
    people_a: int = min(a, b)
    people_b: int = max(a, b)

    while (people_a + 1) % 2 != 0 or people_a + 1 != people_b:
        people_a = (people_a + 1) // 2
        people_b = (people_b + 1) // 2
        answer += 1

    answer += 1
    return answer