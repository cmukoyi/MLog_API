# First, install the required libraries
# pip install pytube pydub

# Ensure ffmpeg is installed and added to your system's PATH

from pytube import YouTube
from pydub import AudioSegment
import os

def download_youtube_video(url, output_path="output"):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Download video
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=output_path)
    
    # Convert to mp3
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    
    audio = AudioSegment.from_file(out_file)
    audio.export(new_file, format="mp3")
    
    # Remove the original file
    os.remove(out_file)
    
    print(f"Downloaded and converted to MP3: {new_file}")

# Example usage
youtube_url = "https://www.youtube.com/watch?v=T6eK-2OQtew"
download_youtube_video(youtube_url)
