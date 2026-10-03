from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ColeccionLlenaError

class Playlist:
    def __init__ (self, limite_maximo):
        self._limite_maximo = limite_maximo
        self._canciones = ListaEnlazada()

    def agregar_cancion (self, cancion):
        if self._canciones.tamanio () >= self._limite_maximo:
            raise ColeccionLlenaError ("La playlist esta llena.")

        self._canciones.insertar_al_final (cancion)

            