from YukkiMusic.core.mongo import mongodb
from config import OWNER_ID
from YukkiMusic.misc import SUDO_USERS

limitsdb = mongodb.limits

SUDOS = SUDO_USERS

async def is_approved(user_id: int) -> bool:
    if user_id in SUDOS:
        return True
    user = await limitsdb.find_one({"user_id": user_id})
    if not user:
        return False
    return True


async def get_approved_users() -> list:
    users_list = []
    async for user in limitsdb.find({"user_id": {"$gt": 0}}):
        users_list.append(user["user_id"])
    return users_list + SUDOS


async def add_to_approved_user(user_id: int):
    is_appr= await is_approved(user_id)
    if is_appr:
        return
    return await limitsdb.insert_one({"user_id": user_id})

async def remove_approved_user(user_id: int):
    is_appr = await is_approved(user_id)
    if not is_appr:
        return
    return await limitsdb.delete_one({"user_id": user_id})
