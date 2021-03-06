# Ejemplo de Proof of Work

## Introducción
En este tutorial, intentaremos simular de una manera muy sencilla el concepto de Proof of Work que se utiliza en la red de Bitcoin para generar consenso sobre cuál es el nuevo bloque que va a ser añadido a la cadena. 

Conoceremos los conceptos básicos de las funciones Hash, base fundamental para mantener los datos guardados en los bloques inmutables. 
Tambien analizaremos el algoritmno que se usa para ver cuando un bloque está listo para ser añadido a la cadena o para validar que el bloque que se quiere añadir cumple todos los requisitos.

Para ello, proponemos una pequeña demo en la que los estudiantes tendrán que completar las partes de código que faltan para completar el algoritmo de Proof of Work propuesto.

## Ejercicios propuestos 1 ( obligatorios )

Los estudiantes tendrán que rellenar los componentes que faltan del fichero `minero.py` para generar el algoritmo de proof of work sobre un bloque dado. 

Este algoritmo deberá comprobar que la versión serializada del bloque (`block.get_json()`) tenga un resultado de la función hash `sha256()` con la misma cantidad de ceros por la derecha que la definida en la dificultad del problema. Para ello, el estudiante deberá incrementar el campo `nonce` del objeto `Block` hasta que se cumpla esa condición.

La manera de ejecutar el fichero `minero.py` es la siguiente:
1. En la terminal, dentro de la carpeta que contiene el fichero, se ha de ejecutar el siguiente comando:
`python3 minero.py --input=YYYYYY.json --difficulty=X`
Donde `YYYYY.json`define el fichero bloque que se quiere minar. (La estructura base del bloque se proporciona en el fichero `bloque_base.json`) 
Y donde `X` es la dificultad que le queremos dar al algoritmo de minado. (Numero entero entre 1 y 10)


#### Lista de funciones a completar

1. get_hash()
2. increase_nonce()
3. calculate_valid_block()

## Ejercicios propuestos 2 ( opcionales )

Hasta ahora hemos verificado que el hash del bloque creado está dentro de las restricciones especificadas.
Sin embargo, también hemos de verificar las transacciones dentro del mismo.

Una transacción solo es válida si existen fondos suficientes para llevarla a cabo.
Por ejemplo, si Leo quiere enviar 10 ETH a Mikel, debemos asegurarnos que Leo posee 10 ETH no gastados.

1. En la terminal, dentro de la carpeta que contiene el fichero, se ha de ejecutar el siguiente comando:
`python3 minero.py --input=YYYYYY.json --difficulty=X --balances=XXXXX.json`

Donde `XXXXX.json` define el fichero de donde leer la lista de balances actuales de cada persona.

Ejemplo de balances.json:

```
{
    "Leo": 100000000,
    "Mikel": 10,
    "Tarun": 10
}
```

### Instrucciones

Existe una función que importa los balances de las distintas personas que participarán en la simulación

1. Se debe importar este fichero y pasarselo a las funciones a rellenar
2. La función Transaction.valid() revisará que la operación es correcta.
3. La función Block.check_valid_transations() debera iterar sobre todas las transacciones y revisar cada una de ellas.
4. Por último deberemos revisar que las transacciones son correctas antes de dar el bloque por válido.

#### Lista de funciones a completar

1. Transaction.valid() 
2. Block.check_valid_transactions()
3. Implement transaction check in calculate_valid_block()