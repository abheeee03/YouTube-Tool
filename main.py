from pytube import YouTube

print("------------------------------\n")
print("YOUTUBE TOOL BY ABHEE\n")
print("------------------------------\n")
link = input("Enter YouTube Video Link : ")
converted_link = YouTube(link)
print(f"\nTitle of the Video : {converted_link.title} ")
