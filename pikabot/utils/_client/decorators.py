import re
import inspect
import sys
from telethon import *
from pathlib import Path
from traceback import format_exc
from time import gmtime, strftime
from asyncio import create_subprocess_shell as asyncsubshell, subprocess as asyncsub
from os import remove
from traceback import format_exc
from pikabot import *
from sys import *
from var import Var
from pathlib import Path
import re
import sys

def pika_sudo(from_client=None, **args):
    if pget("alpha", "cmdhandler"):
       plug = pget("alpha", "cmdhandler")
    else: 
       plug = "."
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    pattern = args.get("pattern", None)
    allow_sudo = True
    # get the pattern from the decorator
    if pattern is not None:
        if pattern.startswith("\#"):
            # special fix for snip.py
            args["pattern"] = re.compile(pattern)
        else:
            args["pattern"] = re.compile(plug + pattern)
            cmd = plug + pattern
            try:
                CMD_LIST[file_test].append(cmd)
                Pika_Cmd[file_test].append(cmd)
            except:
                CMD_LIST.update({file_test: [cmd]})
                Pika_Cmd.update({file_test: [cmd]})
    args["outgoing"] = True
    # should this command be available for other users?
    if allow_sudo:
        if from_client == 1:
           sudo = list(Var.SUDO_USERS1)
        if from_client == 2:
           sudo = list(Var.SUDO_USERS2)
        if from_client == 3:
           sudo = list(Var.SUDO_USERS3)
        if from_client == 4:
           sudo = list(Var.SUDO_USERS4)
                 
        args["from_users"] = sudo
        args["incoming"] = True

    elif "incoming" in args and not args["incoming"]:
        args["outgoing"] = True
        
    is_message_enabled = True

    return events.NewMessage(**args)

def ItzSjDude(**args):
    from pikabot import pget
    if pget("alpha", "cmdhandler"):
       plug = pget("alpha", "cmdhandler")
    else: 
       plug = "."
    _plug = "!"
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    pattern = args.get("pattern", None)
    args.get('disable_edited', True)
    allow_sudo = args.get("allow_sudo", False)
    disable_errors = args.get("disable_errors", False)
    args.get('disable_edited', True)
    groups_only = args.get('groups_only', False)
    trigger_on_fwd = args.get('trigger_on_fwd', False)
    trigger_on_inline = args.get('trigger_on_inline', False)
    pika = args.get("pika", False)
    args["outgoing"] = True

    if pika:
        args["incoming"] = True
        del args["pika"]

    if allow_sudo:
        args["from_users"] = list(Var.SUDO_USERS)
        args["incoming"] = True
        del args["allow_sudo"]

    elif "incoming" in args and not args["incoming"]:
        args["outgoing"] = True

    if pattern is not None:
        if pika:
            if pattern.startswith("^/"):
                pikatg = pattern.replace("^/", "\\/")
                args["pattern"] = re.compile(pikatg)

            elif pattern.startswith("\\#"):
                # special fix for snip.py
                args["pattern"] = re.compile(pattern)
            else:
                args["pattern"] = re.compile(_plug + pattern)
                pikatg = _plug + pattern

            try:
                PikaAsst[file_test].append(pikatg)
            except BaseException:
                PikaAsst.update({file_test: [pikatg]})

        else:
            if pattern.startswith("\\#"):
                args["pattern"] = re.compile(pattern)
            if pattern.startswith("^."):
                pikacmd = pattern.replace("^.", "")
                args["pattern"] = re.compile(plug + pikacmd)
                cmd = plug + pikacmd
                try:
                    Pika_Cmd[file_test].append(cmd)
                except BaseException:
                    Pika_Cmd.update({file_test: [cmd]})
            else:
                args["pattern"] = re.compile(plug + pattern)
                cmd = plug + pattern
                try:
                    Pika_Cmd[file_test].append(cmd)
                except BaseException:
                    Pika_Cmd.update({file_test: [cmd]})

    if "allow_edited_updates" in args and args["allow_edited_updates"]:
        args["allow_edited_updates"]
        del args["allow_edited_updates"]
    if "trigger_on_inline" in args:
        del args['trigger_on_inline']
    if "disable_edited" in args:
        del args['disable_edited']
    if "groups_only" in args:
        del args['groups_only']
    if "disable_errors" in args:
        del args['disable_errors']
    if "trigger_on_fwd" in args:
        del args['trigger_on_fwd']
    # check if the plugin should listen for outgoing 'messages'

    def decorator(func):
        async def wrapper(check):
            if BOTLOG:
                send_to = BOTLOG_CHATID
            if not trigger_on_fwd and check.fwd_from:
                return
            if check.via_bot_id and not trigger_on_inline:
                return
            if disable_errors:
                return
            if groups_only and not check.is_group:
                await check.respond("`I don't think this is a group.`")
                return
            try:
                await func(check)
            except events.StopPropagation:
                raise events.StopPropagation
            except KeyboardInterrupt:
                pass
            except BaseException as e:
                pikalog.exception(e)
                if not disable_errors:
                    date = strftime("%Y-%m-%d %H:%M:%S", gmtime())

                    text = "**Sorry, I encountered a error!**\n"
                    link = "[https://t.me/PikachuUserbotSupport](Pikabot Support Chat)"
                    text += "If you wanna you can report it"
                    text += f"- just forward this message to {link}.\n"
                    text += "I won't log anything except the fact of error and date\n"

                    ftext = "\nDisclaimer:\nThis file uploaded ONLY here, "
                    ftext += "we logged only fact of error and date, "
                    ftext += "we respect your privacy, "
                    ftext += "you may not report this error if you've "
                    ftext += "any confidential data here, no one will see your data "
                    ftext += "if you choose not to do so.\n\n"
                    ftext += "--------BEGIN PIKABOT TRACEBACK LOG--------"
                    ftext += "\nDate: " + date
                    ftext += "\nGroup ID: " + str(check.chat_id)
                    ftext += "\nSender ID: " + str(check.sender_id)
                    ftext += "\n\nEvent Trigger:\n"
                    ftext += str(check.text)
                    ftext += "\n\nTraceback info:\n"
                    ftext += str(format_exc())
                    ftext += "\n\nError text:\n"
                    ftext += str(sys.exc_info()[1])
                    ftext += "\n\n--------END USERBOT TRACEBACK LOG--------"

                    command = "git log --pretty=format:\"%an: %s\" -5"

                    ftext += "\n\n\nLast 5 commits:\n"

                    process = await asyncsubshell(command,
                                                  stdout=asyncsub.PIPE,
                                                  stderr=asyncsub.PIPE)
                    stdout, stderr = await process.communicate()
                    result = str(stdout.decode().strip()) \
                        + str(stderr.decode().strip())

                    ftext += result

                    file = open("error.log", "w+")
                    file.write(ftext)
                    file.close()

                    if BOTLOG:
                        await check.client.send_file(
                            send_to,
                            "error.log",
                            caption=text,
                        )
                    else:
                        await check.client.send_file(
                            check.chat_id,
                            "error.log",
                            caption=text,
                        )

                    remove("error.log")

        if bot:
            if pika:
                pass
            else:
                bot.add_event_handler(wrapper, events.NewMessage(**args))
        if bot2:
            if pika:
                pass
            else:
                bot2.add_event_handler(wrapper, events.NewMessage(**args))
        if bot3:
            if pika:
                pass

            else:
                bot3.add_event_handler(wrapper, events.NewMessage(**args))
        if bot4:
            if pika:
                pass
            else:
                bot4.add_event_handler(wrapper, events.NewMessage(**args))
        if tgbot:
            if pika:
                tgbot.add_event_handler(wrapper, events.NewMessage(**args))
            else:
                pass
        try:
            LOAD_PLUG[file_test].append(wrapper)
        except Exception:
            LOAD_PLUG.update({file_test: [wrapper]})

        return wrapper
    return decorator

