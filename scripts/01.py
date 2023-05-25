import yt_dlp
from moviepy.editor import VideoFileClip

video_url = "https://www.youtube.com/watch?v=ovI7ODWM2kU"

ydl_opts = {
    'format': 'best',
    'paths': {
        'home': 'download'
    },
    'outtmpl': {
        'default': 'video.%(ext)s'
    }
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(video_url)

clip = VideoFileClip("download/video.mp4")
audio = clip.audio
audio.write_audiofile("download/audio.wav", codec='pcm_s16le', fps=16000)
