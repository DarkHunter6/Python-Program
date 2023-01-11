from pytube import YouTube

def Download(Link):
    MyYoutube = YouTube(Link)
    MyYoutube = MyYoutube.streams.get_highest_resolution()

    try:
        MyYoutube.Download()
    except:
        print('There Is An Error In Downloading')
print('Your Download Is Completed..!')

Link = input('Paste The Url Of The Video : ')
Download(Link)