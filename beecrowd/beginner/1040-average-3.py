a, b ,c, d = map(float, input().split())
media_str = f"{((a*2+b*3+c*4+d*1)/10):.1f}"
media = float(media_str)

if media >= 7.0:
    print(f"Media: {media}")
    print("Aluno aprovado.")
elif media <= 6.9 and media >=4.9:
    print(f"Media: {media}")
    print("Aluno em exame.")
    another_score = float(input())
    print(f"Nota do exame: {another_score}")
    final_score_str = f"{((media+another_score)/2):.1f}"
    final_score = float(final_score_str)
    if final_score >= 5.0:
        print("Aluno aprovado.")
    elif final_score <= 4.9:
        print("Aluno reprovado.")
    print(f"Media final: {final_score}")
elif media < 5.0:
    print(f"Media: {media}")
    print("Aluno reprovado.")