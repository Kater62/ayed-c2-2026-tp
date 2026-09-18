class Cancion:
    def __init__ (self, id, titulo, artista, genero, proviene_de = None):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.proviene_de = proviene_de

CATALOGO = [Cancion (1, "High Hopes", "Pink Floyd", "Rock Progresivo"),
            Cancion (2, "Drag The Waters", "Pantera", "Groove Metal"),
            Cancion (3, "Lord Of This World", "Black Sabbath", "Heavy Metal"),
            Cancion (4, "Mi Genio Amor", "Patricio Rey y sus Redonditos de Ricota", "Rock Nacional"),
            Cancion (5, "High Hopes (Cover)", "Nightwish", "Metal Sinfonico", 1),
            Cancion (6, "High Hopes (Live)", "Nightwish", "Metal Sinfonico", 5 )]

def versiones (id):
    for ver in CATALOGO:
        if ver.proviene_de == id:
            print (f"{ver.artista} - {ver.titulo}")
            versiones (ver.id)
        



def listar_catalogo():
    # Esta función recorre nuestra lista y muestra cada canción en la pantalla
    print("--- CATÁLOGO MUSICAL ---")
    for cancion in CATALOGO:
        print(f"{cancion.id}. {cancion.titulo} - {cancion.artista} - {cancion.genero}")
    print("------------------------")
