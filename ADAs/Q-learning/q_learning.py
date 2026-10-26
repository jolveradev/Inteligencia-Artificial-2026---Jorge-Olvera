
import random
import csv


# 1. Parámetros del experimento
ALPHA = 0.5
GAMMA = 1.0
EPSILON = 0.1
EPISODIOS = 500
MAX_PASOS = 200
SEMILLA = 0

random.seed(SEMILLA)

FILAS = 4
COLUMNAS = 12

INICIO = (3, 0)
META = (3, 11)

ACCIONES = ["N", "E", "S", "W"] # orden fijo, tambien el de desempate

MOVIMIENTOS = {
    "N": (-1, 0),
    "E": (0, 1),
    "S": (1, 0),
    "W": (0, -1),
}



# 2. Tabla Q 
Q = {
    (fila, columna): {accion: 0.0 for accion in ACCIONES}
    for fila in range(FILAS)
    for columna in range(COLUMNAS)
    if (fila, columna) != META
}



# 3. Entorno
def paso(estado, accion):
    fila, columna = estado
    df, dc = MOVIMIENTOS[accion]

    nueva_fila = fila + df
    nueva_columna = columna + dc

    if not (0 <= nueva_fila < FILAS
            and 0 <= nueva_columna < COLUMNAS):
        nueva_fila, nueva_columna = fila, columna

    siguiente = (nueva_fila, nueva_columna)

    # Penalización y regreso a S
    if nueva_fila == 3 and 1 <= nueva_columna <= 10:
        return INICIO, -100, False

    recompensa = -1
    terminado = (siguiente == META)

    return siguiente, recompensa, terminado


# 4. Política epsilon-greedy
def elegir_accion(estado, epsilon):
    # elegir una acción al azar
    if random.random() < epsilon:
        return random.choice(ACCIONES)

    # escoger la primera acción máxima
    valores = Q[estado]
    mejor_valor = max(valores.values())

    for accion in ACCIONES:
        if valores[accion] == mejor_valor:
            return accion


# 5. Actualización Q-learning
def actualizar_q(estado, accion, recompensa,
                 siguiente, terminado):

    if terminado:
        objetivo = recompensa
    else:
        objetivo = (
            recompensa
            + GAMMA * max(Q[siguiente].values())
        )

    valor_actual = Q[estado][accion]

    Q[estado][accion] = valor_actual + ALPHA * (
        objetivo - valor_actual
    )


# 6. Entrenamiento
recompensas_episodios = []
pasos_episodios = []

for episodio in range(EPISODIOS):
    estado = INICIO
    recompensa_total = 0
    pasos_totales = 0

    for _ in range(MAX_PASOS):
        accion = elegir_accion(estado, EPSILON)

        siguiente, recompensa, terminado = paso(
            estado, accion
        )

        # Se actualiza usando la acción realmente ejecutada
        actualizar_q(
            estado, accion, recompensa,
            siguiente, terminado
        )

        recompensa_total += recompensa
        pasos_totales += 1
        estado = siguiente

        if terminado:
            break

    recompensas_episodios.append(recompensa_total)
    pasos_episodios.append(pasos_totales)

# Guardar las recompensas de los 500 episodios
with open("recompensas.csv", "w", newline="",
          encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["episodio", "recompensa", "pasos"])

    for i, (recompensa, pasos) in enumerate(
        zip(recompensas_episodios, pasos_episodios), start=1
    ):
        escritor.writerow([i, recompensa, pasos])



# 7. Evaluación greedy
estado = INICIO
camino = [estado]
acciones_evaluacion = []
retorno = 0
terminado = False

for _ in range(MAX_PASOS):
    
    accion = elegir_accion(estado, epsilon=0.0)

    siguiente, recompensa, terminado = paso(estado, accion)

    acciones_evaluacion.append(accion)
    camino.append(siguiente)
    retorno += recompensa
    estado = siguiente

    if terminado:
        break

print("\n--- RESULTADOS ---")
print("Semilla:", SEMILLA)
print("Episodios de entrenamiento:", EPISODIOS)
print("Acciones greedy:", " -> ".join(acciones_evaluacion))
print("Camino de estados:", camino)
print("Pasos greedy:", len(acciones_evaluacion))
print("Retorno greedy:", retorno)
print("¿Meta?:", terminado)


# 8. Mostrar la política greedy
FLECHAS = {
    "N": "^",
    "E": ">",
    "S": "v",
    "W": "<",
}

print("\n--- Politica Greedy ---")

for fila in range(FILAS):
    celdas = []

    for columna in range(COLUMNAS):
        estado = (fila, columna)

        if estado == INICIO:
            simbolo = "S"
        elif estado == META:
            simbolo = "G"
        elif fila == 3 and 1 <= columna <= 10:
            simbolo = "C"
        else:
            valores = Q[estado]
            mejor = max(valores.values())
            accion = next(
                a for a in ACCIONES if valores[a] == mejor
            )
            simbolo = FLECHAS[accion]

        celdas.append(simbolo)

    print(" ".join(celdas))



# 9. Gráfica

import matplotlib.pyplot as plt

ventana = 10
medias_moviles = [
    sum(recompensas_episodios[i - ventana + 1:i + 1])
    / ventana
    for i in range(ventana - 1, EPISODIOS)]

episodios_media = list(
        range(ventana, EPISODIOS + 1))

plt.figure(figsize=(11, 5))

plt.plot(
    range(1, EPISODIOS + 1),
    recompensas_episodios,
    alpha=0.3,
    label="Recompensa por episodio")

plt.plot(
        episodios_media,
        medias_moviles,
        label="Media móvil (10 episodios)")

plt.axhline(
    y=-13, linestyle="--",
    label="Retorno óptimo greedy (-13)")

plt.xlabel("Episodio")
plt.ylabel("Recompensa acumulada")
plt.title("Q-learning en Cliff Walking")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("recompensas.png", dpi=150)
plt.show()


