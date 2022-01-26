def peso_o_dolar(option, mensaje, valor_dolar):

    money = float(input("Cuanto dinero quieres convertir: "))

    if option == 1:
        convertir_pesos(mensaje, money, valor_dolar)
    elif option == 2:
        convertir_dolares(mensaje, money, valor_dolar)
    else:
        print("Coloca uno de los números indicados")

def convertir_pesos(mensaje, pesos, valor_dolar):
    dolares = str(round(pesos/valor_dolar, 2))
    print(f"Se cambio de {mensaje} a dolares y el resultado fue: $ {dolares} USD")

def convertir_dolares(mensaje, dolares, valor_dolar):
    pesos = str(round(valor_dolar * dolares, 2))
    print(f"se cambio de dolares a {mensaje} el resultado fue: $ {pesos}")


def run():
  menu = """
  1 - Pesos colombianos
  2 - Pesos argentinos
  3 - Pesos mexicanos
  Elige una opción: """

  option = int(input(" 1: Para cambiar pesos a dolares 2: Para cambiar dolares a pesos -> "))
  option2 = int(input(menu))

  if option2 == 1:
        peso_o_dolar(option, "Pesos colombianos", 3964.97)
  elif option2 == 2:
        peso_o_dolar(option, "Pesos argentinos", 104.62)
  elif option2 == 3:
        peso_o_dolar(option, "Pesos mexicanos", 20.62)

if __name__ == '__main__':
    run()