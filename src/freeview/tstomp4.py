import json
import os
import sys
import subprocess

from ccaerrors import errorNotify, errorRaise, errorExit
import ccalogging

log = ccalogging.log


class FqfnNotExits(Exception):
    pass


class FfmpegReadError(Exception):
    pass


def fileInfo(fqfn):
    try:
        if not os.path.exists(fqfn):
            raise FqfnNotExits(f"{fqfn} does not exist")
        cmd = ["ffprobe", "-loglevel", "quiet", "-of", "json", "-show_streams", fqfn]
        proc = subprocess.run(cmd, capture_output=True)
        if proc.returncode != 0:
            raise FfmpegReadError(f"{fqfn} could not be read correctly by ffmpeg")
        return json.loads(proc.stdout.decode("utf-8"))
    except Exception as e:
        errorExit(sys.exc_info()[2], e)
