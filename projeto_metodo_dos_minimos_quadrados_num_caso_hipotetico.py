import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Importando uma tabela com os dados
data = pd.read_csv('/content/drive/MyDrive/portfolio/ciencia_de_dados/trabalho_mmq/pequena_lanchonete_caso_hipotetico.csv')
print(data)

# Estruturando os somatórios que serão usados para formar os coeficientes "a" e "b"
x=data['receita']
y=data['lucro']
xy=(data['receita'])*(data['lucro'])
xx=(data['receita'])*(data['receita'])
s1=0
s2=0
s3=0
s4=0

#Número de elementos que serão analisados no método dos mínimos quadrados
n=len(data['receita'])
#Utilizando laços de repetição para somar
for i in x:
  s1=s1+i
for j in y:
  s2=s2+j
for k in xy:
  s3=s3+k
for l in xx:
  s4=s4+l    

#Coeficientes oriundos do método dos mínimos quadrados
a= (n*s3-s1*s2)/(n*s4-(s1**2))
b=(s2*s4-s1*s3)/(n*s4-(s1**2))
print('a =',a)
print('b =',b)

#Plotando os pontos num gráfico
plt.scatter(x,y,color="blue")
plt.title("Análise Preditiva")
plt.xlabel("Receita")
plt.ylabel("Lucro")

#Plotando a reta num gráfico
coeficientes=np.polyfit(x,y,1)
funcao=np.poly1d(coeficientes)
intervalo=np.arange(0,100000)
plt.plot(intervalo,funcao(intervalo),color="red")
plt.show()
