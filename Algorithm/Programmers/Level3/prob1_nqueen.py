def solution(n: int) -> int:
    answer: int = 0
    def backtracking(i: int, col: list, right_dig: list, left_dig: list) -> int:
        ans: int = 0
        if i == n:
            return 1
        else:
            for k in range(n):
                if col[k] == 0 and right_dig[i - k + n] == 0 and left_dig[i + k] == 0:
                    col[k] = right_dig[i - k + n] = left_dig[i + k] = 1
                    ans += backtracking(i + 1, col, right_dig, left_dig)
                    col[k] = right_dig[i - k + n] = left_dig[i + k] = 0

            return ans
    
    col: list = [0 for _ in range(n)]
    right_dig: list = [0 for _ in range(2 * n + 1)]
    left_dig: list = [0 for _ in range(2 * n + 1)]
    answer = backtracking(0, col, right_dig, left_dig)

    return answer

for i in range(4, 13):
    print(solution(i))