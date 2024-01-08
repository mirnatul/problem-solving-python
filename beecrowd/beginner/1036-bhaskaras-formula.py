import math
a, b, c = list(map(float, input().split()))

delta = round(pow(b, 2)-4*a*c, 2)

if a==0 or delta<0:
    print("Impossivel calcular")
else:
    x1 = f"{(-b+math.sqrt(delta))/(2*a):.5f}"
    x2 = f"{(-b-math.sqrt(delta))/(2*a):.5f}"
    print("R1 =", x1)
    print("R2 =", x2)