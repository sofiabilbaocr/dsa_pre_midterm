from ll_double_linked import LinkedList

def cargar_canciones(lista_vinculada):
    # Lista de 50 canciones reales con Nombre, Artista y Álbum
    canciones = [
        {"nombre": "Bohemian Rhapsody", "artista": "Queen", "album": "A Night at the Opera"},
        {"nombre": "Billie Jean", "artista": "Michael Jackson", "album": "Thriller"},
        {"nombre": "Hotel California", "artista": "Eagles", "album": "Hotel California"},
        {"nombre": "Imagine", "artista": "John Lennon", "album": "Imagine"},
        {"nombre": "Smells Like Teen Spirit", "artista": "Nirvana", "album": "Nevermind"},
        {"nombre": "Sweet Child O Mine", "artista": "Guns N Roses", "album": "Appetite for Destruction"},
        {"nombre": "One", "artista": "U2", "album": "Achtung Baby"},
        {"nombre": "Like a Rolling Stone", "artista": "Bob Dylan", "album": "Highway 61 Revisited"},
        {"nombre": "Stayin Alive", "artista": "Bee Gees", "album": "Saturday Night Fever"},
        {"nombre": "Hey Jude", "artista": "The Beatles", "album": "Single"},
        {"nombre": "De Musica Ligera", "artista": "Soda Stereo", "album": "Cancion Animal"},
        {"nombre": "Rayando el Sol", "artista": "Mana", "album": "Falta Amor"},
        {"nombre": "Titi Me Pregunto", "artista": "Bad Bunny", "album": "Un Verano Sin Ti"},
        {"nombre": "Provenza", "artista": "Karol G", "album": "Mañana Será Bonito"},
        {"nombre": "Despacito", "artista": "Luis Fonsi", "album": "Vida"},
        {"nombre": "La Bachata", "artista": "Manuel Turizo", "album": "2000"},
        {"nombre": "Hips Dont Lie", "artista": "Shakira", "album": "Oral Fixation Vol. 2"},
        {"nombre": "Lamento Boliviano", "artista": "Enanitos Verdes", "album": "Big Bang"},
        {"nombre": "Persiana Americana", "artista": "Soda Stereo", "album": "Signos"},
        {"nombre": "Glow Up", "artista": "Young Miko", "album": "Trap Kitty"},
        {"nombre": "Blinding Lights", "artista": "The Weeknd", "album": "After Hours"},
        {"nombre": "Shape of You", "artista": "Ed Sheeran", "album": "Divide"},
        {"nombre": "Rolling in the Deep", "artista": "Adele", "album": "21"},
        {"nombre": "Yellow", "artista": "Coldplay", "album": "Parachutes"},
        {"nombre": "Mr. Brightside", "artista": "The Killers", "album": "Hot Fuss"},
        {"nombre": "Wonderwall", "artista": "Oasis", "album": "Whats the Story Morning Glory"},
        {"nombre": "Lose Yourself", "artista": "Eminem", "album": "8 Mile"},
        {"nombre": "In the End", "artista": "Linkin Park", "album": "Hybrid Theory"},
        {"nombre": "Back in Black", "artista": "AC/DC", "album": "Back in Black"},
        {"nombre": "Highway to Hell", "artista": "AC/DC", "album": "Highway to Hell"},
        {"nombre": "Every Breath You Take", "artista": "The Police", "album": "Synchronicity"},
        {"nombre": "Take on Me", "artista": "A-ha", "album": "Hunting High and Low"},
        {"nombre": "Girls Just Want to Have Fun", "artista": "Cyndi Lauper", "album": "Shes So Unusual"},
        {"nombre": "Under the Bridge", "artista": "Red Hot Chili Peppers", "album": "Blood Sugar Sex Magik"},
        {"nombre": "Bitter Sweet Symphony", "artista": "The Verve", "album": "Urban Hymns"},
        {"nombre": "Creep", "artista": "Radiohead", "album": "Pablo Honey"},
        {"nombre": "Seven Nation Army", "artista": "The White Stripes", "album": "Elephant"},
        {"nombre": "Clocks", "artista": "Coldplay", "album": "A Rush of Blood to the Head"},
        {"nombre": "Gasolina", "artista": "Daddy Yankee", "album": "Barrio Fino"},
        {"nombre": "Danza Kuduro", "artista": "Don Omar", "album": "Meet the Orphans"},
        {"nombre": "Vivir Mi Vida", "artista": "Marc Anthony", "album": "3.0"},
        {"nombre": "Propuesta Indecente", "artista": "Romeo Santos", "album": "Formula, Vol. 2"},
        {"nombre": "Hawai", "artista": "Maluma", "album": "Papi Juancho"},
        {"nombre": "Monaco", "artista": "Bad Bunny", "album": "Nadie Sabe Lo Que Va A Pasar Mañana"},
        {"nombre": "Flowers", "artista": "Miley Cyrus", "album": "Endless Summer Vacation"},
        {"nombre": "As It Was", "artista": "Harry Styles", "album": "Harrys House"},
        {"nombre": "Anti-Hero", "artista": "Taylor Swift", "album": "Midnights"},
        {"nombre": "Vampire", "artista": "Olivia Rodrigo", "album": "Guts"},
        {"nombre": "Cruel Summer", "artista": "Taylor Swift", "album": "Lover"},
        {"nombre": "Paint The Town Red", "artista": "Doja Cat", "album": "Scarlet"}
    ]

    for cancion in canciones:
        lista_vinculada.append(cancion)

def ejecutar_demo():
    # Inicia la playlist vacía
    mi_playlist = LinkedList()
    print("Playlist creada (vacia)")
    
    # Llena la playlist con las 50 canciones
    cargar_canciones(mi_playlist)
    print("Se han cargado 50 canciones exitosamente")

if __name__ == "__main__":
    ejecutar_demo()