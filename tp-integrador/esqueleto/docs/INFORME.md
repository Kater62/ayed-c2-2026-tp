# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema: Biblioteca Musical
- Por qué lo eligieron (5–8 líneas):
Elegimos este tema ya que nos parecio intuitivo y familiar por las apps de musica de hoy en dia, ademas de por lo menos yo soy bastante 
fan de la musica.

## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.x

Ítem del catálogo: Nuestro ítem es un diccionario que representa una canción.
Mutables: La lista principal (CATALOGO) y los diccionarios de cada canción.
Inmutables: Los textos (como los nombres) y los números (como los ID) de las canciones.

```text
(pueden pegar un diagrama ASCII o una lista de clases)
```

## 3. Recursión (E2)

- Función: versiones (id):

- Caso base: Ocurre cuando nuestro ciclo for recorre todo el catalogo y no encuentra ninguna cancion cuyo proviene_de es igual al id buscado, al no encontrarlo termina la funcion

- Caso recursivo: Ocurre cuando el if encuentra una cancion cuyo proviene_de es igual al id buscado, la imprime y vuelve a llamarse pasandole el id de la nueva version encontrada

- Traza de un ejemplo real del dataset:
 Llamada 1 : versiones (1) el for recorre el catalogo y encuentra el cover de Nightwish (ID5) porque su proviene_de es (1) lo imprime y ejecuta el caso recursivo llamando a versiones (5)
 Llamada 2 : versiones (5) el for recorre el catalogo y encuentra la version live (ID6) porque su proviene_de es (5) la imprime y ejecuta el caso recursivo llamando a versiones (6)
 Llamada 3 : versiones (6) el for recorre el catalogo buscando quien derive del (6), no encuentra a nadie, se alcanza el caso base, la llamada 3 termina y avisa a la llamada 2 que termino, cerrando el ciclo

## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada |  |  |
| Pila |  |  |
| Cola |  |  |

Dónde se usa cada uno en el dominio.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
|  |  |  |  |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
|  |  |  |

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
