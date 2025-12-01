
b1 = float(input("primeira nota  "))
b2 = float(input("segunda nota  "))
b3 = float(input("terceira nota  "))
b4 = float(input("quarta nota  "))

somaf = (b1+b2+b3+b4)
print(f"essa é sua média aritmética {somaf/4}")



print(f"total de pontos {somaf}")
if somaf >= 24:
    print(f"voce passou de ano {somaf}")
elif somaf <=23:
    print(f"voce ta devendo ponto {somaf}")
else:
    print(f"você está de recuperaçâo {somaf}")


boletim =("essa é a cor do seu boletim")
if boletim and somaf >=24:
    print(f"{boletim}: verde")
if boletim and somaf <=23:
    print(f"{boletim}: laranja")
elif boletim and somaf <=22:
    print(f"{boletim}: vermelho")
elif boletim and somaf <=21:
    print(f"{boletim}: roxo")
