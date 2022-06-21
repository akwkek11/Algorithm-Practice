def solution(n: int, k: int) -> int:
    
    answer: int = 0
    k_n: list = []
    while n >= k:
        k_n.append(str(n % k))
        n //= k
    k_n.append(str(n))
    result = (''.join(k_n[::-1])).split('0')
    for i in result:
        if i != '' and int(i) > 1 and int(i) <= 10 ** 13:
            check: int = int(i)
            p: int = int(check ** 0.5)
            is_prime = True

            for i in range(2, p + 1):
                if check % i == 0:
                    is_prime = False
                    break

            if is_prime:
                answer += 1
    return answer

print(solution(524287, 3))
print(solution(110011, 10))