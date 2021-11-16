import os
import Utils
from typing import BinaryIO, Optional
from worlds.Files import APDeltaPatch

USHASH = 'a7c7a76b4d6f6df389bd631757b91b76'


def read_rom(stream: BinaryIO, strip_header: bool = True) -> bytes:
    """Reads rom into bytearray and optionally strips off any smc header"""
    data = stream.read()
    if strip_header and len(data) % 0x400 == 0x200:
        return data[0x200:]
    return data


class SoEDeltaPatch(APDeltaPatch):
    hash = USHASH
    game = "Illusion of Gaia"
    patch_file_ending = ".apiog"

    @classmethod
    def get_source_data(cls) -> bytes:
        with open(get_base_rom_path(), "rb") as stream:
            return read_rom(stream)


def get_base_rom_path(file_name: str = "") -> str:
    options = Utils.get_options()
    if not file_name:
        file_name = options["iog_options"]["rom_file"]
    if not os.path.exists(file_name):
        file_name = Utils.user_path(file_name)
    return file_name
