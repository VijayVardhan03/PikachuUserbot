#!/usr/bin/env python3
#
# copyright (c) 2020 by itzsjdude@github, < https://github.com/itzsjdude/pikachuuserbot >.
#
# this file is part of < https://github.com/itzsjdude/pikachuuserbot > project,
# and is released under the "gnu v3.0 license agreement".
#
# please see < https://github.com/itzsjdude/pikachuuserbot/blob/master/license >
#
# all rights reserved

from ...utils import pika_msg
from ..login import pika_login
from ...clients import bot, bot2, bot3, bot4, tgbot
from ..logit import *
from sys import *
import asyncio, os
from telethon import *
from pathlib import Path
from logging import getLogger
from telethon.tl.types import *
import telethon.utils as tutils
from telethon.errors.rpcerrorlist import *
import time
pikalog = getLogger(__name__)

async def pikabot(): 
    from ...core.database import pdb
    if bot is None:
        pikalog.info(
           "**mainclient**: started login assistent, do /start at {}'s pm".format(pdb.Bf_uname))
        await pika_login("alpha")
    else:
        _const = {}
        _start = True
        _logstr_ = "__{}__: connected 🔥"
        _logstr2_ = "__{}__: started login assistent, do /start at {}'s pm".format(
            _const, Pdb.bf_uname)
        import glob
        path = './plugins/*.py'
        _path = './pikabot/assistant/plugins/*.py'
        files = glob.glob(path)
        _files = glob.glob(_path)

        if _start:
            await tgbot.start()
            tgbot.me = await tgbot.get_me()
            tgbot.pikaasst = {}
            tgbot.uid = tutils.get_peer_id(tgbot.me)
            pikalog.info(_logstr_.format("tgbot"))
            msg = _logstr_.format("_tgbot_") + '\n\n'
            _logpika = await tgbot.send_message(pdb.Botlog_chat, msg)
            if pdb.Alpha:
                try:
                    await bot.start()
                    bot.me = await bot.get_me()
                    bot.pika_cmd = {}
                    bot.uid = tutils.get_peer_id(bot.me)
                    pikalog.info(_logstr_.format("mainclient"))
                    msg += _logstr_.format("mainclient") + "\n\n"
                    await pika_msg(_logpika, msg)
                except exception as e:
                    pikalog.info(str(e))
                    pikalog.info(_logstr2_.format("mainclient"))
                    msg += _logstr2_.format("mainclient") + "\n\n"
                    await pika_msg(_logpika, msg)
                    await pika_login("alpha")

            if pdb.Beta:
                try:
                    await bot2.start()
                    pikalog.info(_logstr_.format("multiclient1"))
                    bot2.me = await bot2.get_me()
                    bot2.uid = tutils.get_peer_id(bot2.me)
                    msg += _logstr_.format("multiclient1") + "\n\n"
                    await pika_msg(_logpika, msg)
                except baseexception:
                    pikalog.info(_logstr2_.format("multiclient1"))
                    msg += _logstr2_.format("multiclient1") + "\n\n"
                    await pika_msg(_logpika, msg)
                    await pika_login("beta")
            if pdb.Gaama:
                try:
                    await bot3.start()
                    pikalog.info(_logstr2_.format("multiclient2"))
                    bot3.me = await bot3.get_me()
                    bot3.uid = tutils.get_peer_id(bot3.me)
                    msg += _logstr_.format("multiclient2") + "\n\n"
                    await pika_msg(_logpika, msg)
                except baseexception:
                    pikalog.info(_logstr2_.format("multiclient2"))
                    msg += _logstr2_.format("multiclient2") + "\n\n"
                    await pika_msg(_logpika, msg)
                    await pika_login("gaama")
            if pdb.Delta:
                try:
                    await bot4.start()
                    pikalog.info(_logstr_.format("multiclient3"))
                    bot4.me = await bot4.get_me()
                    bot4.uid = tutils.get_peer_id(bot4.me)
                    msg += logstr_.format("multiclient3") + "\n\n"
                    await pika_msg(_logpika, msg)
                except baseexception:
                    pikalog.info(_logstr2_.format("multiclient3"))
                    msg += _logstr2_.format("multiclient3") + "\n\n"
                    await pika_msg(_logpika, msg)
                    await pika_login("delta")

            def __load_plugs__():
                from .loader import pika_plugins, pika_assistant
                for name in files:
                    with open(name) as f:
                        path1 = Path(f.name)
                        shortname = path1.stem
                        pika_plugins(shortname.replace(".py", ""))

                for name in _files:
                    with open(name) as f:
                        _asstpath = Path(f.name)
                        shortname = _asstpath.stem
                        pika_assistant(shortname.replace(".py", ""))
            __load_plugs__()

            msg += "sucessfully loaded plugins\n\n"
            await pika_msg(_logpika, msg)
            msg += "**pikabot started sucessfully**"
            await pika_msg(_logpika, msg)

        if len(argv) not in (1, 3, 4):
            if bot:
                await bot.disconnect()
            if client2:
                await bot2.disconnect()
            if client3:
                await bot3.disconnect()
            if client4:
                await bot4.disconnect()
        else:
            if bot:
                await bot.run_until_disconnected()
            if bot2:
                await client2.run_until_disconnected()
            if bot3:
                await client3.run_until_disconnected()
            if bot4:
                await client4.run_until_disconnected()
