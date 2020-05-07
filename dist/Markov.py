import numpy as np
import pandas as pd   
import matplotlib.pyplot as plt

def Markov(op):

  if  (op==1):
    def initM():
      k = int(input("Digite el valor de K:"))
      N = int(input("Digite el valor de N:"))
      txt = input("Digite el nombre de el txt: ")

      def hazpar(modelo):
          for i in range(len(modelo)-1):
              yield (modelo[i], modelo[i+1])
            

      
      
      File = open(txt, encoding='utf8').read()

      modelo = File.split()
      check = False
      line = File[:k]
      ju= len(line)
      
      if(line[ju-1:] == " "):
          check=True
          line = line[0:ju-1]
      
      model = dict()
      i = 0
      cadena = " ".join(modelo)
      
      while(i <= len(cadena)-k-1):
          c = cadena[i:i+k]
          s = cadena[i+k]
          if(c in model):
              if(s in model[c]):
                  model[c][s] = int(model[c][s])+1
              else:
                  model[c][s] = 1
          else:
              model[c] = dict()
              model[c][s] = 1
          i+=1

    
      
      pares = hazpar(modelo)

      dictP = {}

      for palabra1, palabra2 in pares:
          if palabra1 in dictP.keys():
              dictP[palabra1].append(palabra2)
          else:
              dictP[palabra1] = [palabra2]
      
      ppalabra = np.random.choice(modelo)

      sw=True
      ll=len(line)

      while sw:
          
          if(line[ll-1] != ppalabra[0]):
              ppalabra = np.random.choice(modelo)  
          else:
              
              sw=False

      cMarkov = [ppalabra]
      n_words = int(N/4)

      for i in range(n_words):
          cMarkov.append(np.random.choice(dictP[cMarkov[-1]]))


      uuu=' '.join(cMarkov)
      ##print("Cadena generada: "+ uuu)
      uuu = uuu[1:len(uuu)]

      if check:
          cunt= line + uuu + " "
          print(cunt[:N])
      else:
          cunt= line + uuu  
          print(cunt[:N])
    initM()

  elif (op == 2):
    
    def calprobs():

      txt = input("Digite el nombre de el txt: ")
      k = int(input("Digite el valor de K:"))
      File = open(txt, encoding='utf8').read()

      modelo = File.split()    
      model = dict()
      i = 0
      cadena = " ".join(modelo)
      
      while(i <= len(cadena)-k-1):
          c = cadena[i:i+k]
          s = cadena[i+k]
          if(c in model):
              if(s in model[c]):
                  model[c][s] = int(model[c][s])+1
              else:
                  model[c][s] = 1
          else:
              model[c] = dict()
              model[c][s] = 1
          i+=1

      
      for value in model:
          print(value,model[value])

      print("Se esta generando el histograma, puede tomar un rato considerando la longitud del txt \n Un poco de paciencia por favor") 
      pd.DataFrame(model).plot(kind='bar')

      plt.show()

    calprobs() 



#1 = Generar Texto
#2 = Histograma
BigFNotation = int(input("1= Generar texto    2= Histograma ------> "))

Markov(BigFNotation)      




