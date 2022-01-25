def convertir_pesos(pesos, option2):
    if option2 == 1:
        valor_dolar = 3964.97
    elif option2 == 2:
        valor_dolar = 104.62
    elif option2 == 3:
        valor_dolar = 20.62

    dolares = str(round(pesos/valor_dolar, 2))
    print(f"Tienes $ {dolares} dolares")

def convertir_dolares(dolares, option2):
    if option2 == 1:
        valor_pesos = 3964.97
    elif option2 == 2:
        valor_pesos = 104.62
    elif option2 == 3:
        valor_pesos = 20.62

    pesos = str(round(valor_pesos * dolares, 2))
    print(f"Tienes $ {pesos} pesos")


def run():
  menu = """
  1 - Pesos colombianos
  2 - Pesos argentinos
  3 - Pesos mexicanos
  Elige una opción: """
  option = int(input(" 1: Para cambiar pesos a dolares 2: Para cambiar dolares a pesos -> "))
  money = float(input("Cuanto dinero quieres convertir: "))
  option2 = int(input(menu))
  
  if option == 1:
      convertir_pesos(money, option2)
  elif option == 2:
      convertir_dolares(money, option2)
  else:
      print("Coloca uno de los números indicados")

if __name__ == '__main__':
    run()