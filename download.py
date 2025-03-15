import os
import yt_dlp as youtube_dl
from pytube import YouTube
from pytube.request import default_headers

# Configurar headers atualizados
default_headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.youtube.com/'
})

def main():
    url = input("URL do YouTube: ")
    
    try:
        baixar_com_pytube(url)
    except Exception as e:
        print(f"\nErro no pytube: {e}")
        baixar_com_ytdlp(url)

def baixar_com_ytdlp(url):
    destino = os.path.join("videos", "%(title)s.%(ext)s")
    
    ydl_opts = {
        'outtmpl': destino,
        'progress_hooks': [progress_hook],
        'cookiefile': 'cookies.txt',
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'noplaylist': True,
        'ignoreerrors': True,
        'geo_bypass': True,
        'throttled_rate': '1M',
        'retries': 10,
        'socket_timeout': 30,
        'http_chunk_size': 1048576,
        'verbose': False
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            if 'entries' in info:
                print(f"\n⚠️ Detectada playlist com {len(info['entries'])} vídeos!")
                if input("Deseja baixar toda a playlist? (s/n): ").lower() != 's':
                    ydl_opts['noplaylist'] = True
                    
            ydl.download([url])
        print("\n✅ Download concluído com sucesso!")
    except Exception as e:
        print(f"\n❌ Erro final: {str(e)[:200]}")

# ... (mantenha as funções de progresso anteriores)

if __name__ == "__main__":
    main()