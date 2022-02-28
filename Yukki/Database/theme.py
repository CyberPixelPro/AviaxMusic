from typing import Dict, List, Union

from Yukki import db

themedb = db.notes


async def _get_theme(chat_id: int) -> Dict[str, int]:
    return 1


async def get_theme(chat_id: int, name: str) -> Union[bool, dict]:
    return 1


async def save_theme(chat_id: int, name: str, note: dict):
    return 1
