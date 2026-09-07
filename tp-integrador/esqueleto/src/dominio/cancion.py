CATALOGO = [
    {"id": 1, "titulo": "High Hopes", "artista": "Pink Floyd", "genero": "Rock Progresivo"},
    {"id": 2, "titulo": "Drag the Waters", "artista": "Pantera", "genero": "Groove Metal"},
    {"id": 3, "titulo": "Lord of this World", "artista": "Black Sabbath", "genero": "Heavy Metal"},
    {"id": 4, "titulo": "Mi Genio Amor", "artista": "Patricio Rey y sus Redonditos de Ricota", "genero": "Rock Nacional"}
]

def listar_catalogo():
    # Esta función recorre nuestra lista y muestra cada canción en la pantalla
    print("--- CATÁLOGO MUSICAL ---")
    for cancion in CATALOGO:
        print(f"{cancion['id']}. {cancion['titulo']} - {cancion['artista']}")
    print("------------------------")