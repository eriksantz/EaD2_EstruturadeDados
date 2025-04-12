nome = input("Digite o seu nome completo: ")
primeiro_nome = nome.split()[0]

print(f"\nPrimeiro nome (horizontal): {primeiro_nome}")

print("primeiro nome (vertical):")
for letra in primeiro_nome:
    print(letra)
