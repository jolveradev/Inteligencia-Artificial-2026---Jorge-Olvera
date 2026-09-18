# Ejercicio 2 — Descripción PEAS de agentes inteligentes

## 1. Asistente virtual de voz

* **Performance:** responder correctamente a las solicitudes del usuario, minimizar el tiempo de respuesta, reconocer el habla con precisión, ejecutar las acciones solicitadas y mantener un alto nivel de satisfacción del usuario. También se busca reducir errores al interpretar órdenes y evitar acciones no autorizadas.

* **Environment:** hogar u otros espacios donde se encuentre el altavoz inteligente, con usuarios que realizan consultas o dan instrucciones. Es un entorno **parcialmente observable**, porque el agente no conoce todo lo que ocurre alrededor; **estocástico**, debido a variaciones en el lenguaje y comportamiento de los usuarios; **secuencial**, porque una respuesta puede afectar las siguientes interacciones; **dinámico**, porque las condiciones y solicitudes cambian constantemente; y principalmente **continuo**, debido al audio y al tiempo.

* **Actuators:** reproducir respuestas mediante el altavoz, controlar dispositivos inteligentes, reproducir música, crear recordatorios, enviar mensajes, realizar búsquedas y proporcionar información al usuario.

* **Sensors:** micrófono para captar la voz, reconocimiento de palabras de activación, historial de interacciones, información proporcionada por el usuario y datos obtenidos mediante servicios o APIs externas.

> **Justificación:** El entorno es parcialmente observable porque el asistente solo recibe la información que puede captar mediante sus sensores y servicios conectados. Es secuencial y dinámico porque las conversaciones y acciones anteriores influyen en las siguientes decisiones.

---

## 2. Robot aspirador doméstico

* **Performance:** maximizar la superficie limpiada, reducir la cantidad de suciedad restante, evitar choques y caídas, completar la limpieza en el menor tiempo posible y utilizar eficientemente la batería.

* **Environment:** pisos de una vivienda con muebles, paredes, escaleras, personas, mascotas y diferentes tipos de suciedad. Es un entorno **parcialmente observable**, porque el robot no puede conocer todo el espacio al mismo tiempo; **estocástico**, debido a obstáculos y situaciones que pueden cambiar inesperadamente; **secuencial**, porque cada movimiento afecta las decisiones posteriores; **dinámico**, por el movimiento de personas y mascotas; y **continuo**, debido al movimiento físico del robot.

* **Actuators:** motores de las ruedas para desplazarse, sistema de aspiración, cepillos giratorios y mecanismos para cambiar de dirección o regresar a la estación de carga.

* **Sensors:** sensores de proximidad y obstáculos, sensores de caída, sensores de suciedad, cámaras o sensores LiDAR en modelos que los incorporan, sensores de posición y sensores de batería.

> **Justificación:** El robot no observa toda la vivienda de manera simultánea y debe construir una representación del espacio a medida que se desplaza. Además, las personas, mascotas y objetos pueden cambiar de posición, haciendo que el entorno sea dinámico y parcialmente observable.

---

## 3. Sistema de recomendación de streaming

* **Performance:** aumentar la relevancia de las recomendaciones, lograr que el usuario encuentre contenido de su interés, incrementar la satisfacción y el tiempo de interacción y reducir la cantidad de recomendaciones ignoradas o abandonadas.

* **Environment:** plataforma de streaming con películas, series o canciones y usuarios con diferentes gustos y hábitos. Es un entorno **parcialmente observable**, porque el sistema no conoce directamente las preferencias reales del usuario; **estocástico**, porque no puede determinar con certeza cómo reaccionará ante una recomendación; **secuencial**, porque las interacciones anteriores influyen en recomendaciones futuras; **dinámico**, porque cambian el catálogo y los intereses de los usuarios; y principalmente **discreto**, porque las acciones y contenidos se representan mediante elementos diferenciados.

