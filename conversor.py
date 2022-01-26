def peso_o_dolar(option, mensaje, money, valor_dolar):
    if option == 1:
        convertir_pesos(money, valor_dolar)
    elif option == 2:
        convertir_dolares(mensaje, money, valor_dolar)
    else:
        print("Coloca uno de los números indicados")

def convertir_pesos(pesos, valor_dolar):
    dolares = str(round(pesos/valor_dolar, 2))
    print(f"Tienes $ {dolares} dolares")

def convertir_dolares(mensaje, dolares, valor_dolar):
    pesos = str(round(valor_dolar * dolares, 2))
    print(f"Tienes $ {pesos} {mensaje}")


def run():
  menu = """
  1 - Pesos colombianos
  2 - Pesos argentinos
  3 - Pesos mexicanos
  Elige una opción: """

  option = int(input(" 1: Para cambiar pesos a dolares 2: Para cambiar dolares a pesos -> "))
  money = float(input("Cuanto dinero quieres convertir: "))
  option2 = int(input(menu))

  if option2 == 1:
        valor_dolar = 3964.97
        mensaje = "Pesos colombianos"
        peso_o_dolar(option, mensaje, money, valor_dolar)
  elif option2 == 2:
        valor_dolar = 104.62
        mensaje = "Pesos argentinos"
        peso_o_dolar(option, mensaje, money, valor_dolar)
  elif option2 == 3:
        valor_dolar = 20.62
        mensaje = "Pesos mexicanos"
        peso_o_dolar(option, mensaje, money, valor_dolar)

if __name__ == '__main__':
    run()