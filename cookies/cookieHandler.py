import os
import sys
import requests
import asyncio
import time  
from config import LOGGER_ID, BOT_TOKEN, API_HASH, API_ID
from http.cookiejar import MozillaCookieJar as surefir
from pyrogram import Client, filters, idle
from pyrogram.types import Message
from AnonXMusic.core.mongo import mongodb


# Paths & Global Variables
cookiePath = os.path.join(os.getcwd(), "cookies", "cookies.txt")
areCookiesValid = False
mid = None
wid = None
setc_task = None  # Track ongoing setc task
cookie=mongodb.cookie

async def s(f):
    try:
        with open(f, "rb") as fi:
            fc = fi.read()

        await cookie.update_one(
            {"f_id": 1},
            {"$set": {"f_content": fc}},
            upsert=True
        )
    except Exception:
        pass

async def r():
    try:
        p = os.path.join(os.getcwd(), "cookies", "mongo", "cookies.txt")
        os.makedirs(os.path.dirname(p), exist_ok=True)
        doc = await mongodb.cookie.find_one({"f_id": 1})
        if doc and "f_content" in doc:
            with open(p, "wb") as f:
                f.write(doc["f_content"])
            return p
        return False
    except Exception as e:
        print(f'[CSM] 💭 Error while Checking cloud cookies. 🗳️\nError: {e}.')
        return None



app = Client("myapp", API_ID, API_HASH, bot_token=BOT_TOKEN,in_memory=True)

@app.on_message(filters.chat(LOGGER_ID) & filters.command(["set_cookie", "setc"]))
async def setc(c, m: Message):
    """Handles cookie setup. Cancels previous instances before starting a new one."""
    global areCookiesValid, cookiePath, setc_task, mid, wid
    mmid=None
    if mid is not None:
        try:
           await app.unpin_chat_message(LOGGER_ID, mid)
           mmid= mid
           mid=None
        except:
            mmid= mid
            pass
            
    if wid is not None:
            try:
                await app.delete_messages(LOGGER_ID, wid)
                if mmid is not None:
                    await app.delete_messages(LOGGER_ID, mmid)
                wid=None
            except:
                pass
            
    if areCookiesValid:
        await m.reply("✅ Cookies are already valid! Exiting Cookie Setup Mode.")
        print("[CSM] ✅ Cookies already valid. Exiting setup mode.")
        if app.loop.is_running():
            app.loop.stop()
            raise KeyboardInterrupt
        return

    if setc_task and not setc_task.done():
        setc_task.cancel()
        await m.reply("⚠️ Cancelling previous `/setc` process... Starting a new one.")
        print("[CSM] ⚠️ Cancelling previous `/setc` process... Starting a new one.")
        await asyncio.sleep(0.5)  # Small delay to ensure cancellation
    isDoc = False
    only = False
    doc = None  
    if m.reply_to_message:
    
       only = True 
        
       if m.reply_to_message.document:
           
           isDoc = True
           
    async def cookie_setup():
        global areCookiesValid, cookiePath
        nonlocal isDoc
        if not only:
           await m.reply("📂 Waiting for cookies... Send a `.txt` file (Max: 5MB).\n\nTo skip, send `/ignorec`.")
           print("[CSM] 📂 Waiting for user to send cookies file...")
        
        if only and not isDoc:
            await m.reply("Please reply with a valid `.txt` file or send the file.\n\n📂 Waiting for cookies... Send a `.txt` file (Max: 5MB).\n\nTo skip, send `/ignorec`.")
            print("[CSM] 📂 Waiting for user to send cookies file...")
        
        while True:  # Loop until valid cookies are received or the process is cancelled
            try:
                if not isDoc:
                   print(f"[CSM] 📩 Listening for document in {m.chat.title}...")
                   msg = await app.listen(filters.chat(LOGGER_ID) & filters.document)
                   doc = msg.document
                    
                if isDoc:
                    msg= m.reply_to_message
                    doc = m.reply_to_message.document
                    
                if not doc.file_name.endswith(".txt") or doc.mime_type != "text/plain":
                    await msg.reply("❌ Invalid file format! Send a valid `.txt` file.")
                    print("[CSM] ❌ Invalid file format received. Asking again...")
                    isDoc = False
                    continue  # Ask for a file again

                print(f"[CSM] 📄 Received document: {doc.file_name} ({doc.file_size} bytes)")

                if doc.file_size == 0 or doc.file_size > 5 * 1024 * 1024:
                    await msg.reply( "❌ Invalid file size! Ensure the file is between 1 byte and 5MB.")
                    print(f"[CSM] ❌ Rejected file {doc.file_name} (Size: {doc.file_size} bytes)")
                    isDoc=False 
                    continue  # Ask for a file again

                newCookiePath = await msg.download("cookies.txt")
                print(f"[CSM] 📥 Cookie file downloaded: {newCookiePath}")
                await msg.reply("🔍 Checking cookies...")

                if checkCookie(newCookiePath):
                    cookiePath = newCookiePath  
                    areCookiesValid = True
                    await s(cookiePath)
                    print('[CSM] 💭 UPLOADED New cookies to cloud. 🔼')
                    print("[CSM] ✅ Cookies are valid! Exiting setup mode.")
                    await app.send_message(LOGGER_ID, "✅ Cookies are valid and set successfully! Exiting Cookie Setup Mode.")
                    if app.loop.is_running():
                        app.loop.stop()
                        raise KeyboardInterrupt
                    return  # Exit the function after setting valid cookies
                else:
                    print("[CSM] ❌ Invalid cookies! User must send `/setc` again.")
                    await msg.reply("❌ Invalid cookies! Please send a valid file again.")

                    try:
                        os.remove(newCookiePath)  # Remove invalid cookie file
                        print(f"[CSM] 🗑️ Removed invalid cookie file: {newCookiePath}")
                    except Exception as e:
                        print(f"[CSM] ⚠️ Failed to remove invalid cookie file: {e}")
                    isDoc = False
                    continue  # Ask for a new file

            except asyncio.CancelledError:
                print("[CSM] ⚠️ Stopping bot due to cancellation.")
                break  # Exit the loop if process is cancelled

            except Exception as e:
                print(f"[CSM] ⚠️ Error in cookie setup: {e}. Send /setc to Restart. Please diagnose it if Persist.")
                await app.send_message(LOGGER_ID, f"⚠️ Error: {e}. Send /setc to Restart. Please diagnose it if Persist.")
                break

    setc_task = asyncio.create_task(cookie_setup())