* **Actuators:** mostrar recomendaciones, ordenar o seleccionar contenido en la interfaz, generar listas personalizadas, reproducir contenido recomendado y modificar las recomendaciones futuras de acuerdo con las interacciones.

* **Sensors:** historial de reproducción, búsquedas, contenido pausado o terminado, calificaciones, géneros consultados, tiempo de reproducción, listas creadas y datos de interacción con la plataforma.

> **Justificación:** El sistema no puede observar directamente si una persona realmente disfrutará de una película, por lo que debe inferir sus preferencias a partir de sus acciones. Además, las recomendaciones forman una secuencia, ya que cada interacción proporciona nueva información para las siguientes decisiones.

---

## 4. Vehículo autónomo en ciudad

* **Performance:** transportar a los pasajeros de forma segura y eficiente, respetar las normas de tránsito, llegar al destino en un tiempo razonable, reducir el consumo de energía o combustible y evitar accidentes, colisiones y maniobras innecesarias.

* **Environment:** calles y avenidas urbanas con automóviles, motocicletas, bicicletas, peatones, semáforos, señales, construcciones y condiciones variables del clima. Es un entorno **parcialmente observable**, porque existen zonas fuera del alcance de los sensores; **estocástico**, debido al comportamiento impredecible de otros conductores y peatones; **secuencial**, porque cada decisión de conducción afecta las siguientes; **dinámico**, porque los elementos del tráfico se encuentran en movimiento; y **continuo**, debido al movimiento del vehículo y de los demás objetos.

* **Actuators:** controlar el volante, acelerador y freno, cambiar de velocidad, activar direccionales, luces y otros sistemas del vehículo.

* **Sensors:** cámaras, LiDAR, radar, GPS, sensores ultrasónicos, sensores de velocidad y sensores que permiten conocer el estado del propio vehículo.

> **Justificación:** Es un entorno altamente dinámico porque vehículos y peatones cambian continuamente de posición. También es estocástico, ya que el agente no puede conocer con certeza las acciones futuras de otros participantes del tráfico.

---

## 5. Agente de trading algorítmico en bolsa

* **Performance:** maximizar el rendimiento de las operaciones ajustado al riesgo, reducir pérdidas, controlar los costos y comisiones de transacción, ejecutar órdenes en el momento adecuado y respetar los límites de riesgo establecidos.

* **Environment:** mercados financieros con acciones, compradores, vendedores, instituciones financieras y otros algoritmos de negociación. Es un entorno **parcialmente observable**, porque el agente no conoce todas las órdenes ni las decisiones de los participantes; **estocástico**, debido a la incertidumbre de los precios; **secuencial**, porque cada operación afecta el capital disponible y las decisiones posteriores; **dinámico**, porque los precios cambian constantemente; y **continuo**, debido a la evolución temporal de precios y cantidades negociadas.

* **Actuators:** enviar órdenes de compra y venta, cancelar o modificar órdenes, establecer límites de precio y cantidad y administrar la distribución del capital disponible.

* **Sensors:** cotizaciones en tiempo real, volumen de operaciones, historial de precios, libro de órdenes cuando está disponible, noticias o indicadores obtenidos mediante APIs y estado actual de la cartera.

> **Justificación:** El agente no tiene acceso a toda la información que determina el comportamiento del mercado y, además, las decisiones de otros participantes son inciertas. Por ello, el entorno es parcialmente observable y estocástico, mientras que las decisiones son secuenciales porque cada operación modifica el estado de la cartera.

---

## 6. Sistema de diagnóstico médico asistido por IA

* **Performance:** identificar correctamente posibles enfermedades o anomalías, mantener una alta sensibilidad y especificidad, reducir falsos positivos y falsos negativos, proporcionar resultados en un tiempo adecuado y presentar información útil para apoyar la decisión del médico.

