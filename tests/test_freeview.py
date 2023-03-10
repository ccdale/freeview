import os

import pytest

import freeview
from freeview.tstomp4 import fileInfo, FqfnNotExits, FfmpegReadError


def test_version():
    assert freeview.__version__ == "0.1.1"


def test_fileInfo():
    here = os.path.dirname(os.path.realpath(__file__))
    fqfn = os.path.join(here, "freeview.ts")
    assert os.path.exists(fqfn)
    finfo = fileInfo(fqfn)
    assert "streams" in finfo
    assert len(finfo["streams"]) > 2
    assert finfo["streams"][0]["codec_name"] == "mpeg2video"


def test_fileInfo_not_exist():
    fqfn = "wibble.not.exist"
    assert not os.path.exists(fqfn)
    with pytest.raises(SystemExit):
        with pytest.raises(FqfnNotExits):
            finfo = fileInfo(fqfn)


def test_fileInfo_failed():
    here = os.path.dirname(os.path.realpath(__file__))
    fqfn = os.path.join(here, "random.not.ts")
    assert os.path.exists(fqfn)
    with pytest.raises(SystemExit):
        with pytest.raises(FfmpegReadError):
            finfo = fileInfo(fqfn)
