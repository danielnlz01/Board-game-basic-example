import random

tablero=[[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "]]

pos_jugador_1=[0,0]
pos_jugador_2=[0,0]
puntos_jugador_1=0
puntos_jugador_2=0

def pintar_puntos():
  print("Jugador 1: "+str(puntos_jugador_1) +" Jugador 2: "+ str(puntos_jugador_2))
def pintar_tablero():
  for i in range(len(tablero)):
    for j in range(len(tablero[i])):
      print("[",end=" ")
      if pos_jugador_1[0]==j and pos_jugador_1[1]==i:
        print("A",end=" ")
      else:
        print("V",end=" " )
      if pos_jugador_2[0]==j and pos_jugador_2[1]==i:
        print("T",end=" ")
      else:
        print("V",end=" " )   
      print("]",end="")     
    print("")

pintar_tablero()

preguntas_opcion_multiple=[
  ["Como se llama el profesor?",["1) Andrés "," 2) Juan"],1],
  ["Como se apellida el profesor?",["1) López "," 2) Torres"," 3) Pérez"],2]
]

def preguntar(numero_jugador):
  pregunta=random.choice(preguntas_opcion_multiple)
  print(pregunta[0])
  for i in range(len(pregunta[1])):
    print(pregunta[1][i],end=" ")
  respuesta=int(input())
  if respuesta==pregunta[2]:
    if numero_jugador==1:
      global puntos_jugador_1
      puntos_jugador_1+=1
    elif numero_jugador==2:
      global puntos_jugador_2
      puntos_jugador_2+=1



turno =1
while True:
  print("Jugador "+ str(turno)+" es tu turno, estás listo? 1)Si 2)Salir")
  respuesta=input()
  if(respuesta=="2"):
    break
  else:
    if(turno==1):
      numero_dado=random.randint(1,6)
      pos_jugador_1[0]=pos_jugador_1[0]+numero_dado
      print("Tiraste: "+str(numero_dado)+" en el dado")
      if(pos_jugador_1[0]>9):
        pos_jugador_1[0]=pos_jugador_1[0]-10
        pos_jugador_1[1]+=1
    elif(turno==2):
      numero_dado=random.randint(1,6)
      pos_jugador_2[0]=pos_jugador_2[0]+numero_dado
      print("Tiraste: "+str(numero_dado)+" en el dado")
      if(pos_jugador_2[0]>9):
        pos_jugador_2[0]=pos_jugador_2[0]-10
        pos_jugador_2[1]+=1
    pintar_tablero()
    preguntar(turno)
    pintar_puntos()
    if(turno==1):
      turno=2
    else:
      turno=1 

    

