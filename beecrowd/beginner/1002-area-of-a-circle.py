PI = 3.14159

r_float = round(float(input("")), 2)
result = round(PI * pow(r_float, 2), 4)
final_result = f"{result:.4f}"

# f"{number:.3f}"

print("A="+str(final_result))