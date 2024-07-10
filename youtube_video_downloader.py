from pytube import YouTube

url = "https://youtube.com/shorts/kuk3Io_qq1w?si=Yw68bcWMdsxKe0zs"
yt = YouTube(url)

# This will download the video in high quality
video = yt.streams.get_highest_resolution()

# This will download the video in low quality
# video = yt.streams.get_lowest_resolution()

# This will only download the audio 
# video = yt.streams.get_audio_only()

video.download()
print("Successfull")