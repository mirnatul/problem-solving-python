# Md Mirnatul Islam
# +8801763199000
# www.mirnatul@gmail.com

import math

first_line = input("")
value1 = first_line.split()
x1 = float(value1[0])
y1 = float(value1[1])

second_line = input("")
value2 = second_line.split()
x2 = float(value2[0])
y2 = float(value2[1])

distance = f"{math.sqrt(pow(x2-x1, 2)+pow(y2-y1, 2)):.4f}"
print(distance)