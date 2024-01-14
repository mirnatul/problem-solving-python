start_hr, start_min, end_hr, end_min = map(int, input().split())

if end_min<start_min:
    end_min += 60
    start_hr += 1
if (end_min == start_min and end_hr == start_hr) or end_hr<start_hr:
    end_hr += 24

print(f"O JOGO DUROU {end_hr-start_hr} HORA(S) E {end_min-start_min} MINUTO(S)")