# Python Modules
from urllib import parse, request
import re
import youtube_dl
import os

# Lee lo que escribe el usuario y genera una url de busqueda
search = input('Busca un video ')
query_string = parse.urlencode({"search_query": search})
html_content = request.urlopen(
    "http://www.youtube.com/results?" + query_string)
search_results = re.findall(
     r"watch\?v=(\S{11})", html_content.read().decode())
# url de respeusta
url = "https://www.youtube.com/watch?v=" + search_results[0]

# Parametros de descarga
ydl_op = {
     'format': 'bestaudio/best',
     'quiet': True,
     'postprocessor': [{
          'key': 'FFmpegExtractAudio',
          'preferredcodec': 'mp3',
          'preferredquality': '192',
     }],
}



# Descarga
with youtube_dl.YoutubeDL(ydl_op) as ydl:
     print('[+] Descargando video...')
     ydl.download([url])
     print('[+] Video descargado, convirtiendo a .mp3...')
     for file in os.listdir('./'):
          if file.endswith('.m4a') or file.endswith('.webm'):
               indice = file.index('.')
               newName = file[0:indice]
               print(newName)
               os.rename(file, f'{newName}.mp3')
               print('[+] Video converttido exitosamente!')