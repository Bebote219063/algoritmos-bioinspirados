import random

# ----------------------------
# Datos del problema
# ----------------------------
tareas = ["Clase", "Estudiar", "Inglés", "Descanso"]
horas_disponibles = list(range(8))  # 8 bloques de tiempo

POBLACION_TAM = 20
GENERACIONES = 50
PROB_MUTACION = 0.1

# ----------------------------
# Crear un individuo (cromosoma)
# ----------------------------
def crear_individuo():
    return [random.choice(horas_disponibles) for _ in tareas]

# ----------------------------
# Función fitness
# ----------------------------
def fitness(individuo):
    penalizacion = 0
    
    # Penalizar horarios repetidos (choques)
    penalizacion += len(individuo) - len(set(individuo))
    
    # Penalizar si las horas están muy juntas (cansancio)
    individuo_ordenado = sorted(individuo)
    for i in range(len(individuo_ordenado) - 1):
        if individuo_ordenado[i+1] - individuo_ordenado[i] == 0:
            penalizacion += 1

    return penalizacion  # MENOR es mejor

# ----------------------------
# Selección por torneo
# ----------------------------
def seleccion(poblacion):
    torneo = random.sample(poblacion, 3)
    torneo.sort(key=fitness)
    return torneo[0]

# ----------------------------
# Cruce
# ----------------------------
def cruce(padre1, padre2):
    punto = random.randint(1, len(tareas)-1)
    hijo = padre1[:punto] + padre2[punto:]
    return hijo

# ----------------------------
# Mutación
# ----------------------------
def mutacion(individuo):
    if random.random() < PROB_MUTACION:
        i = random.randint(0, len(tareas)-1)
        individuo[i] = random.choice(horas_disponibles)

# ----------------------------
# Algoritmo Genético
# ----------------------------
poblacion = [crear_individuo() for _ in range(POBLACION_TAM)]

for gen in range(GENERACIONES):
    nueva_poblacion = []
    
    for _ in range(POBLACION_TAM):
        padre1 = seleccion(poblacion)
        padre2 = seleccion(poblacion)
        hijo = cruce(padre1, padre2)
        mutacion(hijo)
        nueva_poblacion.append(hijo)
    
    poblacion = nueva_poblacion

# ----------------------------
# Mejor solución
# ----------------------------
mejor = min(poblacion, key=fitness)

print("Mejor horario encontrado:")
for tarea, hora in zip(tareas, mejor):
    print(f"{tarea}: hora {hora}")
print("Penalización:", fitness(mejor))
