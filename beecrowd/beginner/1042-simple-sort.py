# not finished

a, b, c = map(int, input().split())

array = [a, b, c]
preserved = array.copy()
preserved2 = array[:]

array.sort()

print(array)
print(preserved)
print(preserved2)