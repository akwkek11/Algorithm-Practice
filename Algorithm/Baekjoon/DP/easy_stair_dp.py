a = [1,1,1,1,1,1,1,1,1,1]
b = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
sum = 0
n = int(input())
for i in range(1,n):

  for j in range(10):
    if j==0:
      b[j] = a[j+1]
    elif j==9:
      b[j] = a[j-1]
    else:
      b[j] = a[j+1] + a[j-1]
  for k in range(10):
    a[k] = b[k]

print(a)
for i in range(1,10):
  sum += a[i]

sum %= 1000000000
print(str(sum))