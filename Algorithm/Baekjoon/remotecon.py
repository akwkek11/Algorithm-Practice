# not solved
# 자릿수 말고, 좀 더 일반화된 방식으로 접근할 것

# start : initialization
start: int = 100

# target : where to go, n : num of damaged buttons, damaged : list of damaged buttons
target: int = int(input())
n: int = int(input())
damaged: list = list(map(int, input().split()))

# min_start : min distance of the target, num_queue : 500000 -> 5 0 0 0 0 0, temp_start : min_start = min(abs(start-target), abs(int(temp_start)-target))
min_start: int = 0
num_queue: str = str(target)
temp_start: str = ''

one_number = 1000000000
for s in num_queue:
    out = int(s)
    min_distance = 10
    res = ''
    for i in range(0, 10):
        distance = 10
        if i not in damaged:
            one_number = i
            if len(num_queue) >= 2 and out > i and temp_start != '':
                distance = 10+i-out
            else:
                distance = abs(out-i)
            
            if distance <= min_distance:
                min_distance = distance
                res = str(i)   

    temp_start += res

if temp_start == '':
    if min(abs(one_number-target), abs(start-target)) == abs(one_number-target):
        min_start = one_number
    else:
        min_start = start

elif min(abs(start-target), abs(int(temp_start)-target)) == abs(start-target):
    if min(abs(one_number-target), abs(start-target)) == abs(one_number-target):
        min_start = one_number
    else:
        min_start = start
else:
    if min(abs(one_number-target), abs(int(temp_start)-target)) == abs(one_number-target):
        min_start = one_number
    else:
        min_start = int(temp_start)

result = 0
if min_start == start:
    result = abs(min_start-target)
else :
    result = len(str(min_start))+abs(min_start-target)
print(result)