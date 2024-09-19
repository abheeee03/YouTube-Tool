from pytube import YouTube


def download_video(link):
  converted_link = YouTube(link)
  vid_title = converted_link.title
  print(f"You are downloading : {vid_title}")
  vid_stream = converted_link.streams.get_highest_resolution()
  vid_stream.download()
  print("Downloaded Successfully!")

def download_audio(link):
  converted_link = YouTube(link)
  vid_title = converted_link.title
  print(f"You are downloading Audio of : {vid_title}")
  audio_stream = converted_link.streams.get_audio_only()
  audio_stream.download()
  print("Downloaded Successfully!")


print("------------------------------\n")
print("YOUTUBE TOOL BY ABHEE\n")
print("------------------------------\n")
print("\nChoose the Services You want to use :")
print("1. Download Video")
print("2. Download Audio\n\n")
usr_input = int(input("Enter 1 or 2 : "))
link = input("Enter YouTube Video Link : ")

if usr_input == 1:
  download_video(link)
elif usr_input == 2:
  download_audio(link)
else:
  print("Error ! Try Again Entering Valid Number")
