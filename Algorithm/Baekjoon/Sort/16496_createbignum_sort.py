import sys

def solution(numbers):
    size = len(str(max(numbers))) + 1

    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*size, reverse=True) 
    
    return ''.join(numbers) if numbers[0] != '0' else '0'

N: int = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))
print(f'{solution(numbers)}')