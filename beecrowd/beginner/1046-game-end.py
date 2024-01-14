start, end = map(int, input().split())

if start<end:
    print(f"O JOGO DUROU {end-start} HORA(S)")
else:
    print(f"O JOGO DUROU {(end+24)-start} HORA(S)")