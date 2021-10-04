#Sebastian Veloza
# -*- coding: utf-8 -*-


alfabeto = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóú,."
print(len(alfabeto))
def cifrado_cesar(alfabeto,n,texto):
    texto_cifrado = ""
    for letra in texto:
        if letra in alfabeto:
            indiceA = alfabeto.index(letra)
            indiceC =  indiceA + n
            if indiceC > 60:
                indiceC = (indiceA + n) % len(alfabeto)
            texto_cifrado += alfabeto[indiceC]
        else:
            texto_cifrado += letra
    return texto_cifrado

def decodificar(alfabeto,n,texto):
    texto_decodificado = ""
    for letra in texto:
        if letra in alfabeto:
            indiceC = alfabeto.index(letra)
            indiceO = indiceC - n
            if indiceO <0 :
               indiceO= (indiceC+len(alfabeto)-n)%len(alfabeto)
            texto_decodificado += alfabeto[indiceO]
        else:
            texto_decodificado += letra
    return texto_decodificado


frase = "El hijo de rana,Rinrín renacuajo salió esta mañana muy tioso, muy majo. Con pantalon corto, corbata a la moda sobrero encintado y chupa de boda."
frase_cifrada = cifrado_cesar(alfabeto,3,frase)
print("La frase a cifrar es: "+frase)
print("Frase Cifrada = " + frase_cifrada)
frase_decodificada = decodificar(alfabeto,3,frase_cifrada)
print("frase decifrar= " +frase_decodificada)
