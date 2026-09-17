class Cancion:
    def __init__ (self, id, titulo, artista, genero):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.genero = genero

CATALOGO = [Cancion (1, "High Hopes", "Pink Floyd", "Rock Progresivo"),
            Cancion (2, "Drag The Waters", "Pantera", "Groove Metal"),
            Cancion (3, "Lord Of This World", "Black Sabbath", "Heavy Metal"),
            Cancion (4, "Mi Genio Amor", "Patricio Rey y sus Redonditos de Ricota", "Rock Nacional")]

def listar_catalogo():
    # Esta función recorre nuestra lista y muestra cada canción en la pantalla
    print("--- CATÁLOGO MUSICAL ---")
    for cancion in CATALOGO:
        print(f"{cancion.id}. {cancion.titulo} - {cancion.artista} - {cancion.genero}")
    print("------------------------")

