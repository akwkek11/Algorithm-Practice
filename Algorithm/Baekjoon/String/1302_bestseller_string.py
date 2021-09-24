import sys

bestseller: dict = {}

n: int = int(sys.stdin.readline().strip())

for _ in range(n):
    book_name: str = sys.stdin.readline().strip()
    if not bestseller.get(book_name):
        bestseller[book_name] = 1
    else:
        bestseller[book_name] += 1

result = dict(reversed(sorted(dict(reversed(sorted(bestseller.items(), key=lambda item: item[0]))).items(), key=lambda item: item[1])))

values_view = result.keys()
value_iterator = iter(values_view)
first_key = next(value_iterator)

print(first_key)