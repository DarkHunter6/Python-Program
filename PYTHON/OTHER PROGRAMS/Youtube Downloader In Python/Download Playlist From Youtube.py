# ========================================================= (PROGRAM 3 -> For Playlist Download) ==============================================

from pytube import Playlist # Import 'Playlist' Class From 'pytube' To Download Any Playlist From Youtube

PlayList_1 = Playlist(str(input('Enter The PlayList Url You Want To Download : '))) # Call The 'PlayList' Function. 
print(PlayList_1.title) # For Show The Title Of The Video

for Video in PlayList_1.videos:
    Video.streams.get_highest_resolution().download()