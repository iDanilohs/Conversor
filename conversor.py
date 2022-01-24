def convertir_pesos():
    pesos = input("Pon los pesos que tengas: ")
    pesos = float(pesos)
    valor_dolar = 3974
    dolares = pesos/valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print(f"Tienes $ {dolares} dolares")

def convertir_dolares():
    dolares = input("Pon los dolares que tines: ")
    dolares = float(dolares)
    valor_pesos = 3974
    pesos = valor_pesos * dolares
    pesos = round(pesos, 2)
    pesos = str(pesos)
    print(f"Tienes $ {pesos} pesos")


def run():
  option = int(input(" 1: Para cambiar pesos a dolares 2: Para cambiar dolares a pesos -> "))
  
  if option == 1:
      convertir_pesos()
  elif option == 2:
      convertir_dolares()
  else:
      print("Coloca uno de los números indicados")




if __name__ == '__main__':
    run()