#!/usr/bin/env python3
#
# Copyright (C) 2020 by ItzSjDude@Github, < https://github.com/ItzSjDude/PikachuUserbot >.
#
# This file is part of < https://github.com/ItzSjDude/PikachuUserbot > project,
# and is released under the "GNU v3.0 License Agreement".
# 
# Please see < https://github.com/ItzSjDude/PikachuUserbot/blob/master/LICENSE >
#
# All rights reserved 

from pikabot import is_user_exist, add_user
from Asst_modules import telethon, os, Button, custom, events, GetFullUserRequest, Pika_CallBack, re

pic = os.environ.get("START_PIC", None)
if pic:
 pic = pic
else:
 pic = "https://telegra.ph/file/2178b5a5b578d9f84d2e8.jpg"

@ItzSjDude(pattern='^/start', pika=True)
async def start(event):
    botuname = (await event.client.get_me()).username
    replied_user = await event.client(GetFullUserRequest(event.sender_id))
    fname = replied_user.user.first_name
    pname = (await bot.get_me()).first_name
    stext = f"Hi {fname}, my name is {botuname}\n\n<// I am {pname}'s Assistant / Group Management Bot with a lot of Special Features. //>\n\n**Powered By** [PikachuUserbot](t.me/PikachuUserbot)\nDeveloped By  @ItzSjDude"
    if event.sender_id == bot.uid:
        await tgbot.send_message(event.chat_id, "Hi Master, Your Assistant / Group Manager Bot is Here 🙋\n\nDo /help to Reveal all Commands", buttons=[[custom.Button.inline("Users List", data= "pikalist")], [custom.Button.url("Add Me to Group 👥", f"t.me/{botuname}?startgroup=true")],])
    else:
        if is_user_exist(event.sender_id):
            pass
        else: 
            add_user(event.sender_id)
        await tgbot.send_file(
            event.chat_id,
            file=pic,
            caption=stext,
            link_preview=False,
            buttons=[
                [custom.Button.inline("Deploy your Own PikaBot", data="pika8")],
                [Button.url("Need Help ❓", "t.me/pikachuUserbotSupport")],
            ],
        )




