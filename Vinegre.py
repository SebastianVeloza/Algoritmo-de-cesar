# -*- coding: utf-8 -*-
#Sebastian Veloza
alfabeto = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóú,."

Lindice = dict(zip(alfabeto, range(len(alfabeto))))
indiceL = dict(zip(range(len(alfabeto)), alfabeto))


def cifrado_vinegre(frase, key):
    texto_cifrado = ""
    espacioMensaje = [
        frase[i : i + len(key)] for i in range(0, len(frase), len(key))
    ]

    for espacioD in espacioMensaje:
        i = 0
        for letra in espacioD:
            N = (Lindice[letra] + Lindice[key[i]]) % len(alfabeto)
            texto_cifrado += indiceL[N]
            i += 1

    return texto_cifrado


def decifrar(cipher, key):
    decrypted = ""
    split_encrypted = [
        cipher[i : i + len(key)] for i in range(0, len(cipher), len(key))
    ]

    for espacioD in split_encrypted:
        i = 0
        for letra in espacioD:
            N = (Lindice[letra] - Lindice[key[i]]) % len(alfabeto)
            decrypted += indiceL[N]
            i += 1

    return decrypted


frase = "Holi"
key = "sebas"
mensaje_escriptado = cifrado_vinegre(frase, key)
mensaje_decifrado = decifrar(mensaje_escriptado, key)

print("Original frase: " + frase)
print("Encrypted frase: " + mensaje_escriptado)
print("Decrypted frase: " + mensaje_decifrado)

