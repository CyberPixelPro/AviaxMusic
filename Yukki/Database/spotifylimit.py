from typing import Dict, List, Union
from Yukki import SUDOERS, db

spotifydb = db.spotify


async def get_playlist_limit_sudoers() -> list:
    sudoers = await spotifydb.find_one({"sudo": "sudo"})
    if not sudoers:
        return SUDOERS
    for user_id in SUDOERS:
            if user_id not in sudoers["sudoers"]:
                sudoers["sudoers"].append(user_id)
    return sudoers["sudoers"]


async def add_playlist_limit_sudo(user_id: int) -> bool:
    sudoers = await get_playlist_limit_sudoers()
    sudoers.append(user_id)
    await spotifydb.update_one(
        {"sudo": "sudo"}, {"$set": {"sudoers": sudoers}}, upsert=True
    )
    return True


async def remove_playlist_limit_sudo(user_id: int) -> bool:
    sudoers = await get_playlist_limit_sudoers()
    sudoers.remove(user_id)
    await spotifydb.update_one(
        {"sudo": "sudo"}, {"$set": {"sudoers": sudoers}}, upsert=True
    )
    return True