values = [4, 4.50, 5, 2, 1.50]
product, quantity = map(int, input().split())

print(f"Total: R$ {values[product-1]*quantity:.2f}")