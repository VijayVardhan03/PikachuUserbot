"""Plugin which transforms your text into anime stickers
{i}waifu <yourText>
"""
from . import waifu


@ItzSjDude(outgoing=True, pattern="waifu(?: |$)(.*)")
@ItzSjDude(sudo=True, pattern="waifu(?: |$)(.*)")
async def _(animu):
    await waifu(animu)
