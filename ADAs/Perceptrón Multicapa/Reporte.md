# Reporte

---

### 1. ¿Bajar más el error al añadir dos capas, o se estancó / empeoró? ¿Igual en NumPy y en Keras?
Al incorporar dos capas adicionales y ejecutar el entrenamiento durante 500 épocas con una tasa de aprendizaje de 0.03, la red profunda no logra mejorar su desempeño. El error se estanca de forma prematura en un valor elevado (o línea plana), impidiendo la convergencia del modelo. Este estancamiento ocurre de manera equivalente tanto en la implementación en NumPy como en Keras, lo que evidencia una limitación matemática de la arquitectura profunda bajo estas condiciones y no un problema del marco de desarrollo.

---

### 2. ¿Las curvas de la notebook 01 y de Keras se parecen con la misma topología? Si no, ¿qué diferencias de implementación podrían explicarlo (orden de los datos, inicialización, vectorización, etc.)?
Aunque ambas redes quedan estancadas, las curvas de error difieren en su trayectoria debido a la implementación subyacente:
* **Inicialización de pesos:** En NumPy se emplearon valores aleatorios simples en el intervalo [-0.5, 0.5], lo que propicia una saturación temprana. Keras aplica por defecto inicializaciones optimizadas (como Xavier/Glorot), atenuando este efecto inicial.
* **Procesamiento de datos:** El script de NumPy actualiza los pesos muestra por muestra en un orden secuencial fijo. En contraste, Keras agrupa los datos en *mini-batches* de 32 e introduce un barajado aleatorio por época, generando curvas de descenso significativamente menos caóticas.

---

### 3. Con sigmoides apiladas y MSE, ¿tiene sentido que una red **más profunda** no aprenda mejor en Iris? Relaciónalo con lo que viste en las gráficas.
El fallo de la red más profunda al utilizar activaciones sigmoides y MSE se debe al problema del desvanecimiento del gradiente. Dado que la derivada máxima de la función sigmoide es de 0.25, la aplicación de la regla de la cadena en la retropropagación implica la multiplicación acumulativa de estos factores 0.25 x 0.25 x 0.25, reduciendo exponencialmente el gradiente hacia las primeras capas. En consecuencia, los pesos iniciales apenas sufren actualización, congelando la red. Adicionalmente, el dataset Iris es simple y casi separable linealmente, por lo que una arquitectura de cuatro capas resulta sobrecompleja e introduce zonas de gradiente nulo en la superficie de pérdida.
