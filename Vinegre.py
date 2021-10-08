# -*- coding: utf-8 -*-
#Sebastian Veloza
#alfabeto = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóú,. "
alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
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
    texto_decodificado = ""
    split_encrypted = [
        cipher[i : i + len(key)] for i in range(0, len(cipher), len(key))
    ]

    for espacioD in split_encrypted:
        i = 0
        for letra in espacioD:
            N = (Lindice[letra] - Lindice[key[i]]) % len(alfabeto)
            texto_decodificado += indiceL[N]
            i += 1

    return texto_decodificado


#frase = "P A R I S  V A U T  B I E N  U N E  M E S S E" #Ejemplo de wikipedia
#key = "L O U P L  O U P L  O U P L  O U P  L O U P L "
frase="PBVRQVICADSKAÑSDETSJPSIEDBGGMPSLRPWRÑPWYEDSDEÑDRDPCRCPQMNPWKUBZVSFNVRDMTIPWUEQVVCBOVNUEDIFQLONMVNUVRSEIKAZYEACEYEDSETFPHLBHGUÑESOMEHLBXVAEEPUÑELISEUEFWHUNMCLPQPMBRRNBPVIÑMTIBVVEÑICANSJAMTJOKMDODSELPWIUFOZMQMVNFOHASESRJWRSFQCOTMVMBJGRPWVSUEXINQRSJEUEMGGRBDGNNILAGSJIDSVSUEEINTGRUEETFGGMPORDFOGTSSTOSEQOÑTGRRYVLPWJIFWXOTGGRPQRRJSKETXRNBLZETGGNEMUOTXJATORVJHRSFHVNUEJIBCHASEHEUEUOTIEFFGYATGGMPIKTBWUEÑENIEEU"
key="ABER"

mensaje_escriptado = cifrado_vinegre(frase, key)
#mensaje_decifrado = decifrar(mensaje_escriptado, key)
mensaje_decifrado = decifrar(frase, key)

print("La frase a cifrar es: " + frase)
print("Frase Cifrada =" + mensaje_escriptado)
print("Frase decifrar=  " + mensaje_decifrado)

