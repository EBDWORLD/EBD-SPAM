# Mighty X Spam | @MightyXSpam
# Keep Credits Madafaka !!
import os
import asyncio
import sys
import git
import heroku3
from MightyXSpam import Mig, Mig2, Mig3, Mig4, Mig5 , Mig6, Mig7, Mig8, Mig9, Mig10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, mightyversion, mention
from MightyXSpam import CMD_HNDLR as hl
from telethon.tl.functions.users import GetFullUserRequest
from MightyXSpam import ALIVE_NAME, ALIVE_PIC, ALIVE_TEXT
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

MIG_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/2ead82e77994638db6e39.jpg"

MIG_TEXT = ALIVE_TEXT if ALIVE_TEXT else "โยปโ ๐ ๐ถ๐ด๐ต๐๐๐ซ๐ฆ๐ฝ๐ฎ๐บ ๐ถ๐ ๐๐ฒ๐ฟ๐ฒ โยซโ"

                                  
@Mig.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Mig2.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Mig3.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Mig4.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Mig5.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Mig6.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Mig7.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Mig8.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Mig9.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
@Mig10.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event):
  if event.sender_id in SUDO_USERS:
      start = datetime.now()
      text = "๐๐ฉ๐ฆ๐ค๐ฌ๐ช๐ฏ๐จ..."
      check = await event.reply(text, parse_mode=None, link_preview=None )
      end = datetime.now()
      ms = (end-start).microseconds / 1000
      await check.delete()
      await event.client.send_file(event.chat_id,
                                  MIG_PIC, caption=f"""{MIG_TEXT}\n\nโโโโโโโโโโโโโโโโโโโ\nโก ๐๐ข๐ง๐   : `{ms}แตหข`\nโก ๐๐ฐ๐ง๐๐ซ : {mention}\nโก ๐๐ข๐ ๐ก๐ญ๐ฒ ๐ ๐๐ฉ๐๐ฆ : `{mightyversion}`\nโก ๐๐ฒ๐ญ๐ก๐จ๐ง ๐๐๐ซ๐ฌ๐ข๐จ๐ง : `3.9.6`\nโก ๐๐๐ฅ๐๐ญ๐ก๐จ๐ง ๐๐๐ซ๐ฌ๐ข๐จ๐ง : `{version.__version__}`\nโโโโโโโโโโโโโโโโโโโ\n\n""", buttons=[
        [
        Button.url("โจ แดสแดษดษดแดส โจ", "https://t.me/MightyXUpdates"),
        Button.url("โจ sแดแดแดแดสแด โจ", "https://t.me/MightyXSupport")
        ],
        [
        Button.url("๐ฅ สแดแดแด ๐ฅ", "https://github.com/BeingMighty/MightyBotSpamDeploy")
        ]
        ]
        )
    
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@Mig.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Mig10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        text = "๐๐ค๐ฃ๐!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        message = await event.get_reply_message()
        user = await event.client(GetFullUserRequest(message.sender_id))
        firstname = user.user.first_name
        userid = user.user.id
    if userid == OWNER_ID:
        await event.edit(f"โโโโโ โโโโโโ โโโโโ\nโโโโโ โโโโโโ โโโโโ\nโโโโโ โโโโโโ โโโโโ\n\n    โก ๐๐ข๐ ๐ก๐ญ๐ฒ ๐ ๐๐ฉ๐๐ฆ โก\n\n๐๐ข๐ง๐  : `{ms}` แดs\n๐๐ฐ๐ง๐๐ซ : {mention}")
    else:
        await event.edit(f"โโโโโ โโโโโโ โโโโโ\nโโโโโ โโโโโโ โโโโโ\nโโโโโ โโโโโโ โโโโโ\n\n    โก ๐๐ข๐ ๐ก๐ญ๐ฒ ๐ ๐๐ฉ๐๐ฆ โก\n\n๐๐ข๐ง๐  : `{ms}` แดs\n๐๐ฎ๐๐จ ๐๐ฌ๐๐ซ : [{firstname}](tg://user?id={userid})")
        
        

@Mig.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig2.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig3.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig4.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig5.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig6.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig7.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig8.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig9.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Mig10.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "**Restarting Your Mighty X Spam...**\nPlease Wait For Few Seconds."
        await e.reply(text)
        try:
            await Mig.disconnect()
        except Exception:
            pass
        try:
            await Mig2.disconnect()
        except Exception:
            pass
        try:
            await Mig3.disconnect()
        except Exception:
            pass
        try:
            await Mig4.disconnect()
        except Exception:
            pass
        try:
            await Mig5.disconnect()
        except Exception:
            pass
        try:
            await Mig6.disconnect()
        except Exception:
            pass
        try:
            await Mig7.disconnect()
        except Exception:
            pass
        try:
            await Mig8.disconnect()
        except Exception:
            pass
        try:
            await Mig9.disconnect()
        except Exception:
            pass
        try:
            await Mig10.disconnect()
        except Exception:
            pass

        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
        

Heroku = heroku3.from_key(HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
sudousers = os.environ.get("SUDO_USER", None)

@Mig.on(events.NewMessage(incoming=True, pattern=r"\%saddsudo(?: |$)(.*)" % hl))
async def tb(event):
    if event.sender_id == OWNER_ID:
        ok = await event.reply(f"__Adding User As Sudo...__")
        mighty = "SUDO_USER"
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease Setup Your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            target = await get_user(event)
        except Exception:
            await ok.edit(f"Reply To a User !!")
        if sudousers:
            newsudo = f"{sudousers} {target}"
        else:
            newsudo = f"{target}"
        await ok.edit(f"**Added** `{target}` **As Sudo User** โจ \nRestarting... Please Wait Few Seconds.")
        heroku_var[mighty] = newsudo   
   
     
async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    target = replied_user.user.id
    return target
