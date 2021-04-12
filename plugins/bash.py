"""For executing linux/Gnu Commands
{i}bash <cmd> """

from . import _bash


@ItzSjDude(outgoing=True, pattern="bash ?(.*)")
@ItzSjDude(sudo=True, pattern="bash ?(.*)")
async def _(event):
    await _bash(event)
