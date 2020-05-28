from pytube import YouTube
YouTube('https://g1.globo.com/sp/santos-regiao/noticia/2020/05/20/litoral-de-sp-adota-barreiras-para-evitar-turistas-durante-megaferiado.ghtml').streams.first().download()

#from pytube import Playlist
#pl = Playlist("https://www.youtube.com/playlist?list=PL_qemo0pL43sL1QWjfFBdkxiqpCS_x-71")
#pl.download_all()
# or if you want to download in a specific directory
#pl.download_all('path\to\files')