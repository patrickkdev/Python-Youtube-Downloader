from pytube import YouTube
import tkinter as tk
from tkinter import filedialog
import os

def get_save_directory():
    folder = filedialog.askdirectory()
    
    if folder:
        print(f"Pasta selecionada {folder}")

    return folder

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()

        highest_res_stream.download(output_path=save_path)
        print("Video baixado com sucesso.")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    os.system("cls")
    print("\n\n Youtube Downloader \n\n")

    video_url = input ("Informe a URL do vídeo: ")
    save_dir = get_save_directory()

    if save_dir:
        print("Download iniciado. Por favor aguarde.")
        download_video(video_url, save_dir)
    else:
        print("Local inválido")


