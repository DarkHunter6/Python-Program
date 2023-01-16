# =========================================== (PROGRAM 2 -> For Full Format Single Video) ===========================

from pytube import YouTube # Import 'Youtube' Class From 'pytube' Library.

def Download():
    MyTube = YouTube(Link) # Call The Youtube From import pytube And Pass The 'Link' Parameter Through It.
    MyTube = MyTube.streams.get_highest_resolution() # 

    try:
        MyTube.download()
    except:
     print('There Is An Error In Downloading')
    print('Your Download Is Completed..!')

Link = input('Paste The Url Of The Video : ')
Download(Link)