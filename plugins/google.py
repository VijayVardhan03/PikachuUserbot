""" Powered by @Google
Available Commands:
.go <query> credits to owner of bot
"""

from . import _gsearch


@ItzSjDude(outgoing=True, pattern="go (.*)")
@ItzSjDude(sudo=True, pattern="go (.*)")
async def _(event):
    await _gsearch(event)
