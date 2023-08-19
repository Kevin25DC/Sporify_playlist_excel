import spotipy
from spotipy.oauth2 import SpotifyOAuth
import openpyxl

# Configura las credenciales de la API de Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='id_cliente', #esto lo consigues en la pagina sporify developer
                                               client_secret='id_secreto', #al igual que este
                                               redirect_uri='http://localhost:8080',
                                               scope='playlist-read-private'))


playlist_id = '7a802Q3DsRUdBkDNYrUaJ0' #este es el id de la playlist , en este caso yo sacare las canciones de cada playlist, esto lo consigues en la url de la playlist

# Obtiene las canciones de la playlist
tracks = sp.playlist_tracks(playlist_id)

# Crea un nuevo archivo de Excel
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Canciones de la Playlist"

# Agrega encabezados a las columnas
sheet['A1'] = 'Número'
sheet['B1'] = 'Artista'
sheet['C1'] = 'Canción'

# Llena el archivo de Excel con la información de las canciones
for idx, track in enumerate(tracks['items'], start=2):
    sheet[f'A{idx}'] = idx - 1
    sheet[f'B{idx}'] = track['track']['artists'][0]['name']
    sheet[f'C{idx}'] = track['track']['name']

# Guarda el archivo de Excel
workbook.save("canciones_de_mi_amor.xlsx")

print("Las canciones de la playlist se han guardado en canciones_de_playlist.xlsx")
