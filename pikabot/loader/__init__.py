from telethon import *
from importlib.util import *
from ..resources.reqfxns import *
import logging
import sys
from var import Var           
from sys import modules
import pikabot
from pikabot import bot, tgbot, pikatgbot, ItzSjDude
from pikabot.core import pdb, pget
import pikabot.utils as _utilz
from pathlib import Path as _asstpath
from logging import getLogger
logpl = getLogger("Plugins:")
logpa = getLogger("Assistant:")

def pika_assistant(_pikasst=None):
    if pdb.Asstt:
        rx = "!"
        import plugins.__init__ as _Modules
        asst = module_from_spec(spec_from_file_location("pikabot.Assistant.plugins.{}".format(_pikasst), _asstpath(f"./pikabot/Assistant/plugins/{_pikasst}.py")))
                               #____Pikabot__Assistant__Plugins__Loader____
        userbot = pikabot; asst.bot = bot; asst.tgbot = tgbot; asst.Var = Var; asst.rx = rx; asst.ItzSjDude = ItzSjDude; asst.pikatgbot = pikatgbot; modules['Asst_modules'] = _Modules       
        PikaAsst[_pikasst] = asst; modules["pikabot"+_pikasst] = asst; tgbot.PikaAsst[_pikasst] = asst; spec.loader.exec_module(asst); logpa.info("🔥Imported "+_pikasst)
       
    else: 
       return 

def pika_plugins(_pikamod=None):
    from pathlib import Path 
    _rx=pget("alpha", "cmdhandler")
    if _rx: 
        rx = _rx
    else: 
        rx = "."
    path = Path(f"plugins/{_pikamod}.py")
    name = "plugins.{}".format(_pikamod)
    spec = spec_from_file_location(name, path)
    _pika = module_from_spec(spec)
                                   #____Pikabot__Plugins__Loader____
    userbot = pikabot; _pika.bot = bot; _pika.Var = Var; _pika.rx = rx; _pika.ItzSjDude = ItzSjDude; _pika.Config = Var; _pika.borg = bot; _pika.logger = logging.getLogger(_pikamod)
    modules["userbot"] = pikabot; modules["userbot.utils"] = _utilz; spec.loader.exec_module(_pika); bot.pika_cmd[_pikamod] = _pika; modules["pikabot"+_pikamod] = _pika; logpl.info("🔥Imported "+_pikamod)

def load_ext_module(shortname):
    if shortname.endswith("_"):
        from pathlib import Path
        path = Path(f"plugins/{shortname}.py")
        name = "plugins.{}".format(shortname)
        spec = spec_from_file_location(name, path)
        mod = module_from_spec(spec)
        spec.loader.exec_module(mod)


def remove_plugin(shortname):
    try:
        try:
            for i in LOAD_PLUG[shortname]:
                if bot is not None:
                    bot.remove_event_handler(i)
                if bot2 is not None:
                    bot2.remove_event_handler(i)
                if bot3 is not None:
                    bot3.remove_event_handler(i)
                if bot4 is not None:
                    bot4.remove_event_handler(i)
            del LOAD_PLUG[shortname]

        except BaseException:
            name = f"plugins.{shortname}"
            if bot is not None:
                for i in reversed(range(len(bot._event_builders))):
                    ev, cb = bot._event_builders[i],
                    if cb.__module__ == name:
                        del bot._event_builders[i]
            if bot2 is not None:
                for i in reversed(range(len(bot2._event_builders))):
                    ev, cx = bot2._event_builders[i],
                    if cx.__module__ == name:
                        del bot2._event_builders[i]
            if bot3 is not None:
                for i in reversed(range(len(bot3._event_builders))):
                    ev, cy = bot3._event_builders[i],
                    if cy.__module__ == name:
                        del bot3._event_builders[i]
            if bot4 is not None:
                for i in reversed(range(len(bot4._event_builders))):
                    ev, cz = bot4._event_builders[i],
                    if cz.__module__ == name:
                        del bot4._event_builders[i]
    except BaseException:
        raise ValueError
