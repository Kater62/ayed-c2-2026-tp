from src.config import TEMA
from src.dominio.cancion import listar_catalogo, versiones , Cancion
from src.dominio.playlist import Playlist
from src.excepciones import ColeccionLlenaError , PilaVaciaError, ColaVaciaError
from src.tads.pila import Pila
from src.tads.cola import Cola


TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}


def pendiente():
    print("Todavía no está implementado. Completar en la entrega que corresponde.")


def mostrar_menu():
    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")
    print()
    print(f"=== {nombre} — AyED C2 2026 ===")
    print("1. Listar catálogo")
    print("2. Ver detalle")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Operación recursiva")
    print("6. Colección principal (equipo / menú / playlist)")
    print("7. Historial (pila)")
    print("8. Cola")
    print("9. Guardar / cargar archivos")
    print("0. Salir")


def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    opcion = None
    miplaylist = Playlist (2)
    historial = Pila ()
    siguiente_cancion = Cola ()

    while opcion != "0":
        mostrar_menu()
        opcion = input("> ").strip()
        if opcion == "0":
            print("Chau.")

        elif opcion == "1":
            listar_catalogo ()

        elif opcion == "5":
           idelegido = int(input("Ingrese un ID: "))
           print ("-----Versiones derivadas-----")
           versiones (idelegido)

        elif opcion == "6":
            tema = Cancion (99, "Machine Gun", "Jimi Hendrix", "Rock Psicodelico")
            try:
                miplaylist.agregar_cancion (tema)
                print ("Cancion Agregada!")
            except ColeccionLlenaError:
                print ("Error! Playlist Llena no entran mas canciones!")

        elif opcion == "7":
            print ("1: Agregar cancion.")
            print ("2: Eliminar ultima cancion.")
            accion = input("Elija la operacion a realizar")           
            if accion == "1":
                tema_historial = Cancion (98, "Abelardo el Pollo", "Pappo Blues", "Blues")
                historial.apilar (tema_historial)
                print ("Cancion agregada al Historial!")
            elif accion == "2":
                try:
                    historial.desapilar ()
                    print ("Ultima cancion eliminada!")
                except PilaVaciaError:
                    print ("Aviso! Historial vacio no hay nada para quitar")


        elif opcion == "8":
            print("1: Agregar cancion a la Cola de reproduccion")
            print("2: Reproducir la Siguiente Cancion")
            accion2 = input ("Elija la operacion a realizar")
            if accion2 == "1":
                tema_en_cola = Cancion (97, "Quiero Estar Seguro de Vivir", "Vox Dei", "Rock")
                siguiente_cancion.encolar (tema_en_cola)
                print ("Cancion Agregada a la Cola!")
            elif accion2 == "2":
                try:
                    siguiente_cancion.desencolar()
                    print ("Reproduciendo la Siguiente Cancion!")
                except ColaVaciaError:
                    print ("Aviso! Lista de reproduccion vacia!")

        elif opcion in {"2", "3", "4", "9"}:
            pendiente()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
