#Download de video usando a biblioteca pytube
from pytube import YouTube

#Link do video na qual deseja baixar
video = YouTube("https://www.youtube.com/watch?v=R4Ukl9u9_4Q") 

#Utilizado para ver todo o conteúdo baixado e também para pegar a tag de download, recomendo ler a documentação do pytube e ir realizando testes
print(video.streams.filter(file_extension="mp4", progressive=True)) 

#Seleciona o video pela tag obtida pelo comando acima
video = video.streams.get_by_itag(22)

#realiza o download do video
video.download(filename="video.mp4")