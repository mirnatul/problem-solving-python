# Md Mirnatul Islam
# +8801763199000
# www.mirnatul@gmail.com

PI = 3.14159

input_line = input("")
values = input_line.split()

a = float(values[0])
b = float(values[1])
c = float(values[2])

triangulo = f"{(1/2)*a*c:.3f}"
circulo = f"{PI*pow(c,2):.3f}"
trapezio = f"{((a+b)/2)*c:.3f}"
quadrado = f"{pow(b,2):.3f}"
retangulo = f"{a*b:.3f}"

print("TRIANGULO:", triangulo)
print("CIRCULO:", circulo)
print("TRAPEZIO:", trapezio)
print("QUADRADO:", quadrado)
print("RETANGULO:", retangulo)