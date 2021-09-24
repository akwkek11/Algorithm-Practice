import math
import sys

# Catalan Number
catalan = lambda n : math.factorial(2*n) // (math.factorial(n) * math.factorial(n+1))
print(catalan(int(sys.stdin.readline().strip()) // 2) % 987654321)