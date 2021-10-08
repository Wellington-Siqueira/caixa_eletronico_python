from pytube import YouTube

video = YouTube("https://www.youtube.com/watch?v=9FiEji_fzvk")

print(video.streams.filter(file_extension="mp4", progressive=True))

video = video.streams.get_by_itag(22)
video.download(filename="teste.mp4")