* **Environment:** hospitales, clínicas o consultorios donde se analizan pacientes, síntomas, antecedentes y estudios clínicos. Es un entorno **parcialmente observable**, porque el sistema no puede observar directamente todo el estado de salud del paciente; **estocástico**, debido a la variabilidad de las enfermedades y respuestas de los pacientes; **secuencial**, porque nuevos estudios y síntomas pueden modificar el diagnóstico; **dinámico**, porque el estado del paciente puede cambiar; y puede involucrar información **discreta y continua**, como resultados de laboratorio, imágenes y signos vitales.

* **Actuators:** generar posibles diagnósticos, señalar anomalías en imágenes, calcular niveles de riesgo, solicitar o sugerir estudios adicionales cuando el sistema esté diseñado para ello y mostrar información de apoyo al médico.

* **Sensors:** síntomas registrados, historial médico, resultados de laboratorio, signos vitales, imágenes de radiografías, tomografías o resonancias y otros datos clínicos disponibles.

> **Justificación:** El sistema solo puede trabajar con los datos clínicos que recibe y no puede observar directamente todas las condiciones del paciente. Además, el diagnóstico puede cambiar conforme aparecen nuevos resultados, por lo que la tarea es parcialmente observable y secuencial.

---

## 7. Dron de inspección de infraestructura

* **Performance:** detectar correctamente grietas, corrosión, fugas u otros daños, cubrir las zonas de inspección, obtener imágenes de suficiente calidad, minimizar el tiempo de vuelo y consumo de batería y evitar colisiones con la infraestructura.

* **Environment:** puentes, tuberías, torres, líneas eléctricas u otras estructuras, incluyendo obstáculos, viento, cambios de iluminación y zonas de difícil acceso. Es un entorno **parcialmente observable**, porque existen áreas ocultas o fuera del campo de los sensores; **estocástico**, debido principalmente a condiciones ambientales como viento y cambios de iluminación; **secuencial**, porque cada movimiento determina la siguiente zona que puede inspeccionar; **dinámico**, debido al viento y otros cambios ambientales; y **continuo**, por el movimiento tridimensional del dron.

* **Actuators:** motores y hélices para desplazarse, modificar altura y orientación, controlar la velocidad y activar mecanismos de captura o iluminación cuando estén disponibles.

* **Sensors:** cámaras RGB, cámaras térmicas, LiDAR, GPS, IMU, sensores de distancia, sensores de altitud y sensores relacionados con el estado de la batería.

> **Justificación:** El dron debe desplazarse por un espacio tridimensional mientras recopila información sobre zonas que pueden ser difíciles de observar. Las condiciones del viento y otros factores ambientales hacen que el entorno sea dinámico y estocástico.

---

## 8. Agente jugador de ajedrez

* **Performance:** ganar la partida, maximizar la ventaja de posición, evitar perder piezas innecesariamente, utilizar eficientemente el tiempo disponible y seleccionar movimientos que aumenten las posibilidades de obtener un resultado favorable.

* **Environment:** tablero de ajedrez, piezas propias y del oponente, reglas oficiales y reloj de la partida. Es un entorno **totalmente observable**, porque ambos jugadores pueden observar el estado completo del tablero; **determinista**, porque un movimiento produce un resultado definido de acuerdo con las reglas; **secuencial**, porque cada movimiento depende de los movimientos anteriores; **estático** entre movimientos, aunque el reloj puede introducir un elemento dinámico; y **discreto**, porque las posiciones y movimientos posibles están definidos en términos discretos.

* **Actuators:** seleccionar y realizar movimientos de las piezas, incluyendo movimientos normales, capturas, enroque, promoción y otros movimientos permitidos por las reglas.

* **Sensors:** estado completo del tablero, posición de todas las piezas, movimientos realizados previamente, turno actual, reloj de la partida y reglas disponibles para determinar movimientos legales.

> **Justificación:** A diferencia de varias aplicaciones anteriores, el tablero es completamente visible para el agente y las reglas determinan de manera precisa el resultado de cada movimiento. Sin embargo, la tarea es secuencial porque cada jugada modifica el estado del tablero y condiciona las decisiones posteriores.

---

