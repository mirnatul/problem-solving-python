# Md Mirnatul Islam
# +8801763199000
# www.mirnatul@gmail.com

first_line = input("")
values = first_line.split()

prod1 = int(values[0])
amount1 = int(values[1])
price1 = float(values[2])

second_line = input("")
values2 = second_line.split()

prod2 = int(values2[0])
amount2 = int(values2[1])
price2 = float(values2[2])

value_to_pay = (amount1*price1)+(amount2*price2)
two_decimal_value_to_pay = f"{value_to_pay:.2f}"

print("VALOR A PAGAR: R$", two_decimal_value_to_pay)