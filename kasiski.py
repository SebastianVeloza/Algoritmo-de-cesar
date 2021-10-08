#data == "PBVRQVICADSKAÑSDETSJPSIEDBGGMPSLRPWRÑPWYEDSDEÑDRDPCRCPQMNPWKUBZVSFNVRDMTIPWUEQVVCBOVNUEDIFQLONMVNUVRSEIKAZYEACEYEDSETFPHLBHGUÑESOMEHLBXVAEEPUÑELISEUEFWHUNMCLPQPMBRRNBPVIÑMTIBVVEÑICANSJAMTJOKMDODSELPWIUFOZMQMVNFOHASESRJWRSFQCOTMVMBJGRPWVSUEXINQRSJEUEMGGRBDGNNILAGSJIDSVSUEEINTGRUEETFGGMPORDFOGTSSTOSEQOÑTGRRYVLPWJIFWXOTGGRPOTTJSKETXRNBLZETGGNEMUOTXJATORVJHRSFHVNUEJIBCHASEHEUEUOTIEFFGYATGGMPIKTBWUEÑENIEEU"
from math import gcd
from functools import reduce
import itertools

#Get encrypted Text and convert to upper
frase = "PBVRQVICADSKAÑSDETSJPSIEDBGGMPSLRPWRÑPWYEDSDEÑDRDPCRCPQMNPWKUBZVSFNVRDMTIPWUEQVVCBOVNUEDIFQLONMVNUVRSEIKAZYEACEYEDSETFPHLBHGUÑESOMEHLBXVAEEPUÑELISEUEFWHUNMCLPQPMBRRNBPVIÑMTIBVVEÑICANSJAMTJOKMDODSELPWIUFOZMQMVNFOHASESRJWRSFQCOTMVMBJGRPWVSUEXINQRSJEUEMGGRBDGNNILAGSJIDSVSUEEINTGRUEETFGGMPORDFOGTSSTOSEQOÑTGRRYVLPWJIFWXOTGGRPQRRJSKETXRNBLZETGGNEMUOTXJATORVJHRSFHVNUEJIBCHASEHEUEUOTIEFFGYATGGMPIKTBWUEÑENIEEU"#input("Input frase: ").upper()
min_letras = 4#int(input("Mininum number of letras per duplicate group: "))
#initialise other variables
tamañoFrase= len(frase)
duplicados = {}
duplicadosU = {}
distancia = []
ggt = 0
alfa = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
letras = []
letrasOrden = []
letrasOrdenCifrada = []
#elimina los espacios de la frase
if " " in frase:
    frase = frase.split(" ")
    frase = "".join(frase)

for letraC in range(0, tamañoFrase+ 1):

    for letraIndice in range(letraC, tamañoFrase- 1):
        
        if not letraIndice - letraC > min_letras - 2:
            continue
        #convierte los indices en subcadenas
        cadenaSub= frase[letraC:letraIndice + 1]
       
        if cadenaSub in frase[letraIndice:]:
            #obtener la distancia entre esta y la siguiente ocurrencia
            distance = frase[letraIndice + 1:].index(cadenaSub) + len(cadenaSub)
            print(distance + (len(cadenaSub)))
            #agrega los duplicados 
            duplicados[cadenaSub] = distance
        
        else:
            break
        print(letraC, cadenaSub)
        #detener el bucle después de pasar por la mitad de la frase
        if letraIndice - letraC >= tamañoFrase/ 2:
            break
#filtra 

for index, duplicate in enumerate(duplicados):
    unico = True
   
    for segundoIndex, second_duplicate in enumerate(duplicados):
        if segundoIndex == index:
            continue
       
        if duplicate in second_duplicate:
            
            unico = False
            break
    if unico:
        
        duplicadosU[duplicate] = duplicados[duplicate]
        #guarda la distancia
        distancia.append(duplicados[duplicate])

print(duplicados)
print(duplicadosU)
ggt = reduce(gcd, distancia)
print(ggt)

letraIndice = {}

for i in range(0, ggt):
    index = i
    end = False
    while not end:
        # agregar al contador si letra en letra
        if frase[index] in letraIndice:
            letraIndice[frase[index]] = letraIndice[frase[index]] + 1
        # poner el contador a 1
        else:
            letraIndice[frase[index]] = 1
        # salto
        index += ggt
        
        if index >= len(frase):
            end = True
    #añadir letra Indice a las letras generales
    letras.append(letraIndice)
    #reinicia
    letraIndice = {}
for letra in letras:
    print(letra)
    #Ordena las letras
    letrasOrden.append(sorted(letra, key=letra.get, reverse=True)[:4])
    print("\n")
print(letrasOrden)
#iterar sobre las letrasOrden
for letras in letrasOrden:
    letraCifrada = []
    #iterar sobre la matriz actual letras
    for letra in letras:
        #obtener el índice alfabético si la letra actual
        letraIndice = alfa.index(letra.upper())
        #Obtiene el indice 0
        a_index = alfa.index("A")
        #ver el desplazamiento entre la letra actual y la letra a
        nuevoIndice = letraIndice - a_index
        if nuevoIndice >= 0:
            #ess el índice de la letra con la que se cifró la letra
            letraCifrada.append(alfa[nuevoIndice])
        else:
            #indice inverso
            letraCifrada.append(alfa[len(alfa) + nuevoIndice])
    letrasOrdenCifrada.append(letraCifrada)
print(letrasOrdenCifrada)
#crea todas las combinaciones de palabras
posibilidades = list(itertools.product(*letrasOrdenCifrada))
#Muestra las primeras 50 
for index,palabra in enumerate(posibilidades):
    if index > 50:
        break
    print("".join(palabra))
