# Md Mirnatul Islam
# +8801763199000
# www.mirnatul@gmail.com

input_line = input("")
values = input_line.split()

num1 = int(values[0])
num2 = int(values[1])
num3 = int(values[2])
great_12 = int((num1+num2+abs(num1-num2))/2)
great_23 = int((num2+num3+abs(num2-num3))/2)

if great_12>great_23:
    print(great_12, "eh o maior")
else:
    print(great_23, "eh o maior")