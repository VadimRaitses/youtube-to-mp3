# youtube_to_mp3
Extract audio from youtube video

       virtualenv venv 
       source venv/bin/activate

       brew install ffmpeg
       pip install youtube_dl 
       pip install  ffmpeg
       
       python -m get_audio --url "youtube url"



# Workarouns:

For everyone using youtube_dl and wondering how to solve this issue without using another library like ytdlp: First uninstall youtube_dl with pip uninstall youtube_dl then install the master branch of youtube_dl from their github with pip install git+https://github.com/ytdl-org/youtube-dl.git@master#egg=youtube_dl. You need git for this, download it here. Ive tested it and it works actually.