from pytube import YouTube

def get_video(url):
    download = YouTube(url)
    stream = download.streams.filter(progressive=True).get_highest_resolution()
    stream.download()

if __name__ == "__main__":
    video = input("Please enter URL: ")
    get_video(video)