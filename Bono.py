import math
import numpy as np
Digitos = ["0","1","2"]


def base_numero(numero, base):
  a = 0
  b = ''
  while True:
    a = numero%base
    b = str(a) + b
    numero = numero//base
    if numero == 0:
      break

  sol = np.zeros(len(b))
  for i in range(0,len(b)):
    sol[i] = int(b[i])
  return sol



def generarCadenaI(digitos,n,iteracion):
  if(0<=iteracion and iteracion < len(digitos)**n):
    contadores = []
    for i in range(0,n):
      contadores.append(0)
    arreglo = base_numero(iteracion,len(digitos))
    dif = n - len(arreglo)
    cad = ""
    for i in range(0,dif):
      cad = cad + "0"
    for i in arreglo:
      cad = cad+str(int(i))
    return cad  
  else:
    return "Iteracion no valida"

digitos = []
op = 3
while(op==3):
  print("¿Quiere recoger los caracteres de manera manual o por medio de un txt?")
  op = int(input("Digite 1 o 2 respectivamente: "))

  if (op==1):
      while(True):
        aux = int(input("Digite un caracter: "))
        digitos.append(aux)
        print("Desea insertar mas caracteres?")
        op = int(input("1. si 0. no "))
        if(not(op == 1)):
            break
  else:
        print("INFORMACION DE FORMATO DE TXT:","\n","El documento txt tiene que tener solo los numeros a ingresar separados por y unicamente espacio,\n Ejemplo: 5 8 9 1, a continuacion escriba el nombre del documento txt incluyendo su terminacion en .txt")
        Txt = input("Digite el nombre del texto: ")
        File = open(Txt, "r").read()
        digitos = File.split()
        digitos = list(digitos)
        
digitos.sort() 
for i in range(0, len(digitos)): 
    digitos[i] = int(digitos[i])
print(digitos)
        

    

##esta parte de abajo dejala asi

iteracion = int(input("Digite la iteracion que desea ver: "))   
n = int(input("Digite el tamaño de la cadena: "))

print(generarCadenaI(digitos,n,iteracion))