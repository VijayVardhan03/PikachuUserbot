"""Telegraph and Other Utilities
Available Commands:
{i}app <appname>
{i}tm <as reply to a media>
{i}tt <as reply to a large text>

**Android Related Commands**
{i}magisk
**Usage**:Get latest Magisk releases\n
{i}device <codename>
**Usage**: Get info about android device codename or model.\n
{i}codename <brand> <device>
**Usage**: Search for android device codename.\n
{i}specs <brand> <device>
**Usage**: Get device specifications info.\n
{i}twrp <codename>
**Usage**: Get latest twrp download for android device.\n
"""

from . import codename_info, device_info, dspecs, magisk, twrp
from . import _invite, _telegraph, apk

@ItzSjDude(outgoing=True, pattern="magisk$")
@ItzSjDude(sudo=True, pattern="magisk$")
async def _(request):
    await magisk(request)


@ItzSjDude(outgoing=True, pattern=r"device(?: |$)(\S*)")
@ItzSjDude(sudo=True, pattern=r"device(?: |$)(\S*)")
async def _(request):
    await device_info(request)


@ItzSjDude(outgoing=True, pattern=r"codename(?: |)([\S]*)(?: |)([\s\S]*)")
@ItzSjDude(sudo=True, pattern=r"codename(?: |)([\S]*)(?: |)([\s\S]*)")
async def _(request):
    await codename_info(request)


@ItzSjDude(outgoing=True, pattern=r"specs(?: |)([\S]*)(?: |)([\s\S]*)")
@ItzSjDude(sudo=True, pattern=r"specs(?: |)([\S]*)(?: |)([\s\S]*)")
async def _(request):
    await dspecs(request)


@ItzSjDude(outgoing=True, pattern=r"twrp(?: |$)(\S*)")
@ItzSjDude(sudo=True, pattern=r"twrp(?: |$)(\S*)")
async def _(request):
    await twrp(request)


@ItzSjDude(outgoing=True, pattern="app (.*)")
async def _(e):
    await apk(e)


@ItzSjDude(outgoing=True, pattern="invite ?(.*)")
async def _(event):
    await _invite(event)


@ItzSjDude(outgoing=True, pattern="t(m|t) ?(.*)")
async def _(event):
    await _telegraph(event)