def admin_cmd(pattern=None, **args):
    args["func"] = lambda e: e.via_bot_id is None

    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    allow_sudo = args.get("allow_sudo", False)

    # get the pattern from the decorator
    if pattern is not None:
        if pattern.startswith("\#"):
            # special fix for snip.py
            args["pattern"] = re.compile(pattern)
        else:
            args["pattern"] = re.compile("\." + pattern)
            cmd = "." + pattern
            try:
                CMD_LIST[file_test].append(cmd)
            except:
                CMD_LIST.update({file_test: [cmd]})

    args["outgoing"] = True
    # should this command be available for other users?
    if allow_sudo:
        args["from_users"] = list(Var.SUDO_USERS)
        # Mutually exclusive with outgoing (can only set one of either).
        args["incoming"] = True
        del args["allow_sudo"]

    # error handling condition check
    elif "incoming" in args and not args["incoming"]:
        args["outgoing"] = True

    # add blacklist chats, UB should not respond in these chats
    allow_edited_updates = False
    if "allow_edited_updates" in args and args["allow_edited_updates"]:
        allow_edited_updates = args["allow_edited_updates"]
        del args["allow_edited_updates"]

    # check if the plugin should listen for outgoing 'messages'
    is_message_enabled = True

    return events.NewMessage(**args)

async def progress(current, total, event, start, type_of_ps, file_name=None):
    """Generic progress_callback for both
    upload.py and download.py"""
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "[{0}{1}]\nProgress: {2}%\n".format(
            ''.join(["█" for i in range(math.floor(percentage / 5))]),
            ''.join(["░" for i in range(20 - math.floor(percentage / 5))]),
            round(percentage, 2))
        tmp = progress_str + \
            "{0} of {1}\nETA: {2}".format(
                humanbytes(current),
                humanbytes(total),
                time_formatter(estimated_total_time)
            )
        if file_name:
            await event.edit("{}\nFile Name: `{}`\n{}".format(
                type_of_ps, file_name, tmp))
        else:
            await event.edit("{}\n{}".format(type_of_ps, tmp))


def humanbytes(size):
    """Input size in bytes,
    outputs in a human readable format"""
    # https://stackoverflow.com/a/49361727/4723940
    if not size:
        return ""
    # 2 ** 10 = 1024
    power = 2**10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"


def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
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
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time
    
def time_formatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + " day(s), ") if days else "") + \
        ((str(hours) + " hour(s), ") if hours else "") + \
        ((str(minutes) + " minute(s), ") if minutes else "") + \
        ((str(seconds) + " second(s), ") if seconds else "") + \
        ((str(milliseconds) + " millisecond(s), ") if milliseconds else "")
    return tmp[:-2]


class Loader():
    def __init__(self, func=None, **args):
        self.Var = Var
        bot.add_event_handler(func, events.NewMessage(**args))


__all__=['ItzSjDude', 'pika_sudo', 'admin_cmd', 'time_formatter', 'get_readable_time', 'humanbytes', 'progress']
