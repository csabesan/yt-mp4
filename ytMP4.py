from pytube import YouTube
from sys import argv

# Get the YouTube video URL from the command-line arguments
# argv[0] is the script name, so argv[1] contains the URL provided as the first argument
link = argv[1]

# Create a YouTube object
yt = YouTube(link);

# Get the highest resolution stream (video and audio)
stream = yt.streams.get_highest_resolution()

# Download the video to the current working directory with the default file name
stream.download()
