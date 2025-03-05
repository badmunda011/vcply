import asyncio
import os
import yt_dlp
from . import queues
from ..clients.clients import call
from ...console import USERBOT_PICTURE
from asyncio.queues import QueueEmpty
from ntgcalls import InputMode
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types import AudioParameters, VideoParameters, Stream
from pytgcalls.types.input_stream import AudioStream, VideoStream
from youtubesearchpython.__future__ import VideosSearch
from yt_dlp.utils import DownloadError, ExtractorError, GeoRestrictedError

# Adjust the path to your cookies file
COOKIES_FILE_PATH = "/path/to/your/cookies.txt"

async def run_async(func, *args, **kwargs):
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, func, *args, **kwargs)

async def get_result(query: str):
    results = VideosSearch(query, limit=1)
    for result in (await results.next())["result"]:
        url = result["link"]
        try:
            thumbnail = result["thumbnails"][0]["url"].split("?")[0]
        except:
            thumbnail = USERBOT_PICTURE
        
    return url, thumbnail

async def get_stream(link, type):
    if type == "Audio":
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "geo_bypass": True,
            "nocheckcertificate": True,
            "quiet": True,
            "no_warnings": True,
            "cookiefile": COOKIES_FILE_PATH,  # Add cookies file
        }

    elif type == "Video":
        ydl_opts = {
            "format": "(bestvideo[height<=?720][width<=?1280][ext=mp4])+(bestaudio[ext=m4a])",
            "outtmpl": "downloads/%(id)s.%(ext)s",
            "geo_bypass": True,
            "nocheckcertificate": True,
            "quiet": True,
            "no_warnings": True,
            "cookiefile": COOKIES_FILE_PATH,  # Add cookies file
        }
        
    x = yt_dlp.YoutubeDL(ydl_opts)
    try:
        info = x.extract_info(link, False)
    except (DownloadError, ExtractorError, GeoRestrictedError) as e:
        print(f"Error extracting info: {e}")
        return None

    file = os.path.join("downloads", f"{info['id']}.{info['ext']}")
    if os.path.exists(file):
        return file
    await run_async(x.download, [link])
    return file

async def run_stream(file, type):
    if type == "Audio":
        audio_stream = AudioStream(
            input_mode=InputMode.Shell,
            path=f"ffmpeg -i {file} -f s16le -ac 2 -ar 48k pipe:1",
            parameters=AudioParameters(
                bitrate=48000,
                channels=2,
            ),
        )
        stream = Stream(audio_stream, stream_type=StreamType().local_stream)

    elif type == "Video":
        audio_stream = AudioStream(
            input_mode=InputMode.Shell,
            path=f"ffmpeg -i {file} -f s16le -ac 2 -ar 48k pipe:1",
            parameters=AudioParameters(
                bitrate=48000,
                channels=2,
            ),
        )
        video_stream = VideoStream(
            input_mode=InputMode.Shell,
            path=f"ffmpeg -i {file} -f rawvideo -r 30 -pix_fmt yuv420p -vf scale=1280:720 pipe:1",
            parameters=VideoParameters(
                width=1280,
                height=720,
                frame_rate=30,
            ),
        )
        stream = Stream(audio_stream, video_stream, stream_type=StreamType().local_stream)
        
    return stream

async def close_stream(chat_id):
    try:
        await queues.clear(chat_id)
    except QueueEmpty:
        pass
    try:
        return await call.leave_group_call(chat_id)
    except Exception as e:
        print(f"Error leaving group call: {e}")
        pass
