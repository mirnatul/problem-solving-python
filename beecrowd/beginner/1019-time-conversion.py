# Md Mirnatul Islam
# +8801763199000
# www.mirnatul@gmail.com

sec = int(input(""))

hr = int(sec/3600)
remain_sec = sec%3600

min = int(remain_sec/60)
remain_sec = remain_sec%60

print(str(hr)+":"+str(min)+":"+str(remain_sec))