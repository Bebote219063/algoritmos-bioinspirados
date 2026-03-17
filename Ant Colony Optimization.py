import random
import numpy as np

# ----------------------------
# PARAMETROS DEL ALGORITMO
# ----------------------------

NUM_HORMIGAS = 5       # Number of ants (solutions per iteration)
ITERACIONES = 50       # Number of iterations
ALPHA = 1              # Importance of pheromone
BETA = 2               # Importance of heuristic (distance)
EVAPORACION = 0.5      # Pheromone evaporation rate

# ----------------------------
# MATRIZ DE DISTANCIAS
# ----------------------------
# Represents distances between cities

distancias = np.array([
    [0, 2, 2, 5],
    [2, 0, 3, 4],
    [2, 3, 0, 1],
    [5, 4, 1, 0]
])

NUM_CIUDADES = len(distancias)

# ----------------------------
# MATRIZ DE FEROMONAS
# ----------------------------
# Initially all paths have equal pheromone

feromonas = np.ones((NUM_CIUDADES, NUM_CIUDADES))

# ----------------------------
# SELECCIONAR SIGUIENTE CIUDAD
# ----------------------------
def seleccionar_siguiente(ciudad_actual, visitadas):
    """
    Selects the next city based on probability.
    Combines pheromone and distance.
    """

    probabilidades = []

    for j in range(NUM_CIUDADES):
        if j not in visitadas:
            tau = feromonas[ciudad_actual][j] ** ALPHA   # pheromone
            eta = (1 / distancias[ciudad_actual][j]) ** BETA  # heuristic
            probabilidades.append(tau * eta)
        else:
            probabilidades.append(0)

    total = sum(probabilidades)
    probabilidades = [p / total for p in probabilidades]

    return np.random.choice(range(NUM_CIUDADES), p=probabilidades)

# ----------------------------
# CONSTRUIR RUTA
# ----------------------------
def construir_ruta():
    """
    Each ant builds a solution step by step.
    """

    ruta = [random.randint(0, NUM_CIUDADES - 1)]

    while len(ruta) < NUM_CIUDADES:
        siguiente = seleccionar_siguiente(ruta[-1], ruta)
        ruta.append(siguiente)

    return ruta

# ----------------------------
# CALCULAR DISTANCIA
# ----------------------------
def distancia_ruta(ruta):
    """
    Calculates total distance of a route.
    """

    total = 0
    for i in range(len(ruta) - 1):
        total += distancias[ruta[i]][ruta[i+1]]
    
    return total

# ----------------------------
# ALGORITMO PRINCIPAL ACO
# ----------------------------

mejor_ruta = None
mejor_distancia = float("inf")

for iteracion in range(ITERACIONES):

    todas_rutas = []

    # Each ant builds a route
    for _ in range(NUM_HORMIGAS):
        ruta = construir_ruta()
        dist = distancia_ruta(ruta)
        todas_rutas.append((ruta, dist))

    # ----------------------------
    # EVAPORACION
    # ----------------------------
    # Reduce pheromone to avoid stagnation
    feromonas *= (1 - EVAPORACION)

    # ----------------------------
    # ACTUALIZAR FEROMONAS
    # ----------------------------
    # Better routes deposit more pheromone
    for ruta, dist in todas_rutas:
        for i in range(len(ruta) - 1):
            feromonas[ruta[i]][ruta[i+1]] += 1 / dist

    # ----------------------------
    # GUARDAR MEJOR SOLUCION
    # ----------------------------
    for ruta, dist in todas_rutas:
        if dist < mejor_distancia:
            mejor_ruta = ruta
            mejor_distancia = dist

# ----------------------------
# CONVERTIR A INT (IMPORTANTE)
# ----------------------------
# Fix numpy int type for clean output

mejor_ruta = [int(x) for x in mejor_ruta]

# ----------------------------
# RESULTADO FINAL
# ----------------------------

print("Mejor ruta encontrada:", mejor_ruta)
print("Mejor distancia:", mejor_distancia)