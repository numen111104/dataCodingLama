from pytube import YouTube
from moviepy.editor import VideoFileClip

# Fungsi untuk mendownload video dari YouTube
def download_video(url, output_path):
    yt = YouTube(url)
    video = yt.streams.first()
    video.download(output_path)

# Fungsi untuk mengonversi video ke format MP3
def convert_to_mp3(video_path, output_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(output_path)

# Masukkan URL video YouTube dari pengguna
video_url = input("Masukkan URL video YouTube: ")

# Path untuk menyimpan video dan output file MP3
video_output_path = r"C:\Users\numan\OneDrive\Dokumen\DATA MUROTTAL\Output\video.mp4"
mp3_output_path = r"C:\Users\numan\OneDrive\Dokumen\DATA MUROTTAL\Output\audio.mp3"

# Download video dari YouTube
download_video(video_url, video_output_path)

# Konversi video ke format MP3
convert_to_mp3(video_output_path, mp3_output_path)
