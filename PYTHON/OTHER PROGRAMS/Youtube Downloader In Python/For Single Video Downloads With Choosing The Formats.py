# ==================================== (PROGRAM 1 -> For Single Video Downloads With Formats) =============================

from pytube import YouTube # 1

Link = str(input('Enter Youtube Link To Download : ')) # 2
MyTube = YouTube(Link) # 3

Video = MyTube.streams.all() # 4
Vid = list(enumerate(Video)) # 5

for Dwn in Vid: # 6
    print(Dwn) # 7
    
print() # 8
print('-----------------------------------------')
Stream = int(input('Enter The Index Number To Download The Video Format You Want : ')) # 9

try: # 10
    Video[Stream].download() # 11
except: # 12
 print('There Is An Error In Downloading...!')
print('Your Video Is Downloaded Successfully...!')

# ======================================= Defination Of This Code ================================
# 1. We Import The 'Youtube' Class From 'pytube' Library.
# 2. Create A Var 'List' To Paste The Url Of Any YouTube Video.
# 3. Create A Var 'MyTube', Call The 'YouTube' Class And Pass The 'Link' Var.
# 4. Create A Var 'Video', We Have Every Details Of The Url In 'MyTube' Var, 
   # So We Call This Var And 'streams' Helps Us To  Get 'all' The Format, All The Resolution Of The Video.
# 5. Create A Var 'Vid', We Need Every Formats Of The Video In List, So We Call The 'list()' And Use 'enumerate()' To Get The Index Number Of The List.
   # So We Could Use The Index Numbers To Download The Video In Any Format We Want.
# 6 / 7. Mow We Have To Run A 'for' Loop Over The Details Of Video. So We Run This 'for' Loop Through Vid And Print The 'all' The Formats We Want To See.
# 8. For Make A Gap.
# 9. Create A Var 'Stream' And We Have To Input The Index Numbers Of The Formats.
# 10. 'try' Block Helps Us To 'Block' The Codes For Errors.
# 11. We Have Every Formats Into The 'Video' Var, So We Pass The 'Stream' Var Into It Which Is Contains The Index Numbers Of The Video Formats
    # And 'download' For Download The Video.
# 12 . 'except' Block For Handle The Errors Will Occur In The Code.