import pytube

video_list = []

print('Enter the Urls (When finish type STOP ...)')
while True:
    url = input("")
    if url == "stop":
        break
    video_list.append(url)

for x, video in enumerate(video_list):
    v = pytube.YouTube(video)
    stream = v.streams.get_by_itag(140)
    print(f'Downloading video {x}...')
    stream.download()
    print('Done')


