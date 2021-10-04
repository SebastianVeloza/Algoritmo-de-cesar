# -*- coding: utf-8 -*-
alfabeto = ("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

def main():
    frase=input("Mensaje: ")
    myKey="MINOMBREESANTONIOALFONSO"
    accion=input("Mode: ")

    if accion=='encriptar':
        traducido=cifrar_mensaje(myKey,frase)
    elif accion=='descifrar':
        traducido=descifrar_mensaje(myKey,frase)
    print(traducido)

def cifrar_mensaje(clave,mensa):
    return traductor_mensaje(clave,mensa,'encriptar')

def descifrar_mensaje(clave,mensa):
    return traductor_mensaje(clave,mensa,'descifrar')

def traductor_mensaje(clave,mensa,accion):
    traducido=[]
    indice_clave=0
    clave=clave.upper()

    for symbol in mensa:
        num=alfabeto.find(symbol.upper())
        if num!=-1:
            if accion=='encriptar':
                num+=alfabeto.find(clave[indice_clave])
            elif accion=='descifrar':
                num-=alfabeto.find(clave[indice_clave])
            num%=len(alfabeto
        )
            if symbol.isupper():
                traducido.append(alfabeto
            [num])
            elif symbol.islower():
                traducido.append(alfabeto
            [num].lower())
            indice_clave+=1
            if indice_clave==len(clave):
                indice_clave=0

        else:
            traducido.append(symbol)
    return ('').join(traducido)

if __name__ == '__main__':
    main()