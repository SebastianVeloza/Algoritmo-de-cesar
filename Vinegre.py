# -*- coding: utf-8 -*-
#Sebastian Veloza
alfabeto = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóú,. "
#alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
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


def decifrar(cifrado, key):
    texto_decodificado = ""
    encrip = [
        cifrado[i : i + len(key)] for i in range(0, len(cifrado), len(key))
    ]

    for espacioD in encrip:
        i = 0
        for letra in espacioD:
            N = (Lindice[letra] - Lindice[key[i]]) % len(alfabeto)
            texto_decodificado += indiceL[N]
            i += 1

    return texto_decodificado


frase = "El hijo de rana,Rinrín renacuajo salió esta mañana muy tioso, muy majo. Con pantalon corto, corbata a la moda sobrero encintado y chupa de boda." #Ejemplo de clase
key = "ABER"
#frase="PBVRQVICADSKAÑSDETSJPSIEDBGGMPSLRPWRÑPWYEDSDEÑDRDPCRCPQMNPWKUBZVSFNVRDMTIPWUEQVVCBOVNUEDIFQLONMVNUVRSEIKAZYEACEYEDSETFPHLBHGUÑESOMEHLBXVAEEPUÑELISEUEFWHUNMCLPQPMBRRNBPVIÑMTIBVVEÑICANSJAMTJOKMDODSELPWIUFOZMQMVNFOHASESRJWRSFQCOTMVMBJGRPWVSUEXINQRSJEUEMGGRBDGNNILAGSJIDSVSUEEINTGRUEETFGGMPORDFOGTSSTOSEQOÑTGRRYVLPWJIFWXOTGGRPQRRJSKETXRNBLZETGGNEMUOTXJATORVJHRSFHVNUEJIBCHASEHEUEUOTIEFFGYATGGMPIKTBWUEÑENIEEU"
#key="ABER"

mensaje_escriptado = cifrado_vinegre(frase, key)
mensaje_decifrado = decifrar(mensaje_escriptado, key)


print("La frase a cifrar es: " + frase)
print("Frase Cifrada =" + mensaje_escriptado)
print("Frase decifrar=  " + mensaje_decifrado)

