"""Dictionary Plugin
{i}mean <word>"""

# Credits @UniBorg


@ItzSjDude(outgoing=True, pattern="mean (.*)")
@ItzSjDude(sudo=True, pattern="mean (.*)")
async def _(event):
    await dict(event)
