# Md Mirnatul Islam
# +8801763199000
# www.mirnatul@gmail.com

total = int(input(""))

notes_100 = int(total/100)
remain_100 = total%100

notes_50 = int(remain_100/50)
remain_50 = remain_100%50

notes_20 = int(remain_50/20)
remain_20 = remain_50%20

notes_10 = int(remain_20/10)
remain_10 = remain_20%10

notes_5 = int(remain_10/5)
remain_5 = remain_10%5

notes_2 = int(remain_5/2)
remain_2 = remain_5%2

notes_1 = int(remain_2/1)

print(total)
print(notes_100, "nota(s) de R$ 100,00")
print(notes_50, "nota(s) de R$ 50,00")
print(notes_20, "nota(s) de R$ 20,00")
print(notes_10, "nota(s) de R$ 10,00")
print(notes_5, "nota(s) de R$ 5,00")
print(notes_2, "nota(s) de R$ 2,00")
print(notes_1, "nota(s) de R$ 1,00")


# 5 nota(s) de R$ 100,00
# 1 nota(s) de R$ 50,00
# 1 nota(s) de R$ 20,00
# 0 nota(s) de R$ 10,00
# 1 nota(s) de R$ 5,00
# 0 nota(s) de R$ 2,00
# 1 nota(s) de R$ 1,00
