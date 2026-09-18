# Mapa de la Cueva del Wumpus

El agente inicia en la posición `[1,1]` mirando hacia el Este.

```text
                 CUEVA DEL WUMPUS (4x4)

        +--------+--------+--------+--------+
  y=4   |        |        |  ORO   |  PIT   |
        | [1,4]  | [2,4]  | [3,4]  | [4,4]  |
        +--------+--------+--------+--------+
  y=3   |        |        |        | WUMPUS |
        | [1,3]  | [2,3]  | [3,3]  | [4,3]  |
        +--------+--------+--------+--------+
  y=2   |        |  PIT   |        |        |
        | [1,2]  | [2,2]  | [3,2]  | [4,2]  |
        +--------+--------+--------+--------+
  y=1   | AGENTE |        |        |  PIT   |
        |   →    |        |        |        |
        | [1,1]  | [2,1]  | [3,1]  | [4,1]  |
        +--------+--------+--------+--------+

           x=1     x=2     x=3     x=4
```

## Leyenda

- `AGENTE →`: El agente inicia en `[1,1]` mirando hacia el Este.
- `WUMPUS`: Posición del Wumpus `[2,2]`.
- `PIT`: Pozos ubicados en `[2,2]`, `[4,1]` y `[4,4]`.
- `ORO`: Ubicado en `[3,4]`.

## Camino seguro
[1,1] -> [1,2] -> [1,3] -> [1,4] -> [2,4] -> [3,4] ORO
