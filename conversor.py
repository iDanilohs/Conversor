def convertir_pesos(pesos):
    # pesos = float(input("Pon los pesos que tengas: "))
    valor_dolar = 3974
    dolares = str(round(pesos/valor_dolar, 2))
    print(f"Tienes $ {dolares} dolares")

def convertir_dolares(dolares):
    # dolares = float(input("Pon los dolares que tienes: "))
    valor_pesos = 3974
    pesos = str(round(valor_pesos * dolares, 2))
    print(f"Tienes $ {pesos} pesos")


def run():
  option = int(input(" 1: Para cambiar pesos a dolares 2: Para cambiar dolares a pesos -> "))
  money = float(input("Cuanto dinero quieres convertir: "))
  
  if option == 1:
      convertir_pesos(money)
  elif option == 2:
      convertir_dolares(money)
  else:
      print("Coloca uno de los números indicados")


if __name__ == '__main__':
    run()