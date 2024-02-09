import random


# link del colab: 
#https://colab.research.google.com/drive/1Z1YsmNdmRALB_cCBe9B5r5p4IoMIiVYJ#scrollTo=1J6nVO3vCV7-&line=3&uniqifier=1


def crear_mazo():
    valores_carta = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    tipos_carta = ["H", "D", "C", "S"]
    mazo = [carta + tipo for carta in valores_carta for tipo in tipos_carta]
    return mazo

def imprimir_mano(mano):
    print(" ".join(mano))

def tiene_full(mano):
    valores = [carta[:-1] for carta in mano]
    conteo_valores = {valor: valores.count(valor) for valor in set(valores)}
    return 3 in conteo_valores.values() and 2 in conteo_valores.values()

def principal():
    mazo = crear_mazo()
    random.shuffle(mazo)
    jugador = random.sample(mazo, 5)
    computadora = random.sample(mazo, 5)

    print("¡Bienvenido a Tres y Dos!")

    while mazo:
        print("Tu mano:", end=" ")
        imprimir_mano(jugador)

        carta_sacada = mazo.pop()
        print(f"Has sacado la carta: {carta_sacada}")
        jugador.append(carta_sacada)

        carta_descartada = input("Elige una carta de tu mano para descartar: ").upper()

        if carta_descartada not in jugador:
            print("Carta no válida. Has perdido tu turno.")
        else:
            jugador.remove(carta_descartada)
            print(f"Has descartado la carta: {carta_descartada}")

            carta_sacada_computadora = mazo.pop()
            computadora.append(carta_sacada_computadora)

            carta_descartada_computadora = random.choice(computadora)
            computadora.remove(carta_descartada_computadora)

            print(f"La computadora ha sacado la carta: {carta_sacada_computadora}")
            print(f"La computadora ha descartado la carta: {carta_descartada_computadora}")

            if tiene_full(jugador) or tiene_full(computadora):
                if tiene_full(jugador):
                    print("¡Felicidades! Tienes 3 y 2. ¡Has ganado!")
                else:
                    print("La computadora tiene un 3 y 2. ¡Has perdido!")
                break
            else:
                print("Ninguno de los jugadores tiene un 3 y 2. ¡El juego continúa!")

    if not mazo:
        print("El mazo se ha agotado. El juego termina en empate.")

if __name__ == "__main__":
    principal()