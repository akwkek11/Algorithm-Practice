import sys

def dfs(numbers, target, index, temp_sum):
    if index == len(numbers):
        return 1 if temp_sum == target else 0
    else:
        return dfs(numbers, target, index+1, temp_sum+numbers[index]) + dfs(numbers, target, index+1, temp_sum-numbers[index])

def solution(numbers, target):
    answer: int = 0
    answer += dfs(numbers, target, 0, 0)
    return answer

numbers = list(map(int, sys.stdin.readline().split()))
print(numbers)
target = int(input())
result = solution(numbers, target)

print(f'{result}')