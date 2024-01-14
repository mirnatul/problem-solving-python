salary = float(input())
bonus = 0

if salary<=400:
    bonus = salary*(15/100)
    percentage = 15
elif salary<=800:
    bonus = salary*(12/100)
    percentage = 12
elif salary<=1200:
    bonus = salary*(10/100)
    percentage = 10
elif salary<=2000:
    bonus = salary*(7/100)
    percentage = 7
elif salary>2000:
    bonus = salary*(4/100)
    percentage = 4

print(f"Novo salario: {salary+bonus:.2f}")
print(f"Reajuste ganho: {bonus:.2f}")
print(f"Em percentual: {percentage} %")