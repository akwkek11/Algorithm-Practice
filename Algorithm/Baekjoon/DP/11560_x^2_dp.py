tc = int(input())

cnt = 0
k = 0
n = 0
p = 2
pcnt = 2

prepool = [0]*400
pool = [0]*400

while cnt < tc:
  k, n = map(int, input().split(' '))
  for i in range(1,k+1):
    if i==1:
      pool[0] = 1
      pool[1] = 1
    else:
      for j in range(1, i+1):
        for o in range(0, p):
          pool[o+j] = pool[o+j] + prepool[o]
    for z in range(0, p):
      prepool[z] = pool[z]
      print(str(prepool[z]), end=' ')

    print()
    p = p + pcnt
    pcnt = pcnt+1

  print(str(pool[n]))
  pool = [0]*400
  prepool = [0]*400
  p = 2
  pcnt = 2
  cnt = cnt+1