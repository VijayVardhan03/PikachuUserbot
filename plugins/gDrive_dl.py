"""
G-Drive File Downloader Plugin For Userbot.
usage: {i}gdl File-Link
"""
# By: @Zero_cool7870


@ItzSjDude(pattern=r"gdl", outgoing=True)
@ItzSjDude(pattern=r"gdl", sudo=True)
async def _(event):
    await _gdl(event)
