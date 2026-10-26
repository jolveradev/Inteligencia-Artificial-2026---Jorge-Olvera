# Reporte — Ejercicio 1: Q-learning en Cliff Walking

**Parámetros:** α = 0.5, γ = 1, ε = 0.1, 500 episodios, tope de 200 pasos, Q inicial = 0, semilla = 0.
**Desempate:** orden fijo N, E, S, W (se elige la primera acción con Q máxima).

## Resultados

Con la Q ya entrenada, la política greedy (ε = 0) hace el camino
`N E E E E E E E E E E E S`: sube a la fila 2, avanza 11 columnas por esa fila y baja a G.
Son **13 pasos** y un **retorno de −13**. Durante el entrenamiento, la media de recompensa
de los últimos 100 episodios fue de aproximadamente **−48.7**, y solo 2 de los 500 episodios
se cortaron por el tope de pasos.

## 1. ¿Por qué el camino de 13 pasos, pegado al acantilado, es óptimo?

Porque es el camino más corto posible que no cae al acantilado. S está en (3, 0) y G en
(3, 11), pero toda la fila 3 entre ambas casillas es acantilado, así que no se puede ir
en línea recta. Hay que subir una fila (1 paso), avanzar 11 columnas hacia el este por la
fila 2 (11 pasos) y bajar a G (1 paso): 1 + 11 + 1 = 13. Como cada paso cuesta −1 y γ = 1,
el retorno es −13. Cualquier otra ruta, por ejemplo por la fila 1, necesita más movimientos
verticales y por eso suma un retorno peor. La ruta de la fila 2 es la que menos pasos usa,
y por eso Q-learning la prefiere: su blanco usa el máximo de Q(s′, ·), o sea que evalúa
el camino como si siempre se actuara de forma greedy, sin penalizar el riesgo de las
acciones exploratorias.

## 2. ¿Por qué la curva de entrenamiento queda por debajo de −13 aunque la política greedy sea óptima?

Porque la curva se mide con la política de comportamiento ε-greedy, no con la greedy.
Con ε = 0.1, en cada paso hay un 10 % de probabilidad de elegir una acción al azar, y
caminando por la fila 2 (pegados al acantilado) una de esas acciones aleatorias puede ser
"sur", que cae al acantilado y da −100. Como el camino tiene unos 13 pasos, es bastante
probable que en algún momento ocurra una caída, y además cada caída regresa al agente a S
y alarga el episodio. Por eso la media de los últimos 100 episodios es de −48.7 y no de
−13. El −13 solo se obtiene en la evaluación con ε = 0, donde ya no hay exploración. Es
decir, la política aprendida es óptima, pero la que se usa para entrenar no lo es.

## 3. En el paso que cae al acantilado, ¿cuál es s′ y por qué no se trata como estado terminal?

Cuando el agente cae, el siguiente estado es **s′ = S = (3, 0)** y la recompensa es
**r = −100**. Por ejemplo, desde (2, 1) con la acción S, el backup queda:

Q((2,1), S) ← Q((2,1), S) + α [ −100 + γ · max_a′ Q(S, a′) − Q((2,1), S) ]

No se trata como terminal porque el episodio **no termina** al caer: el agente reaparece
en S y sigue jugando. Si se pusiera el máximo futuro en 0 (como se hace con G), se
estaría diciendo que después de caer ya no hay más recompensa por obtener, lo cual es falso
porque todavía puede intentar llegar a la meta desde S. Entonces S es un estado normal y su
valor futuro, max Q(S, ·), sí cuenta en el blanco. La penalización de −100 se queda en
Q(s, a) y enseña a evitar esa acción, pero el valor de volver a empezar sigue incluido.
En el código esto se ve porque `paso` devuelve `terminado = False` al caer y
`actualizar_q` solo usa objetivo = r cuando `terminado` es verdadero (es decir, solo en G).