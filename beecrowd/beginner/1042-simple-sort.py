a, b, c = map(int, input().split())

array = [a, b, c]
preserved = array.copy()

array.sort()

print(f"{array[0]}\n{array[1]}\n{array[2]}\n")
print(f"{preserved[0]}\n{preserved[1]}\n{preserved[2]}")