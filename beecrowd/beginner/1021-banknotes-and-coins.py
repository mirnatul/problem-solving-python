# Md Mirnatul Islam
# +8801763199000
# www.mirnatul@gmail.com


# use array for short code

money = float(input(""))

print("NOTAS:")
for i in [100,50,20,10,5,2]:
    print(f"{int(money/i)} nota(s) de R$ {i}.00")
    money = float(f"{money%i:.2f}")

print("MOEDAS:")
for i in [1,0.50,0.25,0.10,0.05,0.01]:
    print(f"{int(money/i)} moeda(s) de R$ {i:.2f}")
    money = float(f"{money%i:.2f}")
