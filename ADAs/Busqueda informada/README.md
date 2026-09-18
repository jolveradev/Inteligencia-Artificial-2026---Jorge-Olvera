# Ejercicio 1 — Comparar Greedy y A* en el mapa de Rumania

Contexto: Se presentan los resultados de ejecutar los algoritmos de búsqueda informada **Greedy best-first** y **A*** sobre el mapa de Rumania, partiendo de **Zerind** con destino a **Craiova**.

Para esta instancia se utilizó como heurística la **distancia euclidiana hacia Craiova**, calculada a partir de las coordenadas del mapa. Esto se debe a que el destino elegido no es Bucharest, por lo que no se utiliza la tabla de distancias en línea recta de AIMA.

## Subgrafo de la Ruta Encontrada

```text
(Zerind) --75-- (Arad) --140-- (Sibiu) --80-- (Rimnicu Vilcea) --146-- (Craiova)
```

La ruta mostrada corresponde al camino encontrado tanto por **Greedy best-first** como por **A***. Esta ruta tiene una profundidad de **4 carreteras** y un costo total de **441 km**.

Los valores de la heurística para las ciudades de la ruta son:

```text
Zerind          h = 283
Arad            h = 260
Sibiu           h = 175
Rimnicu Vilcea  h = 124
Craiova         h = 0
```

## Tabla Comparativa de Algoritmos

| Algoritmo             | Status  | Path                                             | Depth (roads) | Cost (km) | Expanded | Generated |
| :-------------------- | :------ | :----------------------------------------------- | :------------ | :-------- | :------- | :-------- |
| **Greedy best-first** | success | Zerind → Arad → Sibiu → Rimnicu Vilcea → Craiova | 4             | 441       | 4        | 13        |
| **A***                | success | Zerind → Arad → Sibiu → Rimnicu Vilcea → Craiova | 4             | 441       | 7        | 19        |

**Heurística utilizada en ambos algoritmos:** distancia euclidiana hacia Craiova.

## Valores de `g`, `h` y `f` en el camino

| Ciudad         | `g(n)` | `h(n)` | `f(n) = g(n) + h(n)` |
| :------------- | -----: | -----: | -------------------: |
| Zerind         |      0 |    283 |                  283 |
| Arad           |     75 |    260 |                  335 |
| Sibiu          |    215 |    175 |                  390 |
| Rimnicu Vilcea |    295 |    124 |                  419 |
| Craiova        |    441 |      0 |                  441 |

Como se puede observar, el valor de `f(n)` aumenta a lo largo del camino encontrado:

```text
283 → 335 → 390 → 419 → 441
```

Por lo tanto, en el camino obtenido por A*, `f(n)` no disminuye.

## Análisis de Resultados

### 1. ¿A* encontró el camino de menos km? ¿Greedy coincidió o se desvió?

Sí. A* encontró un camino de **441 km**, que corresponde a la ruta:

`Zerind → Arad → Sibiu → Rimnicu Vilcea → Craiova`.

Greedy también encontró exactamente la misma ruta, con una profundidad de **4 carreteras** y un costo de **441 km**. Por lo tanto, en esta instancia los dos algoritmos coincidieron tanto en el camino como en el costo obtenido.

A* utiliza `f(n) = g(n) + h(n)`, tomando en cuenta tanto el costo acumulado como la estimación del costo restante. La heurística utilizada es admisible, por lo que A* puede encontrar el camino de menor costo bajo las condiciones indicadas para el algoritmo.

### 2. ¿Por qué Greedy puede devolver un camino más caro aunque `h` sea admisible?

Greedy puede devolver un camino más caro porque solamente utiliza el valor de `h(n)` para decidir qué nodo explorar. Es decir, busca avanzar hacia la ciudad que parece estar más cerca del destino, pero no toma en cuenta el costo que ya se ha acumulado para llegar hasta ella.

Por ejemplo, al comenzar en Zerind, sus opciones principales son Arad y Oradea. Arad tiene `h(Arad) = 260`, mientras que Oradea tiene `h(Oradea) = 308`. Por esta razón, Greedy prefiere Arad, ya que tiene un menor valor de `h(n)`. En cambio, A* también considera el costo acumulado. Para Arad se tiene `g(Arad) = 75`, por lo que `f(Arad) = 75 + 260 = 335`.

La heurística sea admisible no significa que Greedy siempre encuentre el camino de menor costo. La admisibilidad de `h(n)` permite que A* utilice esa estimación para buscar un camino óptimo, mientras que Greedy ignora `g(n)` y puede tomar decisiones que posteriormente resulten en un costo mayor.

### 3. En el camino de A*, ¿`f` tiende a no disminuir? ¿Cómo se relaciona con la consistencia?

En el camino encontrado por A*, los valores de `f(n)` fueron:

`283 → 335 → 390 → 419 → 441`.

Como se puede observar, el valor de `f(n)` no disminuye conforme se avanza por la ruta. Esto es consistente con el comportamiento esperado cuando se utiliza una heurística consistente.

En este ejercicio se utilizó la distancia euclidiana hacia **Craiova**, no la tabla AIMA utilizada para el caso de Bucharest. Por lo tanto, la explicación se relaciona con la heurística euclidiana utilizada en esta instancia. Además, en el destino Craiova se tiene `h(Craiova) = 0`, por lo que al llegar al destino `f(n)` coincide con el costo acumulado `g(n)`, que es de **441 km**.

### 4. ¿Por qué A* expandió más nodos que Greedy si encontraron el mismo camino?

Aunque ambos algoritmos encontraron el mismo camino, A* realizó más expansiones. Greedy expandió **4 nodos** y generó **13**, mientras que A* expandió **7 nodos** y generó **19**.

Esto ocurre porque los algoritmos utilizan criterios diferentes para ordenar los nodos. Greedy se enfoca únicamente en `h(n)`, por lo que puede dirigirse rápidamente hacia el destino sin considerar el costo acumulado. A*, por otro lado, utiliza `f(n) = g(n) + h(n)` y evalúa más posibilidades antes de determinar cuál es la mejor opción. Por esta razón, en esta ejecución A* realizó más trabajo, aunque finalmente encontró el mismo camino de 441 km.

