def calculadora():
    main1()

def main():
    n1=int(input("Ingrese primer numero: "))
    calculo= str(input("Ingrese el calculo: "))
    n2=int(input("Ingrese el segundo numero: "))
    print(hacer_calculo(n1,calculo,n2))

def hacer_calculo(n1,calculo,n2):
    resultado=None
    if calculo=="suma":
        resultado=n1+n2
    elif calculo=="resta":
        resultado=n1-n2
    elif calculo=="multiplicacion":
        resultado=n1*n2
    elif calculo=="division":
        resultado=n1/n2
    else:
        raise Exception(f"{calculo} no es un calculo valido. Intente otra vez")
    return resultado
#######################################################################################################################

def main1():
    n1=int(input("Ingrese primer numero: "))
    n2=int(input("Ingrese el segundo numero: "))
    operador=int(input("""
          Seleccionar operador:
          1)Suma
          2)Resta
          3)Multiplicacion
          4)Division
            """))
    print(hacer_calculo1(n1,operador,n2))   

def hacer_calculo1(n1,operador,n2):
    resultado=None
    if operador==1:
        resultado=n1+n2
    elif operador==2:
        resultado=n1-n2
    elif operador==3:
        resultado=n1*n2
    elif operador==4:
        resultado=n1/n2
    return resultado 
    