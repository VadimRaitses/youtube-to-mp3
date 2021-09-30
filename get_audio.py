from __future__ import unicode_literals
import youtube_dl
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--url', help='youtube url')


def get_audio(url):
    print(f'getting, {url}')

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(url)
    except Exception as err:
        print("Oops! Try again...{0}".format(err))


if __name__ == '__main__':
    args = vars(parser.parse_args())
    get_audio([args['url']])
