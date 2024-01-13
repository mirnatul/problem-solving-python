x, y, z = map(float, input().split())
array = [x,y,z]
array.sort(reverse=True)
A, B, C = array

if A>=B+C:
    print("NAO FORMA TRIANGULO")
elif A**2==(B**2)+(C**2):
    print("TRIANGULO RETANGULO")
elif A**2>(B**2)+(C**2):
    print("TRIANGULO OBTUSANGULO")
elif A**2<(B**2)+(C**2):
    print("TRIANGULO ACUTANGULO")
if A==B and B==C:
    print("TRIANGULO EQUILATERO")
elif A==B or B==C or C==A:
    print("TRIANGULO ISOSCELES")