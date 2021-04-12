"""Globally bans User
{i}gban <userid/username/mention> <Reason>
"""
from . import gban


@ItzSjDude(outgoing=True, pattern="gban(?: |$)(.*)")
@ItzSjDude(sudo=True, pattern="gban(?: |$)(.*)")
async def _(event):
    await gban(event)
