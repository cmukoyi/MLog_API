from flask import Flask, render_template, request, send_file
from pytube import YouTube
from pydub import AudioSegment
import os

app = Flask(__name__)

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
    
    return new_file

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        try:
            file_path = download_youtube_video(url)
            return send_file(file_path, as_attachment=True)
        except Exception as e:
            return str(e)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