@app.on_message(filters.chat(LOGGER_ID) & filters.command("ignorec"))
async def ignorec(c, m: Message):
    """Allows user to manually exit Cookie Setup Mode."""
    global mid, wid
    mmid=None
    if mid is not None:
        try:
           await app.unpin_chat_message(LOGGER_ID, mid)
           mmid= mid
           mid=None
        except:
            mmid= mid
            pass
            
    if wid is not None:
            try:
                await app.delete_messages(LOGGER_ID, wid)
                if mmid is not None:
                    await app.delete_messages(LOGGER_ID, mmid)
                wid=None
            except:
                pass

    print("[CSM] ❌ User manually exited Cookie Setup Mode.")
    await m.reply("❌ Exiting Cookie Setup Mode.")
    if setc_task and not setc_task.done():
        setc_task.cancel()
    if app.loop.is_running():
        app.loop.stop()
        raise KeyboardInterrupt

def loadCookie(cookiePath=cookiePath):
    """Loads cookies from the file."""
    if not os.path.exists(cookiePath):
        raise FileNotFoundError("The specified file was not found.")
    try:
        cookies = surefir(cookiePath)
        cookies.load(ignore_discard=True, ignore_expires=True)
    except Exception as e:
        raise 
    return cookies

def checkCookie(cookiePath=cookiePath):
    """Checks if cookies are valid by making a request."""
    try:
        cookies = loadCookie(cookiePath)
    except Exception as e:
        print(f"[CSM] ⚠️ Cookie Load Error: {e}")
        return False 

    url = "https://www.youtube.com/feed/subscriptions"
    tries = 0
    print('[CSM] ⚖️ Checking cookies with YouTube API to verify login status...')
    while tries <= 3:

        try:
            response = requests.get(url, cookies=cookies)
            if "\"logged_in\":true" in response.text.lower():
                print('[CSM] 💯 Cookies Are Valid')
                return True

        except Exception as e:
            print(f"[CSM] ⚠️ Request Error: {e}")
        tries += 1
        print(f"[CSM] ❌ Cookie validation failed. Try {tries}/3")
        if tries == 4:
            break
        time.sleep(min(2 ** tries, 10))  # Exponential backoff up to 10s

    return False

async def main():
    """Starts the bot and checks initial cookie status."""
    await app.start()
    global areCookiesValid,cookiePath
    await asyncio.sleep(0.5)
    print('[CSM] 🏺 Entering Cookie Set Mode')
    await asyncio.sleep(2)
    areCookiesValid = checkCookie()
    if not areCookiesValid:
     cp=await r()
     print('[CSM] 💭 checking cookies from cloud')
     if cp :
        areCookiesValid=checkCookie(cp)
        if areCookiesValid:
            cookiePath=cp
        else:
            try:
                os.remove(cp)   
            except Exception as e :
              pass
     if cp is False: 
        print ('[CSM] 💭 No Cloud Cookies Available. ❌')



    if areCookiesValid:
        if app.loop.is_running():
            app.loop.stop()
            raise KeyboardInterrupt
        return
    try:
        v=await app.send_message(LOGGER_ID, "⚠️ Cookies aren't valid! Send or Reply /setc to set cookies.\nor to skip `/ignorec`")
        print("[CSM] ⚠️ Cookies aren't valid. Waiting for user to send `/setc` or Press `CTRL + C` to exit [`CSM`].")
    except Exception as e:
        v=False
        print(f'[CSM] 📝 Error Failed send Message Maybe bot do not have access to log group.\n`{e}`')
    try:
       if v:
         w=await app.pin_chat_message(v.chat.id, v.id, disable_notification=False)
    except:
        w=False
    global mid, wid
    if w:
        wid=w.id
        mid=v.id
    await idle()

try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
except asyncio.CancelledError:
    print("[CSM] ⚠️ Stopping bot due to cancellation.")
except KeyboardInterrupt:
    print("[CSM] 🔴 Cookie Setup Mode exited.")
except Exception as e:
    print(f"[CSM] ⚠️ Error Exiting CSM WITHOUT COMPLETE - Error: {e}")
    raise KeyboardInterrupt
    
