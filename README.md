<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/Licencia-MIT-green?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Estado-Activo-success?style=for-the-badge" alt="Status">
</p>

<h1 align="center">Algoritmos Bioinspirados</h1>

<p align="center">
  <b>Implementación de algoritmos de optimización inspirados en la naturaleza</b>
</p>

<p align="center">
  <i>Proyecto académico que explora técnicas de inteligencia artificial basadas en comportamientos biológicos</i>
</p>

---

## Descripción

Este repositorio contiene implementaciones de **algoritmos bioinspirados**, una rama de la inteligencia artificial que toma inspiración de procesos naturales para resolver problemas complejos de optimización.

Los algoritmos bioinspirados son metaheurísticas que imitan fenómenos biológicos, como la evolución natural y el comportamiento colectivo de colonias de insectos, para encontrar soluciones óptimas o cercanas al óptimo en problemas de alta complejidad computacional.

---

## Algoritmos Implementados

### 1. Algoritmo Genético (GA)

<table>
  <tr>
    <td width="60%">

**Inspiración:** Teoría de la evolución de Darwin

**Aplicación:** Optimización de horarios académicos

**Operadores genéticos:**
- Selección por torneo
- Cruce de un punto
- Mutación aleatoria

**Parámetros:**
| Parámetro | Valor |
|-----------|-------|
| Población | 20 individuos |
| Generaciones | 50 |
| Prob. Mutación | 10% |

</td>
<td width="40%">

```
       [Población Inicial]
              |
              v
    +---[Evaluación Fitness]<--+
    |         |                |
    |         v                |
    |   [Selección]            |
    |         |                |
    |         v                |
    |     [Cruce]              |
    |         |                |
    |         v                |
    +----[Mutación]------------+
              |
              v
       [Mejor Solución]
```

</td>
  </tr>
</table>

---

### 2. Optimización por Colonia de Hormigas (ACO)

<table>
  <tr>
    <td width="60%">

**Inspiración:** Comportamiento de hormigas buscando alimento

**Aplicación:** Problema del Viajante (TSP - Problema NP-Hard)

**Mecanismos clave:**
- Depósito de feromonas
- Evaporación de feromonas
- Selección probabilística

**Parámetros:**
| Parámetro | Valor |
|-----------|-------|
| Hormigas | 5 |
| Iteraciones | 50 |
| Alpha (feromona) | 1.0 |
| Beta (heurística) | 2.0 |
| Evaporación | 0.5 |

</td>
<td width="40%">

```
    Ciudad A -----> Ciudad B
        ^    \___      |
        |        \     |
   [Feromonas]    \    v
        |          \  Ciudad C
        |           \  /
        +--- Ciudad D-+
        
   Las hormigas refuerzan
   los mejores caminos con
   más feromonas
```

</td>
  </tr>
</table>

---

## Estructura del Proyecto

```
algoritmos-bioinspirados/
│
├── ALGORITMO Genetico.py      # Implementación del Algoritmo Genético
├── Ant Colony Optimization.py # Implementación de ACO
└── README.md                  # Documentación del proyecto
```

---

## Requisitos

```bash
# Dependencias necesarias
Python >= 3.8
NumPy >= 1.21.0
```

---

## Instalación y Uso

### Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/algoritmos-bioinspirados.git
cd algoritmos-bioinspirados
```

### Instalar dependencias

```bash
pip install numpy
```

### Ejecutar los algoritmos

```bash
# Algoritmo Genético - Optimización de Horarios
python "ALGORITMO Genetico.py"

# Colonia de Hormigas - Problema del Viajante
python "Ant Colony Optimization.py"
```

---

## Resultados Esperados

### Algoritmo Genético
```
Mejor horario encontrado:
Clase: hora 2
Estudiar: hora 5
Inglés: hora 0
Descanso: hora 7
Penalización: 0
```

### Colonia de Hormigas
```
Mejor ruta encontrada: [0, 1, 3, 2]
Mejor distancia: 7
```

---

## Fundamento Teórico

### Algoritmos Genéticos

Los **Algoritmos Genéticos** son métodos de búsqueda basados en los principios de la selección natural. Utilizan una población de soluciones candidatas que evolucionan a través de generaciones mediante operadores inspirados en la genética:

| Operador | Descripción |
|----------|-------------|
| **Selección** | Las soluciones más aptas tienen mayor probabilidad de reproducirse (evaluadas mediante una función de *Fitness*) |
| **Cruce** | Combina características de dos soluciones "padre" para crear nueva descendencia |
| **Mutación** | Introduce variabilidad aleatoria para explorar nuevas regiones del espacio de búsqueda y evitar óptimos locales |

### Optimización por Colonia de Hormigas (ACO)

El problema del viajante (TSP) es un problema de clasificación **NP-Hard**, lo que significa que el tiempo de cómputo para encontrar la solución exacta crece exponencialmente con el número de ciudades. **ACO** aborda esto simulando el comportamiento de hormigas reales que encuentran caminos óptimos mediante el depósito de **feromonas**.

La probabilidad de que una hormiga *k* se mueva de la ciudad *i* a la ciudad *j* está dada por la siguiente regla de transición:

$$P_{ij}^k = \frac{[\tau_{ij}]^\alpha \cdot [\eta_{ij}]^\beta}{\sum_{l \in N_i^k} [\tau_{il}]^\alpha \cdot [\eta_{il}]^\beta}$$

Donde:
- **τ_ij** es la cantidad de feromona en el camino de *i* a *j*
- **η_ij** es la información heurística (usualmente el inverso de la distancia)
- **α** y **β** son parámetros que controlan la influencia relativa de la feromona y la heurística
- **N_i^k** es el conjunto de ciudades que la hormiga *k* aún no ha visitado

---

## Aplicaciones Reales

| Algoritmo | Aplicaciones |
|-----------|--------------|
| **Genético** | Optimización de horarios, diseño de circuitos |
| **ACO** | Rutas de transporte y logística, enrutamiento en redes de telecomunicaciones, planificación de tareas (*scheduling*) |

---

## Referencias

- **Machine Learning Mastery** (2021). *Simple Genetic Algorithm From Scratch in Python*. Una guía práctica sobre la implementación moderna de algoritmos evolutivos. Recuperado de: https://machinelearningmastery.com/simple-genetic-algorithm-from-scratch-in-python/
- **Dorigo, M.** (2007). *Ant Colony Optimization*. Scholarpedia. (Artículo web revisado por pares, escrito por el creador original del algoritmo explicando su uso computacional moderno). Recuperado de: http://www.scholarpedia.org/article/Ant_colony_optimization
- **Towards Data Science** (2020). *The Traveling Salesman Problem: Exploring the Ant Colony Optimization Algorithm*. Aplicación práctica de metaheurísticas a problemas NP-Hard. Recuperado de: https://towardsdatascience.com/the-traveling-salesman-problem-exploring-the-ant-colony-optimization-algorithm-ba6b91176882
- **GeeksforGeeks** (2023). *Introduction to Genetic Algorithms*. Referencia técnica sobre operadores genéticos y funciones de *fitness*. Recuperado de: https://www.geeksforgeeks.org/genetic-algorithms/

---

## Autor

**Pablo Cesar Lara**

Proyecto desarrollado para la materia de **Algoritmos Bioinspirados**.

---

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo `LICENSE` para más detalles.

---

<p align="center">
  <img src="https://img.shields.io/badge/Hecho%20con-Python-blue?style=flat-square&logo=python" alt="Made with Python">
</p>

<p align="center">
  <sub>Si este proyecto te fue útil, considera darle una estrella en GitHub</sub>
</p>
