# Ejercicio 1 — Comparar BFS, UCS, DFS, DLS e IDS en el mapa de Rumania

Contexto: Se presentan los resultados de ejecutar múltiples algoritmos de búsqueda no informada y de costo uniforme sobre el mapa de Rumania, partiendo de **Zerind** con destino a **Craiova**.

## Subgrafo de la Ruta Encontrada

```text
(Zerind) --75-- (Arad) --140-- (Sibiu) --80-- (Rimnicu Vilcea) --146-- (Craiova)
```

La ruta mostrada corresponde al camino encontrado por **BFS, UCS, DLS con límite 4 e IDS**. Esta ruta tiene una profundidad de **4 carreteras** y un costo total de **441 km**.

## Tabla Comparativa de Algoritmos

| Algoritmo             | Status  | Path                                                            | Depth (roads) | Cost (km) | Expanded |
| :-------------------- | :------ | :-------------------------------------------------------------- | :------------ | :-------- | :------- |
| **BFS**               | success | Zerind → Arad → Sibiu → Rimnicu Vilcea → Craiova                | 4             | 441       | 7        |
| **UCS**               | success | Zerind → Arad → Sibiu → Rimnicu Vilcea → Craiova                | 4             | 441       | 10       |
| **DFS**               | success | Zerind → Arad → Sibiu → Fagaras → Bucharest → Pitesti → Craiova | 6             | 764       | 7        |
| **DLS (`--limit 2`)** | cutoff  | *N/A*                                                           | *N/A*         | *N/A*     | 3        |
| **DLS (`--limit 4`)** | success | Zerind → Arad → Sibiu → Rimnicu Vilcea → Craiova                | 4             | 441       | 6        |
| **IDS**               | success | Zerind → Arad → Sibiu → Rimnicu Vilcea → Craiova                | 4             | 441       | 16       |

## Análisis de Resultados

### 1. ¿BFS encontró el camino con menos carreteras? ¿UCS el de menos km?

Sí. BFS busca encontrar el camino con la menor cantidad de carreteras, mientras que UCS toma en cuenta el costo acumulado de cada carretera para encontrar el camino con menor distancia. En este caso, los dos algoritmos encontraron la misma ruta: `Zerind → Arad → Sibiu → Rimnicu Vilcea → Craiova`. Esta ruta tiene **4 carreteras** y un costo de **441 km**, por lo que en esta ocasión coincidieron tanto el camino con menos carreteras como el de menor costo.

### 2. ¿Por qué DFS puede devolver un camino más largo aunque el grafo sea el mismo?

DFS puede devolver un camino más largo porque su forma de buscar es diferente. En lugar de comparar todas las opciones para encontrar el camino más corto, va avanzando por una rama hasta encontrar una solución. En este caso, DFS encontró la ruta `Zerind → Arad → Sibiu → Fagaras → Bucharest → Pitesti → Craiova`, que tiene **6 carreteras** y un costo de **764 km**. Aunque encontró una solución, esta fue más larga que la encontrada por BFS y UCS. Esto demuestra que DFS no garantiza encontrar el camino con menor cantidad de carreteras o menor costo.

### 3. ¿Con qué `--limit` DLS pasó de cutoff a solución, y cómo se relaciona esto con la profundidad del camino de BFS/IDS?

DLS dio como resultado `cutoff` cuando se utilizó `--limit 2`, porque con ese límite no podía llegar hasta Craiova. Al aumentar el límite a `4`, encontró una solución con una profundidad de **4 carreteras**. Esto coincide con la profundidad encontrada por BFS e IDS. En el caso de IDS, el algoritmo va aumentando el límite poco a poco hasta encontrar una solución, por lo que terminó encontrándola cuando llegó al límite 4. La diferencia es que IDS tuvo que repetir algunas búsquedas y por eso terminó expandiendo más nodos que BFS.

