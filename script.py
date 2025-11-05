import yt_dlp
import os
import shutil  # usado para verificar se o ffmpeg existe

def baixar_musica(nome_musica, pasta_destino="musicas"):
    os.makedirs(pasta_destino, exist_ok=True)
    print(f"🔎 Procurando '{nome_musica}' no YouTube e baixando o áudio...")

    # Verifica se o ffmpeg está instalado
    ffmpeg_disponivel = shutil.which("ffmpeg") is not None

    # Configurações padrão
    opcoes = {
        'format': 'bestaudio/best',
        'outtmpl': f'{pasta_destino}/%(title)s.%(ext)s',
        'quiet': False,
    }

    # Se o FFmpeg estiver disponível, converte para MP3
    if ffmpeg_disponivel:
        opcoes['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
        print("🎧 FFmpeg encontrado — o áudio será convertido para MP3.")
    else:
        print("⚠️ FFmpeg não encontrado — o áudio será salvo no formato original (webm).")

    # Faz o download e conversão
    with yt_dlp.YoutubeDL(opcoes) as ydl:
        ydl.download([f"ytsearch1:{nome_musica}"])  # busca e baixa o 1º resultado

    print(f"✅ '{nome_musica}' baixada com sucesso!\n")


# 🎵 Lista de músicas
lista_musicas = [
    # AC/DC
    "AC/DC - Highway to Hell",
    "AC/DC - Back in Black",
    "AC/DC - Thunderstruck",

    # Queen
    "Queen - We Will Rock You",
    "Queen - I Want to Break Free",

    # Legião Urbana
    "Legião Urbana - Tempo Perdido",
    "Legião Urbana - Pais e Filhos",
    "Legião Urbana - Faroeste Caboclo",
    "Legião Urbana - Eduardo e Mônica",
    "Legião Urbana - Será",
    "Legião Urbana - Ainda é Cedo",

    # Raul Seixas
    "Raul Seixas - Metamorfose Ambulante",
    "Raul Seixas - Maluco Beleza",
    "Raul Seixas - Eu Nasci Há 10 Mil Anos Atrás",
    "Raul Seixas - Tente Outra Vez",
    "Raul Seixas - Cowboy Fora da Lei",

    # Clássicos adicionais dos anos 80-90
    "Guns N' Roses - Sweet Child O' Mine",
    "Bon Jovi - Livin' on a Prayer",
    "Nirvana - Smells Like Teen Spirit",
    "Metallica - Enter Sandman",
    "Scorpions - Wind of Change",
    "Aerosmith - Dream On",
    "Pearl Jam - Alive",
    "The Police - Every Breath You Take",
    "U2 - With or Without You",
    "Pink Floyd - Another Brick in the Wall",
    "The Rolling Stones - Start Me Up",
    "Deep Purple - Smoke on the Water"
]

for musica in lista_musicas:
    baixar_musica(musica)
